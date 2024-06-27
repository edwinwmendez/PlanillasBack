from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Trabajador, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion
from .serializers import (
    TrabajadorSerializer, CargoSerializer, RegimenLaboralSerializer,
    TipoServidorSerializer, RegimenPensionarioSerializer, AFPSerializer, BancoSerializer, SituacionSerializer
)

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
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