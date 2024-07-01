from django.shortcuts import render
from rest_framework import viewsets
from .models import Ugel, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Periodo, Transaccion, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion, TipoDocumento, Sexo
from .serializers import UgelSerializer, TipoPlanillaSerializer, ClasePlanillaSerializer, FuenteFinanciamientoSerializer, PeriodoSerializer, TransaccionSerializer, CargoSerializer, RegimenLaboralSerializer, TipoServidorSerializer, RegimenPensionarioSerializer, AFPSerializer, BancoSerializer, SituacionSerializer, TipoDocumentoSerializer, SexoSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UgelViewSet(viewsets.ModelViewSet):
    queryset = Ugel.objects.all()
    serializer_class = UgelSerializer
    permission_classes = [IsAuthenticated]

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    permission_classes = [IsAuthenticated]

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
    serializer_class = AFPSerializer
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