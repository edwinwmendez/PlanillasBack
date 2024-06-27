from rest_framework.routers import DefaultRouter
from .views import (
    TrabajadorViewSet, CargoViewSet, RegimenLaboralViewSet, 
    TipoServidorViewSet, RegimenPensionarioViewSet, AFPViewSet, BancoViewSet, SituacionViewSet
)

router = DefaultRouter()
router.register(r'trabajadores', TrabajadorViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'regimenes-laborales', RegimenLaboralViewSet)
router.register(r'tipos-servidores', TipoServidorViewSet)
router.register(r'regimenes-pensionarios', RegimenPensionarioViewSet)
router.register(r'afps', AFPViewSet)
router.register(r'bancos', BancoViewSet)
router.register(r'situaciones', SituacionViewSet)

urlpatterns = router.urls
