# apps/autenticacion/serializers.py
from rest_framework import serializers
from .models import User
from apps.usuarios.models import Ugel

class UgelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugel
        fields = ['id', 'nombre_ugel', 'nombre_corto']

class UserSerializer(serializers.ModelSerializer):
    ugel = UgelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'date_joined', 'ugel']
