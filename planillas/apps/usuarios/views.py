# apps/usuarios/views.py
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Persona, Beneficiario, User
from .serializers import PersonaSerializer, BeneficiarioSerializer, UserSerializer

import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.tokens import RefreshToken

# apps/usuarios/views.py

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

from rest_framework.decorators import action

# Vista personalizada para el login
class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Obtener el nombre de usuario y la contraseña del request
        username = request.data.get("username")
        password = request.data.get("password")

        # Autenticar al usuario
        user = authenticate(username=username, password=password)
        if user is not None:
            # Crear tokens de acceso y refresco para el usuario autenticado
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),  # Token de refresco
                'access': str(refresh.access_token),  # Token de acceso
            }, status=status.HTTP_200_OK)
        # Retornar un error si las credenciales no son válidas
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Vista personalizada para obtener detalles del usuario autenticado
class CustomUserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Serializar y retornar los datos del usuario autenticado
        serializer = UserSerializer(request.user)
        return Response(serializer.data)




class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Sesión cerrada exitosamente"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('ugel')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(ugel=user.ugel)
        return queryset
    

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('tipo_documento', 'sexo', 'estado_civil')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(user__ugel=user.ugel)
        return queryset
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "Persona ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'], url_path='buscar')
    def buscar_por_documento(self, request):
        numero_documento = request.query_params.get('documento')
        if not numero_documento:
            return Response({"error": "El número de documento es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            persona = Persona.objects.get(numero_documento=numero_documento)
            serializer = self.get_serializer(persona)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response({"error": "Persona no encontrada."}, status=status.HTTP_404_NOT_FOUND)

class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('trabajador', 'persona', 'tipo_beneficiario', 'tipo_descuento', 'banco')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(trabajador__ugel=user.ugel)
        return queryset
    
    

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Esta vista requiere autenticación

    def get(self, request):
        # Devolvemos información del usuario autenticado
        return Response({
            "message": "Esta es una vista protegida",
            "user": request.user.username
        })
