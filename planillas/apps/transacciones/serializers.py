# apps/transacciones/serializers.py
from rest_framework import serializers
from .models import TransaccionContrato

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionContrato
        fields = '__all__'
        ref_name = 'TransaccionTrabajadorSerializerTransacciones'

    def validate(self, data):
        if data['periodo_final'] < data['periodo_inicial']:
            raise serializers.ValidationError("El periodo final no puede ser anterior al periodo inicial.")
        if data['monto'] < 0:
            raise serializers.ValidationError("El monto no puede ser negativo.")
        return data