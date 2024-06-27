# apps/auditoria/urls.py
from rest_framework.routers import DefaultRouter
from .views import AuditoriaViewSet

router = DefaultRouter()
router.register(r'auditorias', AuditoriaViewSet)

urlpatterns = router.urls
