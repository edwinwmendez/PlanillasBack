# apps/planillas/admin.py
from django.contrib import admin
from .models import Periodo, PlanillaTrabajador, PlanillaBeneficiario, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'mes', 'anio', 'es_adicional', 'periodo_actual')
    search_fields = ('mes', 'anio', 'periodo')
    list_filter = ('es_adicional',)
    ordering = ('anio', 'mes')

@admin.register(PlanillaTrabajador)
class PlanillaTrabajadorAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'total_haberes', 'total_descuentos', 'essalud', 'emitio_boleta', 'periodo', 'ugel', 'tipo_planilla')
    search_fields = ('trabajador__persona__nombres', 'trabajador__persona__paterno', 'trabajador__persona__materno')
    list_filter = ('periodo', 'ugel', 'tipo_planilla')
    ordering = ('trabajador', 'periodo')

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
    list_display = ('nombre_fuente_financiamiento', 'tipo_planilla')
    search_fields = ('nombre_fuente_financiamiento',)
    list_filter = ('tipo_planilla',)
    ordering = ('nombre_fuente_financiamiento',)
