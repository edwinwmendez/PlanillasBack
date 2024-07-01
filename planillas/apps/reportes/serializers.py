# apps/reportes/serializers.py
from rest_framework import serializers
from apps.trabajadores.models import Trabajador
from apps.transacciones.models import TransaccionTrabajador
from apps.planillas.models import PlanillaBeneficiario

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField(source='transaccion.codigo')
    descripcion = serializers.CharField(source='transaccion.descripcion')

    class Meta:
        model = TransaccionTrabajador
        fields = ['codigo', 'descripcion', 'monto']
        ref_name = 'TransaccionTrabajadorSerializerReportes'

class TrabajadorSerializer(serializers.ModelSerializer):
    transacciones = TransaccionTrabajadorSerializer(many=True, read_only=True)

    class Meta:
        model = Trabajador
        fields = ['id', 'persona', 'estado', 'transacciones']
        ref_name = 'TrabajadorSerializerReportes'


class PlanillaTrabajadorSerializer(serializers.ModelSerializer):
    transacciones = TransaccionTrabajadorSerializer(many=True, source='transacciones')

    class Meta:
        model = Trabajador  # PlanillaTrabajador si es un modelo separado
        fields = ['total_haberes', 'total_descuentos', 'essalud', 'emitio_boleta', 'trabajador', 'tipo_planilla', 'periodo', 'ugel', 'transacciones']
        ref_name = 'PlanillaTrabajadorSerializerReportes'

class PlanillaBeneficiarioSerializer(serializers.ModelSerializer):
    beneficiario = serializers.StringRelatedField()

    class Meta:
        model = PlanillaBeneficiario
        fields = ['id', 'beneficiario', 'monto', 'periodo']
        ref_name = 'PlanillaBeneficiarioSerializerReportes'