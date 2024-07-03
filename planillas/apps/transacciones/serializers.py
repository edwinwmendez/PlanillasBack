# apps/transacciones/serializers.py
from rest_framework import serializers
from .models import TransaccionContrato

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionContrato
        fields = '__all__'
        ref_name = 'TransaccionTrabajadorSerializerTransacciones'
