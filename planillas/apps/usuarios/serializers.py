# apps/usuarios/serializers.py
from rest_framework import serializers
from .models import Persona, Beneficiario, User
from apps.configuracion.models import Ugel

class UgelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugel
        fields = ['id', 'nombre_ugel', 'nombre_corto_ugel']

class UserSerializer(serializers.ModelSerializer):
    ugel = UgelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'date_joined', 'ugel']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'user', 'tipo_documento', 'numero_documento', 'apellido_paterno', 'apellido_materno', 'nombres', 'fecha_nacimiento', 'sexo', 'direccion', 'email']

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['id', 'trabajador', 'persona', 'relacion_trabajador', 'documento_descuento', 'numero_cuenta', 'tipo_beneficiario', 'tipo_descuento', 'descuento_fijo', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin', 'estado', 'banco', 'created', 'updated']