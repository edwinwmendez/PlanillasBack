# apps/usuarios/urls.py
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, BeneficiarioViewSet, UgelViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'beneficiarios', BeneficiarioViewSet)
router.register(r'ugels', UgelViewSet)

urlpatterns = router.urls
