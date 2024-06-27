# apps/auditoria/serializers.py
from rest_framework import serializers
from .models import Auditoria

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = ['id', 'fecha', 'descripcion', 'persona', 'ip_address', 'user_agent', 'accion']
