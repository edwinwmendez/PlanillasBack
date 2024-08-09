# apps/planillas/urls.py
from rest_framework.routers import DefaultRouter
from .views import PlanillaBeneficiarioViewSet,ContratoViewSet, PlanillaViewSet, BoletaViewSet, BoletaTransaccionViewSet

router = DefaultRouter()
router.register(r'contratos', ContratoViewSet)
router.register(r'planillas', PlanillaViewSet)
router.register(r'boletas', BoletaViewSet)

router.register(r'planillas-beneficiarios', PlanillaBeneficiarioViewSet)
router.register(r'boleta-transaccion', BoletaTransaccionViewSet)


urlpatterns = router.urls
