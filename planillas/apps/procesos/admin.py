from django.contrib import admin
from .models import ProcesosPlanilla
from apps.planillas.models import Planilla
from .services import ProcesoPlanilla

@admin.action(description='Generar boletas para las planillas seleccionadas')
def generar_boletas(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            ProcesoPlanilla.generar_boletas_pago(planilla.id)
    modeladmin.message_user(request, "Boletas generadas exitosamente.")

@admin.action(description='Calcular planilla de remuneraciones para las planillas seleccionadas')
def calcular_planilla_remuneraciones(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            ProcesoPlanilla.calcular_planilla_remuneraciones(planilla.id)
    modeladmin.message_user(request, "Planillas de remuneraciones calculadas exitosamente.")

class PlanillaInline(admin.TabularInline):
    model = ProcesosPlanilla.planillas.through
    extra = 1

@admin.register(ProcesosPlanilla)
class ProcesosPlanillaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'planillas_count')
    actions = [generar_boletas, calcular_planilla_remuneraciones]
    inlines = [PlanillaInline]
    exclude = ('planillas',)

    def planillas_count(self, obj):
        return obj.planillas.count()
    planillas_count.short_description = 'Número de Planillas'