# apps/trabajadores/models.py
from django.db import models
from apps.usuarios.models import Persona, Ugel

class Trabajador(models.Model):
    SITUACION_CHOICES = [
        ('HAB', 'Habilitado'),
        ('LSG', 'Licencia sin goce'),
        ('LCG', 'Licencia con goce'),
        ('DES', 'Desabilitado'),
        ('VAC', 'Vacaciones')
    ]
    ugel = models.ForeignKey(
        Ugel, on_delete=models.CASCADE, verbose_name='UGEL')
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    situacion = models.CharField(
        max_length=20, null=True, default='HAB', choices=SITUACION_CHOICES,
        verbose_name='Situación'
    )
    dias_licencia = models.IntegerField(
        null=True, blank=True, verbose_name='Días de Licencia', default=0)
    fecha_ini_licencia = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Inicio de Licencia')
    tiempo_servicios = models.CharField(
        max_length=6, blank=True, verbose_name='Tiempo de Servicios')
    dias_laborados = models.IntegerField(
        null=True, blank=True, verbose_name='Días Laborados', default=30)
    cargo = models.ForeignKey(
        'trabajadores.Cargo', on_delete=models.CASCADE, verbose_name='Cargo', related_name='empleados')
    fecha_ingreso = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Ingreso')
    fecha_cese = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Cese')
    documento_contrato = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Contrato')
    documento_cese = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Cese')
    regimen_laboral = models.ForeignKey(
        'trabajadores.RegimenLaboral', on_delete=models.CASCADE, verbose_name='Régimen Laboral'
    )
    tipo_servidor = models.ForeignKey(
        'trabajadores.TipoServidor', on_delete=models.CASCADE, verbose_name='Tipo de Servidor')
    regimen_pensionario = models.ForeignKey(
        'trabajadores.RegimenPensionario', on_delete=models.CASCADE, verbose_name='Régimen Pensionario'
    )
    afp = models.ForeignKey('trabajadores.AFP', on_delete=models.CASCADE, verbose_name='AFP')
    cuspp = models.CharField(max_length=12, blank=True, verbose_name='CUSPP')
    fecha_afiliacion = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Afiliación')
    fecha_devengue = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Devengue')
    codigo_nexus = models.CharField(
        max_length=10, blank=True, verbose_name='Código Nexus')
    jornada_laboral = models.IntegerField(
        null=True, blank=True, verbose_name='Jornada Laboral')
    descuentos_dias = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Días', default=0)
    descuentos_horas = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Horas', default=0)
    descuentos_minutos = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Minutos', default=0)
    leyenda_permanente = models.CharField(
        max_length=45, blank=True, verbose_name='Leyenda Permanente')
    leyenda_mensual = models.CharField(
        max_length=45, blank=True, verbose_name='Leyenda Mensual')
    banco = models.ForeignKey(
        'trabajadores.Banco', on_delete=models.CASCADE, verbose_name='Banco')
    numero_cuenta = models.CharField(
        max_length=45, blank=True, verbose_name='Número de Cuenta')
    ruc = models.CharField(max_length=11, blank=True, verbose_name='RUC')

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno} - {self.cargo.nombre_cargo} - {self.fecha_ingreso} - {self.fecha_cese}'

    class Meta:
        db_table = 'empleado'
        ordering = ['id']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        indexes = [
            models.Index(fields=['situacion'], name='situacion_idx'),
            models.Index(fields=['fecha_ingreso'], name='fecha_ingreso_idx'),
            models.Index(fields=['fecha_cese'], name='fecha_cese_idx'),
        ]

class Cargo(models.Model):
    nombre_cargo = models.CharField(
        max_length=45, verbose_name='Nombre de Cargo')

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'cargo'
        ordering = ['nombre_cargo']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class RegimenLaboral(models.Model):
    nombre_regimen_laboral = models.CharField(
        max_length=45, verbose_name='Nombre de Régimen Laboral')

    def __str__(self):
        return self.nombre_regimen_laboral

    class Meta:
        db_table = 'regimen_laboral'
        ordering = ['nombre_regimen_laboral']
        verbose_name = 'Régimen Laboral'
        verbose_name_plural = 'Regímenes Laborales'


class TipoServidor(models.Model):
    nombre_tipo_servidor = models.CharField(
        max_length=45, verbose_name='Nombre de Tipo de Servidor')

    def __str__(self):
        return self.nombre_tipo_servidor

    class Meta:
        db_table = 'tipo_servidor'
        ordering = ['nombre_tipo_servidor']
        verbose_name = 'Tipo de Servidor'
        verbose_name_plural = 'Tipos de Servidores'


class RegimenPensionario(models.Model):
    nombre_regimen_pensionario = models.CharField(
        max_length=45, verbose_name='Nombre de Régimen Pensionario')

    def __str__(self):
        return self.nombre_regimen_pensionario

    class Meta:
        db_table = 'regimen_pensionario'
        ordering = ['nombre_regimen_pensionario']
        verbose_name = 'Régimen Pensionario'
        verbose_name_plural = 'Regímenes Pensionarios'


class Afp(models.Model):
    nombre_afp = models.CharField(max_length=45, verbose_name='Nombre de AFP')

    def __str__(self):
        return self.nombre_afp

    class Meta:
        db_table = 'afp'
        ordering = ['nombre_afp']
        verbose_name = 'AFP'
        verbose_name_plural = 'AFPs'


class Banco(models.Model):
    nombre_banco = models.CharField(
        max_length=45, verbose_name='Nombre de Banco')

    def __str__(self):
        return self.nombre_banco

    class Meta:
        db_table = 'banco'
        ordering = ['nombre_banco']
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
