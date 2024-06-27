# apps/trabajadores/admin.py
from django.contrib import admin
from .models import Trabajador, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('persona', 'estado')
    search_fields = ('persona__nombres', 'persona__paterno', 'persona__materno', 'cargo__nombre_cargo')
    list_filter = ('estado',)
    ordering = ('persona__paterno', 'persona__materno', 'persona__nombres')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cargo',)
    search_fields = ('nombre_cargo',)
    ordering = ('nombre_cargo',)

@admin.register(RegimenLaboral)
class RegimenLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombre_regimen_laboral',)
    search_fields = ('nombre_regimen_laboral',)
    ordering = ('nombre_regimen_laboral',)

@admin.register(TipoServidor)
class TipoServidorAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_servidor',)
    search_fields = ('nombre_tipo_servidor',)
    ordering = ('nombre_tipo_servidor',)

@admin.register(RegimenPensionario)
class RegimenPensionarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_regimen_pensionario',)
    search_fields = ('nombre_regimen_pensionario',)
    ordering = ('nombre_regimen_pensionario',)

@admin.register(Afp)
class AfpAdmin(admin.ModelAdmin):
    list_display = ('nombre_afp',)
    search_fields = ('nombre_afp',)
    ordering = ('nombre_afp',)

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre_banco',)
    search_fields = ('nombre_banco',)
    ordering = ('nombre_banco',)

@admin.register(Situacion)
class SituacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'abreviatura', 'codigo', 'created', 'updated')
    search_fields = ('nombre', 'abreviatura', 'codigo')
    ordering = ('nombre',)