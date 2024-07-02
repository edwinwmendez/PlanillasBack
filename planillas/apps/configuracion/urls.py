# apps/configuracion/urls.py
from rest_framework.routers import DefaultRouter
from .views import UgelViewSet, TipoPlanillaViewSet, ClasePlanillaViewSet, FuenteFinanciamientoViewSet, PeriodoViewSet, TransaccionViewSet, CargoViewSet, RegimenLaboralViewSet, TipoServidorViewSet, RegimenPensionarioViewSet, AFPViewSet, BancoViewSet, SituacionViewSet, TipoDocumentoViewSet, SexoViewSet, TipoDescuentoViewSet, TipoBeneficiarioViewSet, EstadoCivilViewSet

router = DefaultRouter()
router.register(r'ugels', UgelViewSet)
router.register(r'periodos', PeriodoViewSet)
router.register(r'transacciones', TransaccionViewSet)
router.register(r'tipos-planilla', TipoPlanillaViewSet)
router.register(r'clases-planilla', ClasePlanillaViewSet)
router.register(r'fuentes-financiamiento', FuenteFinanciamientoViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'regimenes-laborales', RegimenLaboralViewSet)
router.register(r'tipos-documento', TipoDocumentoViewSet)
router.register(r'tipos-servidores', TipoServidorViewSet)
router.register(r'regimenes-pensionarios', RegimenPensionarioViewSet)
router.register(r'afps', AFPViewSet)
router.register(r'bancos', BancoViewSet)
router.register(r'situaciones', SituacionViewSet)
router.register(r'sexos', SexoViewSet)
router.register(r'estados-civiles', EstadoCivilViewSet)
router.register(r'tipos-descuento', TipoDescuentoViewSet)
router.register(r'tipos-beneficiario', TipoBeneficiarioViewSet)


urlpatterns = router.urls
