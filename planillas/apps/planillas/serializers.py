# apps/planillas/serializers.py
from rest_framework import serializers
from .models import Periodo, PlanillaBeneficiario, Contrato, Planilla, Boleta, BoletaTransaccion
from django.db import transaction
from apps.transacciones.models import TransaccionContrato

class BoletaTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoletaTransaccion
        fields = '__all__'
        extra_kwargs = {
            'contrato': {'required': False, 'allow_null': True},
            'transaccion': {'required': False, 'allow_null': True},
        }
        ref_name = 'BoletaTransaccionSerializerPlanillas'
# La clase de abajo se usa para poder registrar transacciones al momento de crear o actualizar un contrato
class TransaccionContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionContrato
        fields = '__all__'

class PlanillaBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanillaBeneficiario
        fields = '__all__'
        ref_name = 'PlanillaBeneficiarioSerializerPlanillas'

    def validate_monto(self, value):
        if value < 0:
            raise serializers.ValidationError("El monto no puede ser negativo.")
        return value

class ContratoSerializer(serializers.ModelSerializer):
    transacciones = TransaccionContratoSerializer(many=True, write_only=True, required=False)
    transacciones_detalles = TransaccionContratoSerializer(many=True, read_only=True, source='transacciones')

    class Meta:
        model = Contrato
        fields = '__all__'

    def validate(self, data):
        if 'fecha_cese' in data and data['fecha_cese'] and data['fecha_cese'] <= data['fecha_ingreso']:
            raise serializers.ValidationError("La fecha de cese debe ser posterior a la fecha de ingreso.")
        if data['dias_laborados'] < 0 or data['dias_laborados'] > 30:
            raise serializers.ValidationError("Los días laborados deben estar entre 0 y 30.")
        if data.get('sueldo') and data['sueldo'] <= 0:
            raise serializers.ValidationError("El sueldo debe ser mayor que cero.")
        if data['jornada_laboral'] < 0 or data['jornada_laboral'] > 48:
            raise serializers.ValidationError("La jornada laboral debe estar entre 0 y 48 horas.")
        return data


    def validate_sueldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("El sueldo debe ser mayor que cero.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        transacciones_data = validated_data.pop('transacciones', [])
        contrato = Contrato.objects.create(**validated_data)
        for transaccion_data in transacciones_data:
            if transaccion_data:
                TransaccionContrato.objects.create(contrato=contrato, **transaccion_data)
        return contrato

    @transaction.atomic
    def update(self, instance, validated_data):
        transacciones_data = validated_data.pop('transacciones', [])
        instance = super().update(instance, validated_data)

        if transacciones_data:
            instance.transacciones.all().delete()
            for transaccion_data in transacciones_data:
                if transaccion_data:
                    TransaccionContrato.objects.create(contrato=instance, **transaccion_data)

        return instance

class PlanillaSerializer(serializers.ModelSerializer):
    contratos = ContratoSerializer(many=True, required=False)

    class Meta:
        model = Planilla
        fields = '__all__'

    def validate_correlativo(self, value):
        if len(value) != 3:
            raise serializers.ValidationError("El correlativo debe tener 3 caracteres.")
        return value

    def validate(self, data):
        if data['total_haberes'] < 0:
            raise serializers.ValidationError("El total de haberes no puede ser negativo.")
        if data['total_descuentos'] < 0:
            raise serializers.ValidationError("El total de descuentos no puede ser negativo.")
        if data['total_aportes'] < 0:
            raise serializers.ValidationError("El total de aportes no puede ser negativo.")
        if data['estado'] not in dict(Planilla.ESTADO_CHOICES):
            raise serializers.ValidationError("El estado no es válido.")
        return data

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

    def validate(self, data):
        if data['total_haberes'] < 0:
            raise serializers.ValidationError("El total de haberes no puede ser negativo.")
        if data['total_descuentos'] < 0:
            raise serializers.ValidationError("El total de descuentos no puede ser negativo.")
        if data['total_aportes'] < 0:
            raise serializers.ValidationError("El total de aportes no puede ser negativo.")
        if data['neto_a_pagar'] < 0:
            raise serializers.ValidationError("El neto a pagar no puede ser negativo.")
        return data