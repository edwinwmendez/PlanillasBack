# apps/configuracion/serializers.py
from rest_framework import serializers
from .models import Ugel, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Periodo, Transaccion, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion, TipoDocumento, Sexo, TipoDescuento, TipoBeneficiario, EstadoCivil

class UgelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugel
        fields = ['id', 'nombre_ugel', 'nombre_corto_ugel']
        ref_name = 'UgelSerializerConfiguracion'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class TipoPlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlanilla
        fields = '__all__'

class ClasePlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasePlanilla
        fields = '__all__'

class FuenteFinanciamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteFinanciamiento
        fields = '__all__'


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'
        ref_name = 'TransaccionSerializerTransacciones'


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

class SituacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacion
        fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = '__all__'

class TipoDescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDescuento
        fields = '__all__'

class TipoBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBeneficiario
        fields = '__all__'

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'