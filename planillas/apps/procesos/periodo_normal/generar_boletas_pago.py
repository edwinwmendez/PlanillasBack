from django.db import transaction
from apps.planillas.models import Planilla, Boleta, Contrato, BoletaTransaccion
from django.db.models import Sum, Max
from decimal import Decimal
from django.utils import timezone


class GenerarBoletasPago:
    @staticmethod
    @transaction.atomic
    def generar(planilla_id):
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

            GenerarBoletasPago.calcular_totales(boleta)
            GenerarBoletasPago.generar_numero_boleta(boleta)
            GenerarBoletasPago.registrar_transacciones_boleta(boleta)
            GenerarBoletasPago.actualizar_totales_planilla(boleta)

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


    @staticmethod
    @transaction.atomic
    def revertir_boletas_generadas(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)

        # Obtener todas las boletas asociadas a la planilla
        boletas = Boleta.objects.filter(planilla=planilla)

        # Eliminar todas las transacciones de boletas asociadas a las boletas
        BoletaTransaccion.objects.filter(boleta__in=boletas).delete()

        # Eliminar todas las boletas asociadas a la planilla
        boletas.delete()

        # Restaurar los valores originales de la planilla (esto asume que tienes una forma de obtener los valores originales)
        planilla.total_haberes = 0
        planilla.total_descuentos = 0
        planilla.total_aportes = 0
        planilla.save()