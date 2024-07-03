# apps/planillas/serializers.py
from rest_framework import serializers
from .models import Periodo, PlanillaBeneficiario, Contrato, Planilla, Boleta
from apps.transacciones.models import TransaccionContrato

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionContrato
        fields = '__all__'
        extra_kwargs = {
            'contrato': {'required': False, 'allow_null': True},
            'transaccion': {'required': False, 'allow_null': True},
        }
        ref_name = 'TransaccionTrabajadorSerializerPlanillas'


class PlanillaBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanillaBeneficiario
        fields = '__all__'
        ref_name = 'PlanillaBeneficiarioSerializerPlanillas'

class ContratoSerializer(serializers.ModelSerializer):
    transacciones = TransaccionTrabajadorSerializer(many=True, write_only=True, required=False)
    transacciones_detalles = TransaccionTrabajadorSerializer(many=True, read_only=True, source='transacciones')

    class Meta:
        model = Contrato
        fields = '__all__'

    def create(self, validated_data):
        transacciones_data = validated_data.pop('transacciones', [])
        contrato = Contrato.objects.create(**validated_data)
        for transaccion_data in transacciones_data:
            if transaccion_data:  # Verificar que transaccion_data no esté vacío
                TransaccionContrato.objects.create(contrato=contrato, **transaccion_data)
        return contrato

    def update(self, instance, validated_data):
        transacciones_data = validated_data.pop('transacciones', [])
        instance = super().update(instance, validated_data)

        if transacciones_data:
            instance.transacciones.all().delete()  # Elimina las transacciones existentes
            for transaccion_data in transacciones_data:
                if transaccion_data:  # Verificar que transaccion_data no esté vacío
                    TransaccionContrato.objects.create(contrato=instance, **transaccion_data)

        return instance

class PlanillaSerializer(serializers.ModelSerializer):
    contratos = ContratoSerializer(many=True, required=False)

    class Meta:
        model = Planilla
        fields = '__all__'

    def create(self, validated_data):
        contratos_data = validated_data.pop('contratos', [])
        planilla = Planilla.objects.create(**validated_data)
        for contrato_data in contratos_data:
            if contrato_data:  # Verificar que contrato_data no esté vacío
                contrato = Contrato.objects.create(**contrato_data)
                planilla.contratos.add(contrato)
        return planilla

    def update(self, instance, validated_data):
        contratos_data = validated_data.pop('contratos', [])
        instance = super().update(instance, validated_data)

        if contratos_data:
            instance.contratos.all().delete()  # Elimina los contratos existentes
            for contrato_data in contratos_data:
                if contrato_data:  # Verificar que contrato_data no esté vacío
                    contrato = Contrato.objects.create(**contrato_data)
                    instance.contratos.add(contrato)

        return instance

class BoletaSerializer(serializers.ModelSerializer):
    planilla = PlanillaSerializer(read_only=True)
    contrato = ContratoSerializer(read_only=True)

    class Meta:
        model = Boleta
        fields = '__all__'