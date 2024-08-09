from django.shortcuts import render
from rest_framework import viewsets
from .models import Ugel, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Periodo, Transaccion, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion, TipoDocumento, Sexo, TipoDescuento, TipoBeneficiario, EstadoCivil, ComisionAfp, ConfiguracionGlobal, ValorConfiguracionGlobal
from .serializers import UgelSerializer, TipoPlanillaSerializer, ClasePlanillaSerializer, FuenteFinanciamientoSerializer, PeriodoSerializer, TransaccionSerializer, CargoSerializer, RegimenLaboralSerializer, TipoServidorSerializer, RegimenPensionarioSerializer, AfpSerializer, BancoSerializer, SituacionSerializer, TipoDocumentoSerializer, SexoSerializer, TipoDescuentoSerializer, TipoBeneficiarioSerializer, EstadoCivilSerializer, ComisionAfpSerializer, ConfiguracionGlobalSerializer, ValorConfiguracionGlobalSerializer
from rest_framework.permissions import IsAuthenticated

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Create your views here.
class UgelViewSet(viewsets.ModelViewSet):
    queryset = Ugel.objects.all()
    serializer_class = UgelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin_sistema':
            return self.queryset
        return self.queryset.filter(id=user.ugel.id)

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by('-periodo')

class TipoPlanillaViewSet(viewsets.ModelViewSet):
    queryset = TipoPlanilla.objects.all()
    serializer_class = TipoPlanillaSerializer
    permission_classes = [IsAuthenticated]

class ClasePlanillaViewSet(viewsets.ModelViewSet):
    queryset = ClasePlanilla.objects.all()
    serializer_class = ClasePlanillaSerializer
    permission_classes = [IsAuthenticated]

class FuenteFinanciamientoViewSet(viewsets.ModelViewSet):
    queryset = FuenteFinanciamiento.objects.all()
    serializer_class = FuenteFinanciamientoSerializer
    permission_classes = [IsAuthenticated]

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    permission_classes = [IsAuthenticated]

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]

class RegimenLaboralViewSet(viewsets.ModelViewSet):
    queryset = RegimenLaboral.objects.all()
    serializer_class = RegimenLaboralSerializer
    permission_classes = [IsAuthenticated]

class TipoServidorViewSet(viewsets.ModelViewSet):
    queryset = TipoServidor.objects.all()
    serializer_class = TipoServidorSerializer
    permission_classes = [IsAuthenticated]

class RegimenPensionarioViewSet(viewsets.ModelViewSet):
    queryset = RegimenPensionario.objects.all()
    serializer_class = RegimenPensionarioSerializer
    permission_classes = [IsAuthenticated]

class AFPViewSet(viewsets.ModelViewSet):
    queryset = Afp.objects.all()
    serializer_class = AfpSerializer
    permission_classes = [IsAuthenticated]

class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    permission_classes = [IsAuthenticated]

class SituacionViewSet(viewsets.ModelViewSet):
    queryset = Situacion.objects.all()
    serializer_class = SituacionSerializer
    permission_classes = [IsAuthenticated]

class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    serializer_class = SexoSerializer
    permission_classes = [IsAuthenticated]

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    permission_classes = [IsAuthenticated]

class TipoDescuentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDescuento.objects.all()
    serializer_class = TipoDescuentoSerializer
    permission_classes = [IsAuthenticated]

class TipoBeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = TipoBeneficiario.objects.all()
    serializer_class = TipoBeneficiarioSerializer
    permission_classes = [IsAuthenticated]

class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer
    permission_classes = [IsAuthenticated]

class ComisionAfpViewSet(viewsets.ModelViewSet):
    queryset = ComisionAfp.objects.all()
    serializer_class = ComisionAfpSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.select_related('periodo', 'afp').order_by('-periodo__periodo', 'afp__nombre_afp')

class ConfiguracionGlobalViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracionGlobal.objects.all()
    serializer_class = ConfiguracionGlobalSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 15))  # Cache por 15 minutos
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.order_by('clave')

class ValorConfiguracionGlobalViewSet(viewsets.ModelViewSet):
    queryset = ValorConfiguracionGlobal.objects.all()
    serializer_class = ValorConfiguracionGlobalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.select_related('configuracion').order_by('configuracion__clave', '-fecha_inicio', '-fecha_fin')