# apps/trabajadores/models.py
from django.db import models
from apps.usuarios.models import Persona

class Trabajador(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    tiempo_servicios = models.CharField(max_length=6, blank=True, verbose_name='Tiempo de Servicios')
    regimen_pensionario = models.ForeignKey('trabajadores.RegimenPensionario', on_delete=models.CASCADE, verbose_name='Régimen Pensionario')
    afp = models.ForeignKey('trabajadores.Afp', on_delete=models.CASCADE, verbose_name='AFP')
    cuspp = models.CharField(max_length=12, blank=True, verbose_name='CUSPP')
    fecha_afiliacion = models.DateField(null=True, blank=True, verbose_name='Fecha de Afiliación')
    fecha_devengue = models.DateField(null=True, blank=True, verbose_name='Fecha de Devengue')
    banco = models.ForeignKey('trabajadores.Banco', on_delete=models.CASCADE, verbose_name='Banco')
    numero_cuenta = models.CharField(max_length=45, blank=True, verbose_name='Número de Cuenta')
    ruc = models.CharField(max_length=11, blank=True, verbose_name='RUC')
    estado = models.BooleanField(verbose_name='Estado', default=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno}'

    class Meta:
        db_table = 'trabajador'
        ordering = ['id']
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        indexes = [
            models.Index(fields=['persona'], name='persona_idx'),
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

class Situacion(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='Nombre de Situación')
    abreviatura = models.CharField(max_length=10, verbose_name='Abreviatura')
    codigo = models.CharField(max_length=10, unique=True, verbose_name='Código')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'situacion'
        ordering = ['nombre']
        verbose_name = 'Situación'
        verbose_name_plural = 'Situaciones'