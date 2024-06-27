# apps/auditoria/models.py
from django.db import models
from apps.usuarios.models import Persona

class Auditoria(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    descripcion = models.TextField(verbose_name='Descripción')
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona'
    )
    ip_address = models.GenericIPAddressField(
        null=True, blank=True, verbose_name='Dirección IP'
    )
    user_agent = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='User Agent'
    )
    accion = models.CharField(
        max_length=50, verbose_name='Acción'
    )

    class Meta:
        db_table = 'auditoria'
        ordering = ['-fecha']
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
