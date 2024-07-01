# apps/planillas/models.py
from django.db import models
from apps.trabajadores.models import Trabajador
from apps.usuarios.models import Beneficiario
from apps.configuracion.models import Cargo, RegimenLaboral, TipoServidor, ClasePlanilla, FuenteFinanciamiento, Situacion, Periodo
from django.utils import timezone
from django.db.models import Sum



class Contrato(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='contratos')
    centro_de_trabajo = models.CharField(max_length=255, blank=True, verbose_name='Centro de Trabajo')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo')
    fecha_ingreso = models.DateField(null=True, blank=True, verbose_name='Fecha de Ingreso')
    fecha_cese = models.DateField(null=True, blank=True, verbose_name='Fecha de Cese')
    documento_contrato = models.CharField(max_length=45, blank=True, verbose_name='Documento de Contrato')
    documento_cese = models.CharField(max_length=45, blank=True, verbose_name='Documento de Cese')
    regimen_laboral = models.ForeignKey(RegimenLaboral, on_delete=models.CASCADE, verbose_name='Régimen Laboral')
    tipo_servidor = models.ForeignKey(TipoServidor, on_delete=models.CASCADE, verbose_name='Tipo de Servidor')
    clase_planilla = models.ForeignKey(ClasePlanilla, on_delete=models.CASCADE, verbose_name='Clase de Planilla')
    fuente_financiamiento = models.ForeignKey(FuenteFinanciamiento, on_delete=models.CASCADE, verbose_name='Fuente de Financiamiento')
    dias_laborados = models.IntegerField(null=True, blank=True, verbose_name='Días Laborados', default=30)
    leyenda_permanente = models.CharField(max_length=255, blank=True, verbose_name='Leyenda Permanente')
    jornada_laboral = models.IntegerField(null=True, blank=True, verbose_name='Jornada Laboral', default=48)
    situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE, verbose_name='Situación')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.trabajador} - {self.cargo} - {self.fecha_ingreso} - {self.fecha_cese}'

    class Meta:
        db_table = 'contrato'
        ordering = ['id']
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'



class Planilla(models.Model):
    ESTADO_CHOICES = [
        ('APERTURADO', 'Aperturado'),
        ('CERRADO', 'Cerrado')
    ]

    correlativo = models.CharField(max_length=10, verbose_name='Correlativo')
    clase_planilla = models.ForeignKey(ClasePlanilla, on_delete=models.CASCADE, verbose_name='Clase de Planilla')
    fuente_financiamiento = models.ForeignKey(FuenteFinanciamiento, on_delete=models.CASCADE, verbose_name='Fuente de Financiamiento')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name='Período')
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes')
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos')
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='APERTURADO', verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('correlativo', 'periodo')
        db_table = 'planilla'

    def __str__(self):
        return f'{self.correlativo} - {self.clase_planilla} - {self.fuente_financiamiento} - {self.periodo} - {self.estado}'

class Boleta(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='boletas')
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='boletas')
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes')
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos')
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes')
    neto_a_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Neto a Pagar')
    numero_boleta = models.CharField(max_length=5, verbose_name='Número de Boleta')
    visualizada = models.BooleanField(default=False, verbose_name='Visualizada')
    fecha_visualizacion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Visualización')
    descargada = models.BooleanField(default=False, verbose_name='Descargada')
    fecha_descarga = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Descarga')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def calcular_totales(self):
        transacciones = self.contrato.transacciones.filter(
            periodo_inicial__lte=self.planilla.periodo,
            periodo_final__gte=self.planilla.periodo,
            estado=True
        )
        self.total_haberes = transacciones.filter(transaccion__tipo_transaccion='HABER').aggregate(Sum('monto'))['monto__sum'] or 0
        self.total_descuentos = transacciones.filter(transaccion__tipo_transaccion='DESCUENTO').aggregate(Sum('monto'))['monto__sum'] or 0
        self.total_aportes = transacciones.filter(transaccion__tipo_transaccion='APORTE').aggregate(Sum('monto'))['monto__sum'] or 0
        self.neto_a_pagar = self.total_haberes - self.total_descuentos


    def save(self, *args, **kwargs):
        self.calcular_totales()
        super().save(*args, **kwargs)

    def marcar_como_visualizada(self):
        self.visualizada = True
        self.fecha_visualizacion = timezone.now()
        self.save()

    def marcar_como_descargada(self):
        self.descargada = True
        self.fecha_descarga = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.contrato} - {self.planilla} - {self.planilla.periodo}'

    class Meta:
        db_table = 'boleta'
        ordering = ['planilla', 'contrato']
        unique_together = ('contrato', 'planilla')
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'


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


