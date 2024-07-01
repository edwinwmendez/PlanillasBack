from django.contrib import admin
from .models import Ugel, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Periodo, Transaccion, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion, TipoDocumento, Sexo, EstadoCivil
from apps.transacciones.models import TransaccionTrabajador

# Register your models here.
@admin.register(Ugel)
class UgelAdmin(admin.ModelAdmin):
    list_display = ['nombre_ugel', 'nombre_corto_ugel']
    search_fields = ['nombre_ugel', 'nombre_corto_ugel']
    ordering = ['nombre_ugel']

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'mes', 'anio', 'es_adicional', 'periodo_actual')
    search_fields = ('mes', 'anio', 'periodo')
    list_filter = ('es_adicional',)
    ordering = ('anio', 'mes')


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



class TransaccionTrabajadorInline(admin.TabularInline):
    model = TransaccionTrabajador
    extra = 1  # Número de formularios adicionales vacíos que se mostrarán

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('codigo_transaccion_mcpp', 'codigo_transaccion_plame', 'descripcion_transaccion', 'tipo_transaccion')
    search_fields = ('codigo_transaccion_mcpp', 'codigo_transaccion_plame', 'descripcion_transaccion', 'tipo_transaccion')
    list_filter = ('tipo_transaccion','imponible')
    ordering = ('codigo_transaccion_mcpp','codigo_transaccion_plame')


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
    list_display = ('nombre_banco','codigo_banco','abreviatura_banco')
    search_fields = ('nombre_banco',)
    ordering = ('nombre_banco',)

@admin.register(Situacion)
class SituacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_situacion', 'abreviatura_situacion', 'codigo_situacion', 'created', 'updated')
    search_fields = ('nombre_situacion', 'abreviatura_situacion', 'codigo_situacion')
    ordering = ('nombre_situacion',)

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('descripcion_tipo_documento', 'codigo_tipo_documento')
    search_fields = ('descripcion_tipo_documento', 'codigo_tipo_documento')
    ordering = ('descripcion_tipo_documento',)

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display = ('descripcion_sexo', 'codigo_sexo')
    search_fields = ('descripcion_sexo', 'codigo_sexo')
    ordering = ('descripcion_sexo',)

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado_civil', 'codigo_estado_civil')
    search_fields = ('nombre_estado_civil', 'codigo_estado_civil')
    ordering = ('nombre_estado_civil',)