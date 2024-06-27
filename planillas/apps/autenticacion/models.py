# apps/autenticacion/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

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
    ugel = models.ForeignKey('usuarios.Ugel', on_delete=models.CASCADE, null=True, blank=True, verbose_name='UGEL')

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
