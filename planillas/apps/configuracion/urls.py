# apps/configuracion/urls.py
from rest_framework.routers import DefaultRouter
from .views import UgelViewSet, TipoPlanillaViewSet, ClasePlanillaViewSet, FuenteFinanciamientoViewSet, PeriodoViewSet, TransaccionViewSet, CargoViewSet, RegimenLaboralViewSet, TipoServidorViewSet, RegimenPensionarioViewSet, AFPViewSet, BancoViewSet, SituacionViewSet

router = DefaultRouter()
router.register(r'ugels', UgelViewSet)
router.register(r'periodos', PeriodoViewSet)
router.register(r'transacciones', TransaccionViewSet)
router.register(r'tipos-planilla', TipoPlanillaViewSet)
router.register(r'clases-planilla', ClasePlanillaViewSet)
router.register(r'fuentes-financiamiento', FuenteFinanciamientoViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'regimenes-laborales', RegimenLaboralViewSet)
router.register(r'tipos-servidores', TipoServidorViewSet)
router.register(r'regimenes-pensionarios', RegimenPensionarioViewSet)
router.register(r'afps', AFPViewSet)
router.register(r'bancos', BancoViewSet)
router.register(r'situaciones', SituacionViewSet)


urlpatterns = router.urls
