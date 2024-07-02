# apps/planillas/models.py
from django.db import models
from apps.trabajadores.models import Trabajador
from apps.usuarios.models import Beneficiario
from apps.configuracion.models import Cargo, RegimenLaboral, TipoServidor, ClasePlanilla, FuenteFinanciamiento, Situacion, Periodo
from django.utils import timezone
from django.db.models import Sum, Max



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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.registrar_transacciones()

    def registrar_transacciones(self):
        from apps.transacciones.models import TransaccionTrabajador
        from apps.configuracion.models import Transaccion

        if self.clase_planilla.codigo_clase_planilla == '03':  # CAS
            transaccion = Transaccion.objects.get(id=1)  # Remuneracion CAS
            periodo_inicial = self.fecha_ingreso.strftime('%Y%m')
            periodo_final = self.fecha_cese.strftime('%Y%m')

             # Calcular la remuneración proporcional a los días trabajados
            sueldo_proporcional = (self.sueldo / 30) * self.dias_laborados

            # Verificar si ya existe una transacción activa que cubra el período actual
            existe_transaccion_activa = TransaccionTrabajador.objects.filter(
                contrato=self,
                transaccion=transaccion,
                estado=True,
                periodo_inicial__lte=periodo_final,
                periodo_final__gte=periodo_inicial
            ).exists()

            if not existe_transaccion_activa:
                TransaccionTrabajador.objects.create(
                    contrato=self,
                    transaccion=transaccion,
                    monto=sueldo_proporcional,
                    periodo_inicial=periodo_inicial,
                    periodo_final=periodo_final,
                    estado=True
                )


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
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes', editable=False)
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos', editable=False)
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes', editable=False)
    neto_a_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Neto a Pagar', editable=False)
    numero_boleta = models.CharField(max_length=3, verbose_name='Número de Boleta', editable=False)
    visualizada = models.BooleanField(default=False, verbose_name='Visualizada', editable=False)
    fecha_visualizacion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Visualización', editable=False)
    descargada = models.BooleanField(default=False, verbose_name='Descargada', editable=False)
    fecha_descarga = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Descarga', editable=False)
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

    def generar_numero_boleta(self):
        # Obtener el número de boleta más alto del período actual
        max_numero_boleta = Boleta.objects.filter(planilla=self.planilla).aggregate(Max('numero_boleta'))['numero_boleta__max']
        if max_numero_boleta:
            # Incrementar el número de boleta
            self.numero_boleta = str(int(max_numero_boleta) + 1).zfill(3)
        else:
            # Si no hay boletas en el período, comenzar con '001'
            self.numero_boleta = '001'

    def save(self, *args, **kwargs):
        if not self.numero_boleta:
            self.generar_numero_boleta()
        self.calcular_totales()
        super().save(*args, **kwargs)
        self.actualizar_totales_planilla()

    def actualizar_totales_planilla(self):
        self.planilla.total_haberes = Boleta.objects.filter(planilla=self.planilla).aggregate(Sum('total_haberes'))['total_haberes__sum'] or 0
        self.planilla.total_descuentos = Boleta.objects.filter(planilla=self.planilla).aggregate(Sum('total_descuentos'))['total_descuentos__sum'] or 0
        self.planilla.total_aportes = Boleta.objects.filter(planilla=self.planilla).aggregate(Sum('total_aportes'))['total_aportes__sum'] or 0
        self.planilla.save()

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


