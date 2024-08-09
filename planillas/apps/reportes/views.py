# apps/reportes/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TrabajadorSerializer, PlanillaBeneficiarioSerializer
from apps.trabajadores.models import Trabajador
from apps.planillas.models import PlanillaBeneficiario, Contrato

class ReporteRemuneracionActivosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        
        user = self.request.user
        queryset = Trabajador.objects.filter(contratos__situacion__codigo='HAB')\
            .select_related('persona', 'ugel', 'regimen_pensionario', 'afp')\
            .prefetch_related('contratos', 'contratos__transacciones')
        
        if user.role != 'admin_sistema':
            queryset = queryset.filter(ugel=user.ugel)
        
        return queryset.distinct()

class ReportePlanillaBeneficiariosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlanillaBeneficiarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return PlanillaBeneficiario.objects.none()
        return PlanillaBeneficiario.objects.all()

class ReporteTrabajadoresPorClasePlanillaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        clase_planilla = self.request.query_params.get('clase_planilla')
        if clase_planilla:
            return Trabajador.objects.filter(contratos__clase_planilla__nombre_clase_planilla=clase_planilla).distinct()
        return Trabajador.objects.none()

class ReporteTrabajadoresPorFuenteFinanciamientoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        fuente_financiamiento = self.request.query_params.get('fuente_financiamiento')
        if fuente_financiamiento:
            return Trabajador.objects.filter(contratos__fuente_financiamiento__nombre_fuente_financiamiento=fuente_financiamiento).distinct()
        return Trabajador.objects.none()

class ReporteTrabajadoresPorVinculoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        dias_restantes = self.request.query_params.get('dias_restantes')
        if dias_restantes is not None:
            try:
                dias_restantes = int(dias_restantes)
                return Trabajador.objects.filter(contratos__dias_laborados__lte=dias_restantes).distinct()
            except ValueError:
                pass
        return Trabajador.objects.none()
