# apps/transacciones/models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Max
from apps.planillas.models import Contrato
from apps.configuracion.models import Transaccion
class TransaccionContrato(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, verbose_name='Contrato', related_name='transacciones')
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, verbose_name='Transacción')
    monto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto')
    periodo_inicial = models.CharField(max_length=6, blank=True, verbose_name='Periodo Inicial')
    periodo_final = models.CharField(max_length=6, blank=True, verbose_name='Periodo Final')
    correlativo = models.IntegerField(verbose_name='Correlativo', editable=False, null=True, blank=True)
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return f'{self.correlativo} - {self.contrato} - {self.monto}'

    class Meta:
        db_table = 'transacciones_trabajadores'
        verbose_name = 'Transacción del Trabajador'
        verbose_name_plural = 'Transacciones de los Trabajadores'
        ordering = ['transaccion', 'correlativo']

    def save(self, *args, **kwargs):
        if not self.pk:
            ultimo_correlativo = TransaccionContrato.objects.filter(transaccion=self.transaccion).aggregate(Max('correlativo'))['correlativo__max']
            self.correlativo = (ultimo_correlativo or 0) + 1
        super().save(*args, **kwargs)
