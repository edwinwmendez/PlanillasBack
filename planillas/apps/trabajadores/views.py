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
        if user.role == 'admin_sistema':
            return Trabajador.objects.all()
        return Trabajador.objects.filter(ugel=user.ugel)

