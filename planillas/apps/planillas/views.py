# apps/planillas/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Periodo, PlanillaTrabajador, PlanillaBeneficiario, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento
from .serializers import PeriodoSerializer, PlanillaTrabajadorSerializer, PlanillaBeneficiarioSerializer, TipoPlanillaSerializer, ClasePlanillaSerializer, FuenteFinanciamientoSerializer

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    permission_classes = [IsAuthenticated]

class PlanillaTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = PlanillaTrabajador.objects.all()
    serializer_class = PlanillaTrabajadorSerializer
    permission_classes = [IsAuthenticated]

class PlanillaBeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = PlanillaBeneficiario.objects.all()
    serializer_class = PlanillaBeneficiarioSerializer
    permission_classes = [IsAuthenticated]

class TipoPlanillaViewSet(viewsets.ModelViewSet):
    queryset = TipoPlanilla.objects.all()
    serializer_class = TipoPlanillaSerializer
    permission_classes = [IsAuthenticated]

class ClasePlanillaViewSet(viewsets.ModelViewSet):
    queryset = ClasePlanilla.objects.all()
    serializer_class = ClasePlanillaSerializer
    permission_classes = [IsAuthenticated]

class FuenteFinanciamientoViewSet(viewsets.ModelViewSet):
    queryset = FuenteFinanciamiento.objects.all()
    serializer_class = FuenteFinanciamientoSerializer
    permission_classes = [IsAuthenticated]
