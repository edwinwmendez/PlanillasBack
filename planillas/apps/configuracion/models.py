# apps/configuracion/models.py
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from auditlog.registry import auditlog

class TipoDocumento(models.Model):
    codigo_tipo_documento = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion_tipo_documento = models.CharField(max_length=50, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion_tipo_documento

    class Meta:
        db_table = 'tipo_documento'
        ordering = ['descripcion_tipo_documento']
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "La UGEL ya se encuentra registrada."},
                status=status.HTTP_400_BAD_REQUEST
            )


class Sexo(models.Model):
    codigo_sexo = models.CharField(max_length=1, unique=True, verbose_name='Código')
    descripcion_sexo = models.CharField(max_length=20, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion_sexo

    class Meta:
        db_table = 'sexo'
        ordering = ['descripcion_sexo']
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class TipoDescuento(models.Model):
    codigo_tipo_descuento = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion_tipo_descuento = models.CharField(max_length=20, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_descuento'
        ordering = ['descripcion_tipo_descuento']
        verbose_name = 'Tipo de Descuento'
        verbose_name_plural = 'Tipos de Descuento'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class TipoBeneficiario(models.Model):
    codigo_tipo_beneficiario = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion_tipo_beneficiario = models.CharField(max_length=20, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_beneficiario'
        ordering = ['descripcion_tipo_beneficiario']
        verbose_name = 'Tipo de Beneficiario'
        verbose_name_plural = 'Tipos de Beneficiario'


class Ugel(models.Model):
    nombre_ugel = models.CharField(max_length=100, verbose_name='Nombre de UGEL')
    nombre_corto_ugel = models.CharField(max_length=25, verbose_name='Nombre Corto de UGEL', null=True, blank=True)
    codigo_ugel = models.CharField(max_length=3, verbose_name='Código de Ugel', unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_corto_ugel

    class Meta:
        db_table = 'ugel'
        ordering = ['nombre_ugel']
        verbose_name = 'UGEL'
        verbose_name_plural = 'UGELs'
        indexes = [
            models.Index(fields=['codigo_ugel'], name='idx_ugel_codigo'),
        ]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class Periodo(models.Model):
    periodo = models.CharField(max_length=6, unique=True, blank=True, verbose_name='Periodo', editable=False)
    es_adicional = models.BooleanField(default=False, verbose_name='¿Es adicional?')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.periodo} - {self.estado}'

    class Meta:
        db_table = 'periodo'
        ordering = ['periodo', 'es_adicional']
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
        indexes = [
            models.Index(fields=['periodo', 'estado'], name='idx_periodo_estado'),
        ]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

class TipoPlanilla(models.Model):
    nombre_tipo_planilla = models.CharField(max_length=45, blank=True, verbose_name='Nombre de Tipo de Planilla')
    codigo_tipo_planilla = models.CharField(max_length=2, unique=True, blank=True, verbose_name='Código de Tipo de Planilla')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_tipo_planilla

    class Meta:
        db_table = 'tipo_planilla'
        ordering = ['nombre_tipo_planilla']
        verbose_name = 'Tipo de Planilla'
        verbose_name_plural = 'Tipos de Planilla'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class ClasePlanilla(models.Model):
    nombre_clase_planilla = models.CharField(max_length=45, blank=True, verbose_name='Nombre de Clase de Planilla')
    codigo_clase_planilla = models.CharField(max_length=2, unique=True, blank=True, verbose_name='Código de Clase de Planilla')
    tipo_planilla = models.ForeignKey(TipoPlanilla, on_delete=models.CASCADE, verbose_name='Tipo de Planilla', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_clase_planilla

    class Meta:
        db_table = 'clase_planilla'
        ordering = ['nombre_clase_planilla']
        verbose_name = 'Clase de Planilla'
        verbose_name_plural = 'Clases de Planilla'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class FuenteFinanciamiento(models.Model):
    nombre_fuente_financiamiento = models.CharField(max_length=45, blank=True, verbose_name='Nombre de Fuente de Financiamiento')
    codigo_fuente_financiamiento = models.CharField(max_length=2, unique=True, blank=True, verbose_name='Código de Fuente de Financiamiento')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_fuente_financiamiento

    class Meta:
        db_table = 'fuente_financiamiento'
        ordering = ['nombre_fuente_financiamiento']
        verbose_name = 'Fuente de Financiamiento'
        verbose_name_plural = 'Fuentes de Financiamiento'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('HABER', 'Haber'),
        ('DESCUENTO', 'Descuento'),
        ('APORTE', 'Aporte')
    ]
    CATEGORIA_CHOICES = [
        ('SUELDO', 'Sueldo'),
        ('BONIFICACION', 'Bonificación'),
        ('DEDUCCION', 'Deducción'),
        ('BENEFICIOS_SOCIALES', 'Beneficios Sociales'),
        ('APORTE', 'Aporte'),
        ('OTRO', 'Otro')
    ]

    tipo_transaccion = models.CharField(max_length=10, choices=TIPO_CHOICES, verbose_name='Tipo', default='HABER')
    categoria_transaccion = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, verbose_name='Categoría', default='SUELDO')
    codigo_transaccion_mcpp = models.CharField(max_length=4, unique=True, verbose_name='Código MCPP', help_text='Código MCPP')
    codigo_transaccion_plame = models.CharField(max_length=4, unique=True, verbose_name='Codigo PLAME', help_text='Codigo PLAME')
    descripcion_transaccion = models.CharField(max_length=45, verbose_name='Descripción')
    imponible = models.BooleanField(default=False, verbose_name='Es Imponible?')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.tipo_transaccion == 'HABER' and self.categoria_transaccion not in ['SUELDO', 'BONIFICACION', 'BENEFICIOS_SOCIALES', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Haber.'))
        if self.tipo_transaccion == 'DESCUENTO' and self.categoria_transaccion not in ['DEDUCCION', 'APORTE', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Descuento.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descripcion_transaccion

    class Meta:
        db_table = 'transaccion'
        ordering = ['descripcion_transaccion']
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'
        indexes = [
            models.Index(fields=['codigo_transaccion_mcpp'], name='idx_transaccion_codigo_mcpp'),
            models.Index(fields=['tipo_transaccion'], name='idx_transaccion_tipo'),
        ]


class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=45, verbose_name='Nombre de Cargo')
    codigo_cargo = models.CharField(max_length=3, unique=True, verbose_name='Código de Cargo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'cargo'
        ordering = ['nombre_cargo']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class RegimenLaboral(models.Model):
    nombre_regimen_laboral = models.CharField(max_length=45, verbose_name='Nombre de Régimen Laboral')
    codigo_regimen_laboral = models.CharField(max_length=2, unique=True, verbose_name='Código de Régimen Laboral')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_regimen_laboral

    class Meta:
        db_table = 'regimen_laboral'
        ordering = ['nombre_regimen_laboral']
        verbose_name = 'Régimen Laboral'
        verbose_name_plural = 'Regímenes Laborales'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class TipoServidor(models.Model):
    nombre_tipo_servidor = models.CharField(max_length=45, verbose_name='Nombre de Tipo de Servidor')
    codigo_tipo_servidor = models.CharField(max_length=2, unique=True, verbose_name='Código de Tipo de Servidor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_tipo_servidor

    class Meta:
        db_table = 'tipo_servidor'
        ordering = ['nombre_tipo_servidor']
        verbose_name = 'Tipo de Servidor'
        verbose_name_plural = 'Tipos de Servidores'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class RegimenPensionario(models.Model):
    nombre_regimen_pensionario = models.CharField(max_length=45, verbose_name='Nombre de Régimen Pensionario')
    codigo_regimen_pensionario = models.CharField(max_length=2, unique=True, verbose_name='Código de Régimen Pensionario')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_regimen_pensionario

    class Meta:
        db_table = 'regimen_pensionario'
        ordering = ['nombre_regimen_pensionario']
        verbose_name = 'Régimen Pensionario'
        verbose_name_plural = 'Regímenes Pensionarios'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class Afp(models.Model):
    nombre_afp = models.CharField(max_length=45, verbose_name='Nombre de AFP')
    codigo_afp = models.CharField(max_length=2, unique=True, verbose_name='Código de AFP')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_afp

    class Meta:
        db_table = 'afp'
        ordering = ['nombre_afp']
        verbose_name = 'AFP'
        verbose_name_plural = 'AFPs'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )


class Banco(models.Model):
    nombre_banco = models.CharField(max_length=45, verbose_name='Nombre de Banco')
    codigo_banco = models.CharField(max_length=3, unique=True, verbose_name='Código de Banco')
    abreviatura_banco = models.CharField(max_length=10, verbose_name='Abreviatura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_banco

    class Meta:
        db_table = 'banco'
        ordering = ['nombre_banco']
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

class Situacion(models.Model):
    nombre_situacion = models.CharField(max_length=45, verbose_name='Nombre de Situación')
    abreviatura_situacion = models.CharField(max_length=10, verbose_name='Abreviatura')
    codigo_situacion = models.CharField(max_length=10, unique=True, verbose_name='Código')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_situacion

    class Meta:
        db_table = 'situacion'
        ordering = ['nombre_situacion']
        verbose_name = 'Situación'
        verbose_name_plural = 'Situaciones'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

class EstadoCivil(models.Model):
    # el codigo de estado civil debe ser unico
    codigo_estado_civil = models.CharField(max_length=2, unique=True, verbose_name='Código de Estado Civil', null=True, blank=True)
    nombre_estado_civil = models.CharField(max_length=45, verbose_name='Nombre de Estado Civil')
    abreviatura_estado_civil = models.CharField(max_length=10, verbose_name='Abreviatura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_estado_civil

    class Meta:
        db_table = 'estado_civil'
        ordering = ['nombre_estado_civil']
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

# MCPP Web

class TipoRegistroAirhsp(models.Model):
    pass

class ConceptoRemunerativo(models.Model):
    tipo = models.CharField(max_length=45, verbose_name='Tipo(Si es Haber o Descuento)')
    codigo_mcpp = models.CharField(max_length=4, unique=True, verbose_name='Código MCPP Web')
    codigo_plame = models.CharField(max_length=4, verbose_name='Código Plame')
    descripcion= models.CharField(max_length=100, verbose_name='Descripción de la Norma')
    imponible = models.BooleanField(default=False, verbose_name='Es Imponible?')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class TipoDeCuenta(models.Model):
    pass


class ComisionAfp(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name='Periodo')
    afp = models.ForeignKey(Afp, on_delete=models.CASCADE, verbose_name='AFP')
    comision_flujo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Comisión por Flujo')
    comision_mixta = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Comisión Mixta')
    prima_seguro = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Prima de Seguro')
    aporte_obligatorio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Aporte Obligatorio')
    total_comision = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total Comisión')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.afp.nombre_afp + ' - ' + self.periodo.periodo + ' - ' + str(self.total_comision)

    def save(self, *args, **kwargs):
        # Calcular el total_comision
        self.total_comision = self.comision_flujo + self.comision_mixta + self.prima_seguro + self.aporte_obligatorio
        # Llamar al método save de la superclase
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'comision_afp'
        ordering = ['periodo']
        verbose_name = 'Comisión AFP'
        verbose_name_plural = 'Comisiones AFP'
        indexes = [
            models.Index(fields=['periodo', 'afp'], name='idx_comisionafp_periodo_afp'),
        ]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as e:
            return Response(
                {"detail": "El régimen pensionario ya se encuentra registrado."},
                status=status.HTTP_400_BAD_REQUEST
            )

class ConfiguracionGlobal(models.Model):
    clave = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    tipo_dato = models.CharField(max_length=20, choices=[
        ('NUMERIC', 'Numérico'),
        ('TEXT', 'Texto'),
        ('JSON', 'JSON'),
        ('BOOLEAN', 'Booleano'),
        ('DATE', 'Fecha'),
    ])

    def __str__(self):
        return self.clave

class ValorConfiguracionGlobal(models.Model):
    configuracion = models.ForeignKey(ConfiguracionGlobal, on_delete=models.CASCADE, related_name='valores')
    valor = models.TextField()
    norma = models.CharField(max_length=100, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    creado_por = models.ForeignKey('usuarios.User', on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.configuracion.clave}: {self.valor} (desde {self.fecha_inicio})"

    def save(self, *args, **kwargs):
        # Si es un nuevo registro (no tiene ID), cerrar el valor anterior
        if not self.pk:
            ValorConfiguracionGlobal.objects.filter(
                configuracion=self.configuracion,
                fecha_fin__isnull=True
            ).update(fecha_fin=self.fecha_inicio - timezone.timedelta(days=1))

        super().save(*args, **kwargs)


auditlog.register(Ugel)
auditlog.register(ComisionAfp)
auditlog.register(Cargo)
auditlog.register(Periodo)
auditlog.register(TipoPlanilla)
auditlog.register(ClasePlanilla)
auditlog.register(FuenteFinanciamiento)
auditlog.register(Transaccion)
auditlog.register(Banco)
auditlog.register(ConfiguracionGlobal)
auditlog.register(ValorConfiguracionGlobal)