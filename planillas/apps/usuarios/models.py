# apps/usuarios/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.configuracion.models import TipoDocumento, Sexo, TipoDescuento, TipoBeneficiario, Ugel, EstadoCivil
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMINISTRADOR_DEL_SISTEMA = 'admin_sistema'
    ADMINISTRADOR_UGEL = 'admin_ugel'
    TECNICO_DE_PROCESOS = 'tecnico_procesos'
    TECNICO_DE_PLANILLAS = 'tecnico_planillas'
    TRABAJADOR = 'trabajador'

    ROLE_CHOICES = [
        (ADMINISTRADOR_DEL_SISTEMA, 'Administrador del Sistema'),
        (ADMINISTRADOR_UGEL, 'Administrador UGEL'),
        (TECNICO_DE_PROCESOS, 'Técnico de Procesos'),
        (TECNICO_DE_PLANILLAS, 'Técnico de Planillas'),
        (TRABAJADOR, 'Trabajador'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=TRABAJADOR,
        verbose_name='Rol'
    )
    ugel = models.ForeignKey(Ugel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='UGEL')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos concedidos a cada uno de sus grupos.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario',
    )


class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,related_name='persona')
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=12, unique=True, db_index=True,verbose_name='Número de Documento')
    apellido_paterno = models.CharField(max_length=45, blank=True, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=45, blank=True, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=45, blank=True, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, verbose_name='Sexo')
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, verbose_name='Estado Civil')
    direccion = models.CharField(max_length=100, blank=True, verbose_name='Dirección')
    email = models.EmailField(max_length=45, blank=True, verbose_name='Email')
    telefono = models.CharField(max_length=9, blank=True, verbose_name='Teléfono')

    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'


    def get_full_name(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'.strip()

    def clean(self):
        if self.tipo_documento.codigo_tipo_documento == 'DNI' and len(self.numero_documento) != 8:
            raise ValidationError(_('El DNI debe tener 8 caracteres.'))
        elif self.tipo_documento.codigo_tipo_documento == 'CET' and len(self.numero_documento) != 9:
            raise ValidationError(_('El Carnet de extranjería debe tener 9 caracteres.'))
        elif self.tipo_documento.codigo_tipo_documento == 'PAS' and len(self.numero_documento) != 12:
            raise ValidationError(_('El pasaporte debe tener 12 caracteres.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'persona'
        ordering = ['apellido_paterno', 'apellido_materno', 'nombres']
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class Beneficiario(models.Model):
    trabajador = models.ForeignKey(
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
        'configuracion.Banco', on_delete=models.CASCADE, verbose_name='Banco'
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