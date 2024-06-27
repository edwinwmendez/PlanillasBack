# apps/usuarios/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Persona, Beneficiario, Ugel
from .serializers import PersonaSerializer, BeneficiarioSerializer, UgelSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated]

class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    permission_classes = [IsAuthenticated]

class UgelViewSet(viewsets.ModelViewSet):
    queryset = Ugel.objects.all()
    serializer_class = UgelSerializer
    permission_classes = [IsAuthenticated]
