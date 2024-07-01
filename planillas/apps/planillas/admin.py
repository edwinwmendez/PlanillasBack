# apps/planillas/admin.py
from django.contrib import admin
from .models import  PlanillaBeneficiario, Contrato, Planilla, Boleta
from apps.configuracion.admin import TransaccionTrabajadorInline

@admin.register(PlanillaBeneficiario)
class PlanillaBeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('beneficiario', 'periodo', 'monto')
    search_fields = ('beneficiario__persona__nombres', 'beneficiario__persona__paterno', 'beneficiario__persona__materno')
    list_filter = ('periodo',)
    ordering = ('beneficiario', 'periodo')
# apps/trabajadores/admin.py

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'cargo', 'fecha_ingreso', 'fecha_cese', 'situacion')
    search_fields = ('trabajador__persona__nombres', 'trabajador__persona__paterno', 'trabajador__persona__materno', 'cargo__nombre_cargo')
    list_filter = ('situacion', 'cargo', 'fecha_ingreso', 'fecha_cese')
    ordering = ('trabajador', 'fecha_ingreso')
    inlines = [TransaccionTrabajadorInline]

@admin.register(Planilla)
class PlanillaAdmin(admin.ModelAdmin):
    list_display = ('correlativo', 'clase_planilla', 'fuente_financiamiento', 'periodo', 'total_haberes', 'total_descuentos', 'total_aportes', 'estado')
    search_fields = ('correlativo', 'clase_planilla__nombre_clase_planilla', 'fuente_financiamiento__nombre_fuente_financiamiento', 'periodo__periodo')
    list_filter = ('clase_planilla', 'fuente_financiamiento', 'periodo', 'estado')
    ordering = ('correlativo', 'periodo')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('clase_planilla', 'fuente_financiamiento', 'periodo')
        return queryset

@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display = ('numero_boleta', 'planilla', 'contrato', 'total_haberes', 'total_descuentos', 'total_aportes', 'neto_a_pagar')
    search_fields = ('numero_boleta', 'planilla__correlativo', 'contrato__trabajador__persona__nombres')
    list_filter = ('visualizada', 'descargada', 'planilla__periodo')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('contrato', 'planilla')
        return queryset