# apps/transacciones/urls.py
from rest_framework.routers import DefaultRouter
from .views import  TransaccionTrabajadorViewSet

router = DefaultRouter()
router.register(r'transacciones-trabajadores', TransaccionTrabajadorViewSet)

urlpatterns = router.urls
