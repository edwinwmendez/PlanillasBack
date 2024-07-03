from django.db import models
from apps.planillas.models import Planilla

class ProcesosPlanilla(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    planillas = models.ManyToManyField(Planilla, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proceso de Planilla"
        verbose_name_plural = "Procesos de Planillas"