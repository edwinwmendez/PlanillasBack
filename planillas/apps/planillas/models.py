# apps/planillas/models.py
from django.db import models
from apps.trabajadores.models import Trabajador
from apps.usuarios.models import Beneficiario
from apps.configuracion.models import Cargo, RegimenLaboral, TipoServidor, ClasePlanilla, FuenteFinanciamiento, Situacion, Periodo

from auditlog.registry import auditlog



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
    sueldo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Sueldo')
    dias_laborados = models.IntegerField(null=True, blank=True, verbose_name='Días Laborados', default=30)
    leyenda_permanente = models.CharField(max_length=255, blank=True, verbose_name='Leyenda Permanente')
    jornada_laboral = models.IntegerField(null=True, blank=True, verbose_name='Jornada Laboral', default=48)
    situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE, verbose_name='Situación')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.trabajador.persona.get_full_name()} - {self.cargo} - {self.fecha_ingreso} - {self.fecha_cese}'

    class Meta:
        db_table = 'contrato'
        ordering = ['id']
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        indexes = [
            models.Index(fields=['trabajador'], name='idx_contrato_trabajador'),
            models.Index(fields=['clase_planilla', 'fuente_financiamiento'], name='idx_contrato_clase_fuente'),
            models.Index(fields=['fecha_ingreso', 'fecha_cese'], name='idx_contrato_fechas'),
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class Planilla(models.Model):
    ESTADO_CHOICES = [
        ('APERTURADO', 'Aperturado'),
        ('CERRADO', 'Cerrado')
    ]

    correlativo = models.CharField(max_length=5, verbose_name='Correlativo')
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
        indexes = [
            models.Index(fields=['periodo', 'estado'], name='idx_planilla_periodo_estado'),
            models.Index(fields=['clase_planilla', 'fuente_financiamiento'], name='idx_planilla_clase_fuente'),
        ]

    def __str__(self):
        return f'{self.correlativo} - {self.clase_planilla} - {self.fuente_financiamiento} - {self.periodo} - {self.estado}'

class Boleta(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='boletas')
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='boletas')
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes')
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos')
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes')
    neto_a_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Neto a Pagar')
    numero_boleta = models.CharField(max_length=3, verbose_name='Número de Boleta', editable=False)
    visualizada = models.BooleanField(default=False, verbose_name='Visualizada', editable=False)
    fecha_visualizacion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Visualización', editable=False)
    descargada = models.BooleanField(default=False, verbose_name='Descargada', editable=False)
    fecha_descarga = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Descarga', editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Datos del contrato en el momento de la generación de la boleta
    centro_de_trabajo = models.CharField(max_length=255, blank=True, verbose_name='Centro de Trabajo')
    cargo = models.CharField(max_length=255, blank=True, verbose_name='Cargo')
    fecha_ingreso = models.DateField(null=True, blank=True, verbose_name='Fecha de Ingreso')
    fecha_cese = models.DateField(null=True, blank=True, verbose_name='Fecha de Cese')
    clase_planilla = models.CharField(max_length=255, blank=True, verbose_name='Clase de Planilla')
    fuente_financiamiento = models.CharField(max_length=255, blank=True, verbose_name='Fuente de Financiamiento')
    sueldo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Sueldo')
    dias_laborados = models.IntegerField(null=True, blank=True, verbose_name='Días Laborados', default=30)
    leyenda_permanente = models.CharField(max_length=255, blank=True, verbose_name='Leyenda Permanente')
    jornada_laboral = models.IntegerField(null=True, blank=True, verbose_name='Jornada Laboral', default=48)

    # Datos del trabajador en el momento de la generación de la boleta
    trabajador_nombres = models.CharField(max_length=255, verbose_name='Nombres del Trabajador')
    trabajador_apellidos = models.CharField(max_length=255, verbose_name='Apellidos del Trabajador')
    trabajador_dni = models.CharField(max_length=20, verbose_name='DNI del Trabajador')
    regimen_laboral = models.CharField(max_length=255, blank=True, verbose_name='Régimen Laboral')
    tipo_servidor = models.CharField(max_length=255, blank=True, verbose_name='Tipo de Servidor')
    regimen_pensionario = models.CharField(max_length=255, blank=True, verbose_name='Régimen Pensionario')
    banco = models.CharField(max_length=255, blank=True, verbose_name='Banco')
    cuenta_bancaria = models.CharField(max_length=255, blank=True, verbose_name='Cuenta Bancaria')

    # Totales calculados
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes', editable=False)
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos', editable=False)
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes', editable=False)
    neto_a_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Neto a Pagar', editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.contrato} - {self.planilla} - {self.planilla.periodo}'

    class Meta:
        db_table = 'boleta'
        ordering = ['planilla', 'contrato']
        unique_together = ('contrato', 'planilla')
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'
        indexes = [
            models.Index(fields=['contrato', 'planilla'], name='idx_boleta_contrato_planilla'),
            models.Index(fields=['visualizada', 'descargada'], name='idx_boleta_estado'),
        ]

class BoletaTransaccion(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=50, verbose_name='Tipo de Transacción')
    codigo = models.CharField(max_length=50, verbose_name='Código de Transacción')
    descripcion = models.CharField(max_length=255, verbose_name='Descripción de Transacción')
    monto = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Monto')

    class Meta:
        db_table = 'boleta_transacciones'
        verbose_name = 'Boleta Transacción'
        verbose_name_plural = 'Boleta Transacciones'


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


auditlog.register(Contrato)
auditlog.register(Planilla)
auditlog.register(Boleta)
auditlog.register(BoletaTransaccion)
auditlog.register(PlanillaBeneficiario)
