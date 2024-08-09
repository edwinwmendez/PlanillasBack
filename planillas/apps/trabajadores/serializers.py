# apps/trabajadores/serializers.py
from rest_framework import serializers
from .models import Trabajador
from apps.usuarios.serializers import PersonaSerializer
from apps.configuracion.serializers import UgelSerializer, RegimenPensionarioSerializer, AfpSerializer, BancoSerializer
from apps.configuracion.models import Ugel, RegimenPensionario, Afp, Banco
from apps.usuarios.models import Persona
class TrabajadorSerializer(serializers.ModelSerializer):
    persona_id = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all(), source='persona', write_only=True)
    ugel_id = serializers.PrimaryKeyRelatedField(queryset=Ugel.objects.all(), source='ugel', write_only=True)
    regimen_pensionario_id = serializers.PrimaryKeyRelatedField(queryset=RegimenPensionario.objects.all(), source='regimen_pensionario', write_only=True)
    afp_id = serializers.PrimaryKeyRelatedField(queryset=Afp.objects.all(), source='afp', write_only=True)
    banco_id = serializers.PrimaryKeyRelatedField(queryset=Banco.objects.all(), source='banco', write_only=True)

    persona = PersonaSerializer(read_only=True)
    ugel = UgelSerializer(read_only=True)
    regimen_pensionario = RegimenPensionarioSerializer(read_only=True)
    afp = AfpSerializer(read_only=True)
    banco = BancoSerializer(read_only=True)

    class Meta:
        model = Trabajador
        fields = '__all__'

    def validate_tiempo_servicios(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("El tiempo de servicios no puede ser negativo.")
        return value

    def validate_cuspp(self, value):
        if value and not value.isalnum():
            raise serializers.ValidationError("El CUSPP debe contener solo letras y números.")
        return value

    def validate_numero_cuenta(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("El número de cuenta debe contener solo dígitos.")
        return value

    def validate_ruc(self, value):
        if value and (not value.isdigit() or len(value) != 11):
            raise serializers.ValidationError("El RUC debe ser un número de 11 dígitos.")
        return value