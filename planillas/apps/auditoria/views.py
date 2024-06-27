# apps/auditoria/views.py
from rest_framework import viewsets
from .models import Auditoria
from .serializers import AuditoriaSerializer

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
