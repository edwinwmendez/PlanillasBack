# apps/usuarios/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Persona, Beneficiario, User
from .serializers import PersonaSerializer, BeneficiarioSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated]

class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    permission_classes = [IsAuthenticated]
