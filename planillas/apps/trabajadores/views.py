# apps/trabajadores/views.py
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Trabajador
from .serializers import TrabajadorSerializer

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Trabajador.objects.select_related('persona', 'ugel', 'regimen_pensionario', 'afp', 'banco')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(ugel=user.ugel)
        return queryset
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El trabajador ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )
