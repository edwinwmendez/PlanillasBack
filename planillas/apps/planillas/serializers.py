# apps/planillas/serializers.py
from rest_framework import serializers
from .models import Periodo, PlanillaBeneficiario, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Contrato
from apps.transacciones.models import TransaccionTrabajador

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionTrabajador
        fields = '__all__'
        extra_kwargs = {
            'contrato': {'required': False, 'allow_null': True},
            'transaccion': {'required': False, 'allow_null': True},
        }
        ref_name = 'TransaccionTrabajadorSerializerPlanillas'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class PlanillaBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanillaBeneficiario
        fields = '__all__'
        ref_name = 'PlanillaBeneficiarioSerializerPlanillas'

class TipoPlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlanilla
        fields = '__all__'

class ClasePlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasePlanilla
        fields = '__all__'

class FuenteFinanciamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteFinanciamiento
        fields = '__all__'

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
                TransaccionTrabajador.objects.create(contrato=contrato, **transaccion_data)
        return contrato

    def update(self, instance, validated_data):
        transacciones_data = validated_data.pop('transacciones', [])
        instance = super().update(instance, validated_data)

        if transacciones_data:
            instance.transacciones.all().delete()  # Elimina las transacciones existentes
            for transaccion_data in transacciones_data:
                if transaccion_data:  # Verificar que transaccion_data no esté vacío
                    TransaccionTrabajador.objects.create(contrato=instance, **transaccion_data)
        
        return instance
