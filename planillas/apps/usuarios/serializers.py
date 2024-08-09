# apps/usuarios/serializers.py
from rest_framework import serializers
from .models import Persona, Beneficiario, User
from apps.configuracion.models import Ugel
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UgelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugel
        fields = ['id', 'nombre_ugel', 'nombre_corto_ugel']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [
            'id', 'user', 'tipo_documento', 'numero_documento', 'apellido_paterno', 
            'apellido_materno', 'nombres', 'fecha_nacimiento', 'sexo', 'estado_civil', 
            'direccion', 'email', 'telefono'
        ]

    def validate_numero_documento(self, value):
        tipo_documento = self.initial_data.get('tipo_documento')
        if tipo_documento == 'DNI' and (not value.isdigit() or len(value) != 8):
            raise serializers.ValidationError("El DNI debe ser un número de 8 dígitos.")
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Ingrese una dirección de correo electrónico válida.")
        return value

    def validate(self, data):
        if data.get('fecha_nacimiento'):
            from datetime import date
            today = date.today()
            age = today.year - data['fecha_nacimiento'].year - ((today.month, today.day) < (data['fecha_nacimiento'].month, data['fecha_nacimiento'].day))
            if age < 18:
                raise serializers.ValidationError("La persona debe ser mayor de 18 años.")
        return data
    
class UserSerializer(serializers.ModelSerializer):
    # persona = PersonaSerializer(read_only=True)
    ugel = UgelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'date_joined', 'ugel']

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 5 caracteres.")
        return value

    def validate(self, data):
        if data.get('role') == 'admin_ugel' and not data.get('ugel'):
            raise serializers.ValidationError("Un administrador UGEL debe tener una UGEL asignada.")
        return data
class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['id', 'trabajador', 'persona', 'relacion_trabajador', 'documento_descuento', 'numero_cuenta', 'tipo_beneficiario', 'tipo_descuento', 'descuento_fijo', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin', 'estado', 'banco', 'created', 'updated']

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 5 caracteres.")
        return value

    def validate(self, data):
        if data.get('role') == 'admin_ugel' and not data.get('ugel'):
            raise serializers.ValidationError("Un administrador UGEL debe tener una UGEL asignada.")
        return data


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
