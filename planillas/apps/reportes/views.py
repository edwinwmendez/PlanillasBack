# apps/reportes/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from apps.trabajadores.models import Trabajador
from apps.planillas.models import PlanillaTrabajador, PlanillaBeneficiario
from .serializers import TrabajadorSerializer, PlanillaTrabajadorSerializer, PlanillaBeneficiarioSerializer

class ReporteRemuneracionActivosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer

    def get_queryset(self):
        return Trabajador.objects.filter(situacion='HAB')

class ReportePlanillaBeneficiariosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlanillaBeneficiarioSerializer

    def get_queryset(self):
        return PlanillaBeneficiario.objects.all()

class ReporteTrabajadoresPorClasePlanillaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer

    def get_queryset(self):
        clase_planilla = self.request.query_params.get('clase_planilla')
        return Trabajador.objects.filter(cargo__clase_planilla=clase_planilla)

class ReporteTrabajadoresPorFuenteFinanciamientoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer

    def get_queryset(self):
        fuente_financiamiento = self.request.query_params.get('fuente_financiamiento')
        return Trabajador.objects.filter(cargo__fuente_financiamiento=fuente_financiamiento)

class ReporteTrabajadoresPorVinculoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer

    def get_queryset(self):
        dias_restantes = self.request.query_params.get('dias_restantes')
        return Trabajador.objects.filter(dias_laborados__lte=dias_restantes)
