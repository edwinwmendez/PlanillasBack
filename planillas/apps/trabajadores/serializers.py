# apps/trabajadores/serializers.py
from rest_framework import serializers
from .models import Trabajador, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class RegimenLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegimenLaboral
        fields = '__all__'

class TipoServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServidor
        fields = '__all__'

class RegimenPensionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegimenPensionario
        fields = '__all__'

class AFPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afp
        fields = '__all__'

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'
