# apps/trabajadores/models.py
from django.db import models
from apps.usuarios.models import Persona
from auditlog.registry import auditlog

class Trabajador(models.Model):
    ugel = models.ForeignKey('configuracion.Ugel', on_delete=models.CASCADE, verbose_name='UGEL')
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    #persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    tiempo_servicios = models.IntegerField(null=True, blank=True, verbose_name='Tiempo de Servicios')
    regimen_pensionario = models.ForeignKey('configuracion.RegimenPensionario', on_delete=models.CASCADE, verbose_name='Régimen Pensionario')
    afp = models.ForeignKey('configuracion.Afp', on_delete=models.CASCADE, verbose_name='AFP')
    cuspp = models.CharField(max_length=12, blank=True, verbose_name='CUSPP')
    fecha_afiliacion = models.DateField(null=True, blank=True, verbose_name='Fecha de Afiliación')
    banco = models.ForeignKey('configuracion.Banco', on_delete=models.CASCADE, verbose_name='Banco')
    numero_cuenta = models.CharField(max_length=45, blank=True, verbose_name='Número de Cuenta')
    ruc = models.CharField(max_length=11, blank=True, verbose_name='RUC')
    estado = models.BooleanField(verbose_name='Estado', default=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.apellido_paterno} {self.persona.apellido_materno}'

    class Meta:
        db_table = 'trabajador'
        ordering = ['id']
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        indexes = [
            models.Index(fields=['persona'], name='idx_trabajador_persona'),
            models.Index(fields=['ugel'], name='idx_trabajador_ugel'),
            models.Index(fields=['estado'], name='idx_trabajador_estado'),
        ]

auditlog.register(Trabajador)