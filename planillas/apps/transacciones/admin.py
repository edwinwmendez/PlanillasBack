# apps/transacciones/admin.py
from django.contrib import admin
from .models import Transaccion, TransaccionTrabajador

class TransaccionTrabajadorInline(admin.TabularInline):
    model = TransaccionTrabajador
    extra = 1  # Número de formularios adicionales vacíos que se mostrarán

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'tipo', 'categoria')
    search_fields = ('codigo', 'descripcion', 'tipo', 'categoria')
    list_filter = ('tipo', 'categoria')
    ordering = ('codigo',)

@admin.register(TransaccionTrabajador)
class TransaccionTrabajadorAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'transaccion', 'monto', 'periodo_inicial', 'periodo_final', 'estado')
    search_fields = ('contrato__trabajador__persona__nombres', 'contrato__trabajador__persona__paterno', 'contrato__trabajador__persona__materno', 'transaccion__descripcion')
    list_filter = ('estado', 'transaccion__tipo')
    ordering = ('transaccion', 'correlativo')
    autocomplete_fields = ['contrato', 'transaccion']
