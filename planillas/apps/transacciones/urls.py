# apps/transacciones/urls.py
from rest_framework.routers import DefaultRouter
from .views import TransaccionViewSet, TransaccionTrabajadorViewSet

router = DefaultRouter()
router.register(r'transacciones', TransaccionViewSet)
router.register(r'transacciones-trabajadores', TransaccionTrabajadorViewSet)

urlpatterns = router.urls
