# apps/transacciones/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TransaccionContrato
from .serializers import TransaccionTrabajadorSerializer

class TransaccionTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = TransaccionContrato.objects.all()
    serializer_class = TransaccionTrabajadorSerializer
    permission_classes = [IsAuthenticated]
