# apps/planillas/urls.py
from rest_framework.routers import DefaultRouter
from .views import (
    PeriodoViewSet, PlanillaTrabajadorViewSet, PlanillaBeneficiarioViewSet,
    TipoPlanillaViewSet, ClasePlanillaViewSet, FuenteFinanciamientoViewSet
)

router = DefaultRouter()
router.register(r'periodos', PeriodoViewSet)
router.register(r'planillas-trabajadores', PlanillaTrabajadorViewSet)
router.register(r'planillas-beneficiarios', PlanillaBeneficiarioViewSet)
router.register(r'tipos-planilla', TipoPlanillaViewSet)
router.register(r'clases-planilla', ClasePlanillaViewSet)
router.register(r'fuentes-financiamiento', FuenteFinanciamientoViewSet)

urlpatterns = router.urls
