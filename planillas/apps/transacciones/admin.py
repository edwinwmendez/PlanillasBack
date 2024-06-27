# apps/transacciones/admin.py
from django.contrib import admin
from .models import Transaccion, TransaccionTrabajador

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'tipo', 'categoria')
    search_fields = ('codigo', 'descripcion', 'tipo', 'categoria')
    list_filter = ('tipo', 'categoria')
    ordering = ('codigo',)

@admin.register(TransaccionTrabajador)
class TransaccionTrabajadorAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'transaccion', 'monto', 'periodo_inicial', 'periodo_final', 'estado')
    search_fields = ('trabajador__persona__nombres', 'trabajador__persona__paterno', 'trabajador__persona__materno', 'transaccion__descripcion')
    list_filter = ('estado', 'transaccion__tipo')
    ordering = ('transaccion', 'correlativo')
    autocomplete_fields = ['trabajador', 'transaccion']
