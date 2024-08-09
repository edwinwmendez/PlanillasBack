# apps/transacciones/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TransaccionContrato
from .serializers import TransaccionTrabajadorSerializer

class TransaccionTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = TransaccionContrato.objects.all()
    serializer_class = TransaccionTrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = TransaccionContrato.objects.select_related(
            'contrato', 'transaccion', 'contrato__trabajador', 'contrato__trabajador__persona'
        )
        
        if user.role != 'admin_sistema':
            queryset = queryset.filter(contrato__trabajador__ugel=user.ugel)
        
        return queryset.distinct()