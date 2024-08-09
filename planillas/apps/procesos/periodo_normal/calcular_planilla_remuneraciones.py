from django.db import transaction
from decimal import Decimal
from apps.configuracion.models import Periodo, Transaccion, ComisionAfp
from apps.planillas.models import Contrato, Planilla
from apps.transacciones.models import TransaccionContrato


class CalcularPlanillaRemuneraciones:
    @staticmethod
    @transaction.atomic
    def calcular(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)

        try:
            periodo_actual = Periodo.objects.get(estado=True)
        except Periodo.DoesNotExist:
            raise ValueError("No hay un periodo activo para procesar las planillas.")

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

            CalcularPlanillaRemuneraciones.registrar_transaccion(contrato, transacciones['remuneracion'], sueldo_proporcional, periodo_actual.periodo)

            regimen_pensionario = contrato.trabajador.regimen_pensionario.codigo_regimen_pensionario

            if regimen_pensionario == '02':  # ONP
                monto_descuento = sueldo_proporcional * Decimal('0.13')
                CalcularPlanillaRemuneraciones.registrar_transaccion(contrato, transacciones['onp'], monto_descuento, periodo_actual.periodo)
            elif regimen_pensionario == '03':  # AFP
                try:
                    comision_afp = ComisionAfp.objects.get(afp=contrato.trabajador.afp, periodo=periodo_actual)
                    monto_descuento = sueldo_proporcional * (comision_afp.total_comision / Decimal('100'))
                    CalcularPlanillaRemuneraciones.registrar_transaccion(contrato, transacciones['afp'], monto_descuento, periodo_actual.periodo)
                except ComisionAfp.DoesNotExist:
                    print(f"No se encontró comisión AFP para {contrato.trabajador.afp} en el periodo {periodo_actual.periodo}")

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
    def revertir_calculo(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)
        periodo_actual = Periodo.objects.get(estado=True)

        # Obtener contratos asociados a esta planilla
        contratos = Contrato.objects.filter(
            clase_planilla=planilla.clase_planilla,
            fuente_financiamiento=planilla.fuente_financiamiento,
            trabajador__estado=True
        ).exclude(situacion__nombre_situacion__in=['Suspendido', 'Baja'])

        # Eliminar transacciones relacionadas con estos contratos y el periodo actual
        TransaccionContrato.objects.filter(
            contrato__in=contratos,
            periodo_inicial=periodo_actual.periodo
        ).delete()

        # Restaurar los valores originales de la planilla (esto asume que tienes una forma de obtener los valores originales)
        planilla.total_haberes = 0
        planilla.total_descuentos = 0
        planilla.total_aportes = 0
        planilla.save()
