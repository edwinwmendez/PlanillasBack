# apps/usuarios/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.autenticacion.models import User

class TipoDocumento(models.Model):
    codigo = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion = models.CharField(max_length=50, verbose_name='Descripción')

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_documento'
        ordering = ['descripcion']
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'


class Sexo(models.Model):
    codigo = models.CharField(max_length=1, unique=True, verbose_name='Código')
    descripcion = models.CharField(max_length=20, verbose_name='Descripción')

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'sexo'
        ordering = ['descripcion']
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'


class TipoDescuento(models.Model):
    codigo = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion = models.CharField(max_length=20, verbose_name='Descripción')

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_descuento'
        ordering = ['descripcion']
        verbose_name = 'Tipo de Descuento'
        verbose_name_plural = 'Tipos de Descuento'


class TipoBeneficiario(models.Model):
    codigo = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion = models.CharField(max_length=20, verbose_name='Descripción')

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_beneficiario'
        ordering = ['descripcion']
        verbose_name = 'Tipo de Beneficiario'
        verbose_name_plural = 'Tipos de Beneficiario'


class Persona(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True,
        related_name='persona'
    )
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name='Tipo de Documento')
    numero_documento = models.CharField(
        max_length=12, unique=True, db_index=True,
        verbose_name='Número de Documento'
    )
    paterno = models.CharField(
        max_length=45, blank=True, verbose_name='Apellido Paterno')
    materno = models.CharField(
        max_length=45, blank=True, verbose_name='Apellido Materno')
    nombres = models.CharField(
        max_length=45, blank=True, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Nacimiento')
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, verbose_name='Sexo')
    direccion = models.CharField(
        max_length=100, blank=True, verbose_name='Dirección')
    email = models.EmailField(max_length=45, blank=True, verbose_name='Email')

    def __str__(self):
        return f'{self.nombres} {self.paterno} {self.materno}'

    def get_full_name(self):
        return f'{self.nombres} {self.paterno} {self.materno}'.strip()

    def clean(self):
        if self.tipo_documento.codigo == 'DNI' and len(self.numero_documento) != 8:
            raise ValidationError(_('El DNI debe tener 8 caracteres.'))
        elif self.tipo_documento.codigo == 'CET' and len(self.numero_documento) != 9:
            raise ValidationError(_('El Carnet de extranjería debe tener 9 caracteres.'))
        elif self.tipo_documento.codigo == 'PAS' and len(self.numero_documento) != 12:
            raise ValidationError(_('El pasaporte debe tener 12 caracteres.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'persona'
        ordering = ['paterno', 'materno', 'nombres']
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class Beneficiario(models.Model):
    empleado = models.ForeignKey(
        'trabajadores.Trabajador', on_delete=models.CASCADE, verbose_name='Empleado', related_name='beneficiarios'
    )
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona'
    )
    relacion_trabajador = models.CharField(
        max_length=45, blank=True, verbose_name='Relación del Trabajador'
    )
    documento_descuento = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Descuento'
    )
    numero_cuenta = models.CharField(
        max_length=20, blank=True, verbose_name='Número de Cuenta'
    )
    tipo_beneficiario = models.ForeignKey(TipoBeneficiario, on_delete=models.CASCADE, default=1, verbose_name='Tipo de Beneficiario')
    tipo_descuento = models.ForeignKey(TipoDescuento, on_delete=models.CASCADE, default=1, verbose_name='Tipo de Descuento')
    descuento_fijo = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Descuento Fijo'
    )
    porcentaje_descuento = models.IntegerField(
        null=True, blank=True, verbose_name='Porcentaje de Descuento'
    )
    fecha_inicio = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Inicio'
    )
    fecha_fin = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Fin'
    )
    estado = models.BooleanField(
        verbose_name='Estado', default=True, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    banco = models.ForeignKey(
        'trabajadores.Banco', on_delete=models.CASCADE, verbose_name='Banco'
    )

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno}'

    class Meta:
        db_table = 'beneficiario'
        ordering = ['id']
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'

    def clean(self):
        if self.tipo_descuento.codigo == 'MF' and not self.descuento_fijo:
            raise ValidationError('Debe especificar un monto fijo para el descuento.')
        if self.tipo_descuento.codigo == 'DP' and not self.porcentaje_descuento:
            raise ValidationError('Debe especificar un porcentaje para el descuento.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Ugel(models.Model):
    nombre_ugel = models.CharField(
        max_length=100, verbose_name='Nombre de Ugel')
    nombre_corto = models.CharField(
        max_length=25, verbose_name='Nombre Corto', null=True, blank=True)

    def __str__(self):
        return self.nombre_corto

    class Meta:
        db_table = 'ugel'
        ordering = ['nombre_ugel']
        verbose_name = 'UGEL'
        verbose_name_plural = 'UGELs'
