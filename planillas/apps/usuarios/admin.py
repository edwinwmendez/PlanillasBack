# apps/usuarios/admin.py
from django.contrib import admin
from .models import Persona, Beneficiario, Ugel

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'paterno', 'materno', 'tipo_documento', 'numero_documento', 'email']
    search_fields = ['nombres', 'paterno', 'materno', 'numero_documento']
    list_filter = ['tipo_documento', 'sexo']
    ordering = ['paterno', 'materno', 'nombres']

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ['persona', 'empleado', 'tipo_beneficiario', 'tipo_descuento', 'descuento_fijo', 'porcentaje_descuento', 'estado']
    search_fields = ['persona__nombres', 'persona__paterno', 'persona__materno', 'empleado__persona__nombres', 'empleado__persona__paterno', 'empleado__persona__materno']
    list_filter = ['tipo_beneficiario', 'tipo_descuento', 'estado']
    ordering = ['persona', 'empleado']

@admin.register(Ugel)
class UgelAdmin(admin.ModelAdmin):
    list_display = ['nombre_ugel', 'nombre_corto']
    search_fields = ['nombre_ugel', 'nombre_corto']
    ordering = ['nombre_ugel']
