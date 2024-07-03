# apps/procesos/services.py
from django.db import transaction
from decimal import Decimal
from apps.configuracion.models import Periodo, Transaccion, ComisionAfp
from apps.planillas.models import Contrato, Planilla, Boleta, BoletaTransaccion
from apps.transacciones.models import TransaccionContrato
from django.db import models
from django.db.models import Sum, Max
from django.utils import timezone


class ProcesoPlanilla:
    @staticmethod
    @transaction.atomic
    def cerrar_aperturar_periodo():
        periodo_actual = Periodo.objects.get(estado=True)
        periodo_actual.estado = False
        periodo_actual.save()

        nuevo_periodo = Periodo.objects.create(
            mes=str(int(periodo_actual.mes) + 1).zfill(2),
            anio=periodo_actual.anio if int(periodo_actual.mes) < 12 else str(int(periodo_actual.anio) + 1),
            estado=True
        )

        # Resetear días laborados en contratos
        Contrato.objects.update(dias_laborados=30)  # Asumiendo 30 días por defecto

        # Aquí puedes agregar más lógica necesaria para el cierre/apertura del periodo

    @staticmethod
    @transaction.atomic
    def calcular_planilla_remuneraciones(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)

        try:
            periodo_actual = Periodo.objects.get(estado=True)
        except Periodo.DoesNotExist:
            raise ValueError("No hay un periodo activo para procesar las planillas.")

        # Filtramos los contratos asociados a esta planilla específica
        contratos = Contrato.objects.filter(
            clase_planilla=planilla.clase_planilla,
            fuente_financiamiento=planilla.fuente_financiamiento,
            trabajador__estado=True
        ).exclude(situacion__nombre_situacion__in=['Suspendido', 'Baja'])

        for contrato in contratos:
            sueldo_proporcional = (contrato.sueldo * Decimal(contrato.dias_laborados)) / Decimal('30')

            transacciones = {
                'remuneracion': Transaccion.objects.get(id=1),
                'onp': Transaccion.objects.get(id=6),
                'afp': Transaccion.objects.get(id=3),
            }

            ProcesoPlanilla.registrar_transaccion(contrato, transacciones['remuneracion'], sueldo_proporcional, periodo_actual.periodo)

            regimen_pensionario = contrato.trabajador.regimen_pensionario.codigo_regimen_pensionario

            if regimen_pensionario == '02':  # ONP
                monto_descuento = sueldo_proporcional * Decimal('0.13')
                ProcesoPlanilla.registrar_transaccion(contrato, transacciones['onp'], monto_descuento, periodo_actual.periodo)
            elif regimen_pensionario == '03':  # AFP
                try:
                    comision_afp = ComisionAfp.objects.get(afp=contrato.trabajador.afp, periodo=periodo_actual)
                    monto_descuento = sueldo_proporcional * (comision_afp.total_comision / Decimal('100'))
                    ProcesoPlanilla.registrar_transaccion(contrato, transacciones['afp'], monto_descuento, periodo_actual.periodo)
                except ComisionAfp.DoesNotExist:
                    print(f"No se encontró comisión AFP para {contrato.trabajador.afp} en el periodo {periodo_actual.periodo}")

        # Actualizar los totales de la planilla
        planilla.total_haberes = sum(t.monto for t in TransaccionContrato.objects.filter(
            contrato__in=contratos,
            transaccion__tipo_transaccion='HABER',
            periodo_inicial=periodo_actual.periodo
        ))
        planilla.total_descuentos = sum(t.monto for t in TransaccionContrato.objects.filter(
            contrato__in=contratos,
            transaccion__tipo_transaccion='DESCUENTO',
            periodo_inicial=periodo_actual.periodo
        ))
        planilla.total_aportes = sum(t.monto for t in TransaccionContrato.objects.filter(
            contrato__in=contratos,
            transaccion__tipo_transaccion='APORTE',
            periodo_inicial=periodo_actual.periodo
        ))
        planilla.save()

    @staticmethod
    def registrar_transaccion(contrato, transaccion, monto, periodo):
        TransaccionContrato.objects.update_or_create(
            contrato=contrato,
            transaccion=transaccion,
            periodo_inicial=periodo,
            periodo_final=periodo,
            defaults={
                'monto': monto,
                'estado': True
            }
        )


    @staticmethod
    @transaction.atomic
    def generar_boletas_pago(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)
        contratos = Contrato.objects.filter(
            clase_planilla=planilla.clase_planilla,
            fuente_financiamiento=planilla.fuente_financiamiento,
            trabajador__estado=True
        ).exclude(situacion__nombre_situacion__in=['Suspendido', 'Baja'])

        boletas_generadas = 0

        for contrato in contratos:
            boleta, created = Boleta.objects.get_or_create(
                contrato=contrato,
                planilla=planilla,
                defaults={
                    'centro_de_trabajo': contrato.centro_de_trabajo,
                    'cargo': contrato.cargo.nombre_cargo if contrato.cargo else '',
                    'fecha_ingreso': contrato.fecha_ingreso,
                    'fecha_cese': contrato.fecha_cese,
                    'clase_planilla': contrato.clase_planilla.nombre_clase_planilla,
                    'fuente_financiamiento': contrato.fuente_financiamiento.nombre_fuente_financiamiento,
                    'sueldo': contrato.sueldo,
                    'dias_laborados': contrato.dias_laborados,
                    'leyenda_permanente': contrato.leyenda_permanente,
                    'jornada_laboral': contrato.jornada_laboral,
                    'trabajador_nombres': contrato.trabajador.persona.nombres,
                    'trabajador_apellidos': f"{contrato.trabajador.persona.apellido_paterno} {contrato.trabajador.persona.apellido_materno}",
                    'trabajador_dni': contrato.trabajador.persona.numero_documento,
                    'regimen_laboral': contrato.regimen_laboral.nombre_regimen_laboral,
                    'tipo_servidor': contrato.tipo_servidor.nombre_tipo_servidor,
                    'regimen_pensionario': contrato.trabajador.regimen_pensionario.nombre_regimen_pensionario,
                    'banco': contrato.trabajador.banco.nombre_banco,
                    'cuenta_bancaria': contrato.trabajador.numero_cuenta,
                }
            )

            ProcesoPlanilla.calcular_totales(boleta)
            ProcesoPlanilla.generar_numero_boleta(boleta)
            ProcesoPlanilla.registrar_transacciones_boleta(boleta)
            ProcesoPlanilla.actualizar_totales_planilla(boleta)

            boletas_generadas += 1

        return f"Se generaron o actualizaron {boletas_generadas} boletas para la planilla {planilla}."

    @staticmethod
    def calcular_totales(boleta):
        transacciones = boleta.contrato.transacciones.filter(
            periodo_inicial__lte=boleta.planilla.periodo.periodo,
            periodo_final__gte=boleta.planilla.periodo.periodo,
            estado=True
        )
        boleta.total_haberes = transacciones.filter(transaccion__tipo_transaccion='HABER').aggregate(Sum('monto'))['monto__sum'] or Decimal('0')
        boleta.total_descuentos = transacciones.filter(transaccion__tipo_transaccion='DESCUENTO').aggregate(Sum('monto'))['monto__sum'] or Decimal('0')
        boleta.total_aportes = transacciones.filter(transaccion__tipo_transaccion='APORTE').aggregate(Sum('monto'))['monto__sum'] or Decimal('0')
        boleta.neto_a_pagar = boleta.total_haberes - boleta.total_descuentos
        boleta.save()

    @staticmethod
    def generar_numero_boleta(boleta):
        max_numero_boleta = Boleta.objects.filter(planilla=boleta.planilla).aggregate(Max('numero_boleta'))['numero_boleta__max']
        if max_numero_boleta:
            boleta.numero_boleta = str(int(max_numero_boleta) + 1).zfill(3)
        else:
            boleta.numero_boleta = '001'
        boleta.save()

    @staticmethod
    def registrar_transacciones_boleta(boleta):
        transacciones = boleta.contrato.transacciones.filter(
            periodo_inicial__lte=boleta.planilla.periodo.periodo,
            periodo_final__gte=boleta.planilla.periodo.periodo,
            estado=True
        )
        for transaccion in transacciones:
            BoletaTransaccion.objects.create(
                boleta=boleta,
                tipo=transaccion.transaccion.tipo_transaccion,
                codigo=transaccion.transaccion.codigo_transaccion_mcpp,
                descripcion=transaccion.transaccion.descripcion_transaccion,
                monto=transaccion.monto
            )

    @staticmethod
    def actualizar_totales_planilla(boleta):
        planilla = boleta.planilla
        planilla.total_haberes = Boleta.objects.filter(planilla=planilla).aggregate(Sum('total_haberes'))['total_haberes__sum'] or Decimal('0')
        planilla.total_descuentos = Boleta.objects.filter(planilla=planilla).aggregate(Sum('total_descuentos'))['total_descuentos__sum'] or Decimal('0')
        planilla.total_aportes = Boleta.objects.filter(planilla=planilla).aggregate(Sum('total_aportes'))['total_aportes__sum'] or Decimal('0')
        planilla.save()

    @staticmethod
    def marcar_como_visualizada(boleta):
        boleta.visualizada = True
        boleta.fecha_visualizacion = timezone.now()
        boleta.save()

    @staticmethod
    def marcar_como_descargada(boleta):
        boleta.descargada = True
        boleta.fecha_descarga = timezone.now()
        boleta.save()