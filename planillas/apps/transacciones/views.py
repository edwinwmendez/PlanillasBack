# apps/transacciones/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Transaccion, TransaccionTrabajador
from .serializers import TransaccionSerializer, TransaccionTrabajadorSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    permission_classes = [IsAuthenticated]

class TransaccionTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = TransaccionTrabajador.objects.all()
    serializer_class = TransaccionTrabajadorSerializer
    permission_classes = [IsAuthenticated]
