# apps/procesos/serializers.py
from rest_framework import serializers

class ProcesarPlanillaSerializer(serializers.Serializer):
    periodo = serializers.CharField(max_length=6)
    tipo_planilla = serializers.IntegerField()
