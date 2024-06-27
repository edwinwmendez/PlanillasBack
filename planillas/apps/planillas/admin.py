# apps/planillas/admin.py
from django.contrib import admin
from .models import Periodo, PlanillaBeneficiario, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Contrato
from apps.transacciones.admin import TransaccionTrabajadorInline

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'mes', 'anio', 'es_adicional', 'periodo_actual')
    search_fields = ('mes', 'anio', 'periodo')
    list_filter = ('es_adicional',)
    ordering = ('anio', 'mes')

@admin.register(PlanillaBeneficiario)
class PlanillaBeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('beneficiario', 'periodo', 'monto')
    search_fields = ('beneficiario__persona__nombres', 'beneficiario__persona__paterno', 'beneficiario__persona__materno')
    list_filter = ('periodo',)
    ordering = ('beneficiario', 'periodo')

@admin.register(TipoPlanilla)
class TipoPlanillaAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_planilla', 'codigo_tipo_planilla')
    search_fields = ('nombre_tipo_planilla', 'codigo_tipo_planilla')
    ordering = ('nombre_tipo_planilla',)

@admin.register(ClasePlanilla)
class ClasePlanillaAdmin(admin.ModelAdmin):
    list_display = ('nombre_clase_planilla', 'codigo_clase_planilla', 'tipo_planilla')
    search_fields = ('nombre_clase_planilla', 'codigo_clase_planilla')
    list_filter = ('tipo_planilla',)
    ordering = ('nombre_clase_planilla',)

@admin.register(FuenteFinanciamiento)
class FuenteFinanciamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre_fuente_financiamiento',)
    search_fields = ('nombre_fuente_financiamiento',)
    list_filter = ('nombre_fuente_financiamiento',)
    ordering = ('nombre_fuente_financiamiento',)

# apps/trabajadores/admin.py

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'cargo', 'fecha_ingreso', 'fecha_cese', 'situacion')
    search_fields = ('trabajador__persona__nombres', 'trabajador__persona__paterno', 'trabajador__persona__materno', 'cargo__nombre_cargo')
    list_filter = ('situacion', 'cargo', 'fecha_ingreso', 'fecha_cese')
    ordering = ('trabajador', 'fecha_ingreso')
    inlines = [TransaccionTrabajadorInline]

