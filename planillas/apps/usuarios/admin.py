# apps/usuarios/admin.py
from django.contrib import admin
from .models import Persona, Beneficiario, User, Ugel
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('role', 'ugel')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Additional info', {
            'fields': ('role', 'ugel')
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role', 'ugel')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellido_paterno', 'apellido_materno', 'tipo_documento', 'numero_documento', 'email']
    search_fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'numero_documento']
    list_filter = ['tipo_documento', 'sexo']
    ordering = ['apellido_paterno', 'apellido_materno', 'nombres']

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ['persona', 'trabajador', 'tipo_beneficiario', 'tipo_descuento', 'descuento_fijo', 'porcentaje_descuento', 'estado']
    search_fields = ['persona__nombres', 'persona__apellido_paterno', 'persona__apellido_materno', 'empleado__persona__nombres', 'empleado__persona__apellido_paterno', 'empleado__persona__apellido_materno']
    list_filter = ['tipo_beneficiario', 'tipo_descuento', 'estado']
    ordering = ['persona', 'trabajador']