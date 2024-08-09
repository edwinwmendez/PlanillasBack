# apps/usuarios/urls.py
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, BeneficiarioViewSet, UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'beneficiarios', BeneficiarioViewSet)



urlpatterns = router.urls
