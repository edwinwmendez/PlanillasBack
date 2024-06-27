# apps/planillas/models.py
from django.db import models
from django.core.exceptions import ValidationError
from apps.trabajadores.models import Trabajador, Ugel
from apps.usuarios.models import Beneficiario

class Periodo(models.Model):
    mes = models.CharField(max_length=2, blank=True, verbose_name='Mes')
    anio = models.CharField(max_length=4, blank=True, verbose_name='Año')
    periodo = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo', editable=False)
    es_adicional = models.BooleanField(
        default=False, verbose_name='¿Es adicional?')
    periodo_actual = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Actual', editable=False, null=True, default=None)

    def __str__(self):
        return f'{self.periodo} - {self.mes}/{self.anio}'

    def clean(self):
        if not self.periodo:
            self.periodo = f'{self.anio}{self.mes}'
        if not self.es_adicional and Periodo.objects.filter(mes=self.mes, anio=self.anio, es_adicional=False).exists():
            raise ValidationError('Ya existe un período principal para este mes y año.')

    def save(self, *args, **kwargs):
        self.clean()
        if not self.periodo:
            self.periodo = f'{self.anio}{self.mes}'

        if not self.es_adicional:
            last_principal_periodo = Periodo.objects.filter(
                es_adicional=False).order_by('-id').first()
            self.periodo_actual = last_principal_periodo.periodo if last_principal_periodo else None

        if not self.es_adicional and Periodo.objects.filter(mes=self.mes, anio=self.anio, es_adicional=False).exists():
            raise ValidationError('Ya existe un período principal para este mes y año.')

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'periodo'
        ordering = ['anio', 'mes']
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'


class PlanillaTrabajador(models.Model):
    total_haberes = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total de Haberes'
    )
    total_descuentos = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total de Descuentos'
    )
    essalud = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='ESSALUD'
    )
    emitio_boleta = models.SmallIntegerField(
        null=True, blank=True, verbose_name='Emisión de Boleta')
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, verbose_name='Trabajador', related_name='remuneraciones', null=True, blank=True)
    tipo_planilla = models.ForeignKey(
        'planillas.TipoPlanilla', on_delete=models.CASCADE, verbose_name='Tipo de Planilla')
    periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, verbose_name='Período')
    ugel = models.ForeignKey(
        Ugel, on_delete=models.CASCADE, verbose_name='UGEL')

    def __str__(self):
        return f'{self.trabajador.persona.nombres} {self.trabajador.persona.paterno} {self.trabajador.persona.materno} - {self.periodo}'

    class Meta:
        db_table = 'planilla_trabajador'
        ordering = ['id']
        verbose_name = 'Planilla del Trabajador'
        verbose_name_plural = 'Planillas de los Trabajadores'


class PlanillaBeneficiario(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name='Beneficiario')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name='Período')
    monto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto')

    def __str__(self):
        return f'{self.beneficiario.persona.nombres} {self.beneficiario.persona.paterno} {self.beneficiario.persona.materno} - {self.periodo}'

    class Meta:
        db_table = 'planilla_beneficiario'
        ordering = ['id']
        verbose_name = 'Planilla del Beneficiario'
        verbose_name_plural = 'Planillas de los Beneficiarios'


class TipoPlanilla(models.Model):
    nombre_tipo_planilla = models.CharField(
        max_length=45, blank=True, verbose_name='Nombre de Tipo de Planilla')
    codigo_tipo_planilla = models.CharField(max_length=2, blank=True, verbose_name='Código de Tipo de Planilla')

    def __str__(self):
        return self.nombre_tipo_planilla

    class Meta:
        db_table = 'tipo_planilla'
        ordering = ['nombre_tipo_planilla']
        verbose_name = 'Tipo de Planilla'
        verbose_name_plural = 'Tipos de Planilla'


class ClasePlanilla(models.Model):
    nombre_clase_planilla = models.CharField(
        max_length=45, blank=True, verbose_name='Nombre de Clase de Planilla')
    codigo_clase_planilla = models.CharField(max_length=2, blank=True, verbose_name='Código de Clase de Planilla')
    tipo_planilla = models.ForeignKey(
        TipoPlanilla, on_delete=models.CASCADE, verbose_name='Tipo de Planilla', null=True, blank=True)

    def __str__(self):
        return self.nombre_clase_planilla

    class Meta:
        db_table = 'clase_planilla'
        ordering = ['nombre_clase_planilla']
        verbose_name = 'Clase de Planilla'
        verbose_name_plural = 'Clases de Planilla'


class FuenteFinanciamiento(models.Model):
    nombre_fuente_financiamiento = models.CharField(
        max_length=45, blank=True, verbose_name='Nombre de Fuente de Financiamiento')
    tipo_planilla = models.ForeignKey(
        ClasePlanilla, on_delete=models.CASCADE, verbose_name='Clase de Planilla', null=True, blank=True)

    def __str__(self):
        return self.nombre_fuente_financiamiento

    class Meta:
        db_table = 'fuente_financiamiento'
        ordering = ['nombre_fuente_financiamiento']
        verbose_name = 'Fuente de Financiamiento'
        verbose_name_plural = 'Fuentes de Financiamiento'
