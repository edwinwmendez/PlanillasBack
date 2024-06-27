# apps/planillas/serializers.py
from rest_framework import serializers
from .models import Periodo, PlanillaTrabajador, PlanillaBeneficiario, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class PlanillaTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanillaTrabajador
        fields = '__all__'
        ref_name = 'PlanillaTrabajadorSerializerPlanillas'

class PlanillaBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanillaBeneficiario
        fields = '__all__'
        ref_name = 'PlanillaBeneficiarioSerializerPlanillas'

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
