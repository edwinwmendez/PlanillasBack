from django.contrib import admin
from .models import ProcesosPlanilla
from apps.planillas.models import Planilla
from .periodo_normal import CalcularPlanillaRemuneraciones, GenerarBoletasPago, CerrarAperturarPeriodo

@admin.action(description='Generar boletas para las planillas seleccionadas')
def generar_boletas(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            GenerarBoletasPago.generar(planilla.id)
    modeladmin.message_user(request, "Boletas generadas exitosamente.")

@admin.action(description='Calcular planilla de remuneraciones para las planillas seleccionadas')
def calcular_planilla_remuneraciones(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            CalcularPlanillaRemuneraciones.calcular(planilla.id)
    modeladmin.message_user(request, "Planillas de remuneraciones calculadas exitosamente.")


@admin.action(description='Cerrar y aperturar nuevo periodo')
def cerrar_aperturar_periodo(modeladmin, request, queryset):
    for proceso in queryset:
        try:
        # Asumiendo que se obtienen mes, anio y es_adicional de algún formulario o método
            periodo = "202407"
            es_adicional = False  # Ejemplo de valor, cambiar según sea necesario
            CerrarAperturarPeriodo.cerrar_aperturar(periodo, es_adicional)
            modeladmin.message_user(request, "Periodo cerrado y nuevo periodo creado exitosamente.")
        except Exception as e:
            modeladmin.message_user(request, f"Error al cerrar y aperturar periodo: {str(e)}", level='error')

@admin.action(description='Revertir cálculo de planilla de remuneraciones para las planillas seleccionadas')
def revertir_calculo(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            CalcularPlanillaRemuneraciones.revertir_calculo(planilla.id)
    modeladmin.message_user(request, "Cálculo de planillas de remuneraciones revertido exitosamente.")

@admin.action(description='Revertir boletas generadas para las planillas seleccionadas')
def revertir_boletas_generadas(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            GenerarBoletasPago.revertir_boletas_generadas(planilla.id)
    modeladmin.message_user(request, "Boletas generadas revertidas exitosamente.")

@admin.action(description='Revertir Cierre/Apertura de periodos')
def revertir_cierre_apertura(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            CerrarAperturarPeriodo.revertir_cierre_apertura(planilla.periodo)
    modeladmin.message_user(request, "Cierre/Apertura de periodos revertidos exitosamente.")


class PlanillaInline(admin.TabularInline):
    model = ProcesosPlanilla.planillas.through
    extra = 1

@admin.register(ProcesosPlanilla)
class ProcesosPlanillaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'planillas_count')
    actions = [cerrar_aperturar_periodo, calcular_planilla_remuneraciones, revertir_calculo, generar_boletas, revertir_boletas_generadas, revertir_cierre_apertura]
    inlines = [PlanillaInline]
    exclude = ('planillas',)

    def planillas_count(self, obj):
        return obj.planillas.count()
    planillas_count.short_description = 'Número de Planillas'