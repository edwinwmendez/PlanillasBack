# apps/reportes/urls.py
from rest_framework.routers import DefaultRouter
from .views import (
    ReporteRemuneracionActivosViewSet, ReportePlanillaBeneficiariosViewSet,
    ReporteTrabajadoresPorClasePlanillaViewSet, ReporteTrabajadoresPorFuenteFinanciamientoViewSet,
    ReporteTrabajadoresPorVinculoViewSet
)

router = DefaultRouter()
router.register(r'remuneracion-activos', ReporteRemuneracionActivosViewSet, basename='reporte-remuneracion-activos')
router.register(r'planilla-beneficiarios', ReportePlanillaBeneficiariosViewSet, basename='reporte-planilla-beneficiarios')
router.register(r'trabajadores-clase-planilla', ReporteTrabajadoresPorClasePlanillaViewSet, basename='reporte-trabajadores-clase-planilla')
router.register(r'trabajadores-fuente-financiamiento', ReporteTrabajadoresPorFuenteFinanciamientoViewSet, basename='reporte-trabajadores-fuente-financiamiento')
router.register(r'trabajadores-vinculo', ReporteTrabajadoresPorVinculoViewSet, basename='reporte-trabajadores-vinculo')

urlpatterns = router.urls
