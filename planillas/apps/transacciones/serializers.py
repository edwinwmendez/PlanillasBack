# apps/transacciones/serializers.py
from rest_framework import serializers
from .models import TransaccionTrabajador

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionTrabajador
        fields = '__all__'
        ref_name = 'TransaccionTrabajadorSerializerTransacciones'
