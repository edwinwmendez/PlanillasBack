# apps/usuarios/serializers.py
from rest_framework import serializers
from .models import Persona, Beneficiario, Ugel

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'user', 'tipo_documento', 'numero_documento', 'paterno', 'materno', 'nombres', 'fecha_nacimiento', 'sexo', 'direccion', 'email']

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['id', 'empleado', 'persona', 'relacion_trabajador', 'documento_descuento', 'numero_cuenta', 'tipo_beneficiario', 'tipo_descuento', 'descuento_fijo', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin', 'estado', 'banco', 'created', 'updated']

class UgelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugel
        fields = ['id', 'nombre_ugel', 'nombre_corto']
