# apps/transacciones/serializers.py
from rest_framework import serializers
from .models import Transaccion, TransaccionTrabajador

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'
        ref_name = 'TransaccionSerializerTransacciones'

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionTrabajador
        fields = '__all__'
        ref_name = 'TransaccionTrabajadorSerializerTransacciones'
