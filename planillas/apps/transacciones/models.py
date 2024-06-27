# apps/transacciones/models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Max
from django.utils.translation import gettext_lazy as _
from apps.trabajadores.models import Trabajador

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('HABER', 'Haber'),
        ('DESCUENTO', 'Descuento')
    ]
    CATEGORIA_CHOICES = [
        ('SUELDO', 'Sueldo'),
        ('BONIFICACION', 'Bonificación'),
        ('DEDUCCION', 'Deducción'),
        ('BENEFICIOS_SOCIALES', 'Beneficios Sociales'),
        ('APORTE', 'Aporte'),
        ('OTRO', 'Otro')
    ]

    tipo = models.CharField(
        max_length=10, choices=TIPO_CHOICES, verbose_name='Tipo', default='HABER'
    )
    categoria = models.CharField(
        max_length=20, choices=CATEGORIA_CHOICES, verbose_name='Categoría'
    )
    codigo = models.CharField(
        max_length=4, unique=True, verbose_name='Código', help_text='Código de Transacción'
    )
    descripcion = models.CharField(
        max_length=45, verbose_name='Descripción'
    )

    def clean(self):
        if self.tipo == 'HABER' and self.categoria not in ['SUELDO', 'BONIFICACION', 'BENEFICIOS_SOCIALES', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Haber.'))
        if self.tipo == 'DESCUENTO' and self.categoria not in ['DEDUCCION', 'APORTE', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Descuento.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'transaccion'
        ordering = ['descripcion']
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'


class TransaccionTrabajador(models.Model):
    trabajador = models.ForeignKey(
        Trabajador, on_delete=models.CASCADE, verbose_name='Trabajador', related_name='transacciones', null=True, blank=True
    )
    transaccion = models.ForeignKey(
        Transaccion, on_delete=models.CASCADE, verbose_name='Transacción'
    )
    monto = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto'
    )
    periodo_inicial = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Inicial'
    )
    periodo_final = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Final'
    )
    correlativo = models.IntegerField(
        verbose_name='Correlativo', editable=False, null=True, blank=True
    )
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return f'{self.correlativo} - {self.trabajador} - {self.transaccion.descripcion} - {self.monto}'

    class Meta:
        db_table = 'transacciones_trabajadores'
        verbose_name = 'Transacción del Trabajador'
        verbose_name_plural = 'Transacciones de los Trabajadores'
        ordering = ['transaccion', 'correlativo']

    def save(self, *args, **kwargs):
        if not self.pk:
            ultimo_correlativo = TransaccionTrabajador.objects.filter(transaccion=self.transaccion).aggregate(Max('correlativo'))['correlativo__max']
            self.correlativo = (ultimo_correlativo or 0) + 1
        super().save(*args, **kwargs)
