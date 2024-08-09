# apps/auditoria/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Auditoria
from .serializers import AuditoriaSerializer

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('persona').order_by('-fecha')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(persona__user__ugel=user.ugel)
        return queryset