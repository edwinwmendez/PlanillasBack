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
    list_display = ('trabajador', 'fuente_financiamiento', 'cargo', 'fecha_ingreso', 'fecha_cese', 'situacion')
    search_fields = ('trabajador__persona__nombres', 'trabajador__persona__apellido_paterno', 'trabajador__persona__apellido_materno', 'cargo__nombre_cargo')
    list_filter = ('situacion', 'cargo', 'fecha_ingreso', 'fecha_cese')
    ordering = ('trabajador', 'fecha_ingreso')
    autocomplete_fields = ['trabajador', 'cargo', 'clase_planilla', 'fuente_financiamiento']
    inlines = [TransaccionTrabajadorInline]


@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display = ('numero_boleta', 'planilla', 'contrato', 'total_haberes', 'total_descuentos', 'total_aportes', 'neto_a_pagar')
    search_fields = ('numero_boleta', 'planilla__correlativo', 'contrato__trabajador__persona__nombres')
    list_filter = ('visualizada', 'descargada', 'planilla__periodo')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('contrato', 'planilla')
        return queryset



from apps.procesos.utils import generar_boletas_para_planilla

@admin.action(description='Generar boletas para esta planilla')
def generar_boletas(modeladmin, request, queryset):
    for planilla in queryset:
        generar_boletas_para_planilla(planilla.id)
    modeladmin.message_user(request, "Boletas generadas exitosamente.")

@admin.register(Planilla)
class PlanillaAdmin(admin.ModelAdmin):
    list_display = ('correlativo', 'clase_planilla', 'fuente_financiamiento', 'periodo', 'total_haberes', 'total_descuentos', 'total_aportes', 'estado')
    actions = [generar_boletas]
    search_fields = ('correlativo', 'clase_planilla__nombre', 'fuente_financiamiento__nombre')
    list_filter = ('estado', 'periodo', 'clase_planilla', 'fuente_financiamiento')
    ordering = ('correlativo', 'periodo')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('clase_planilla', 'fuente_financiamiento', 'periodo')
        return queryset

