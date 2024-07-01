# apps/transacciones/admin.py
from django.contrib import admin
from .models import TransaccionTrabajador

@admin.register(TransaccionTrabajador)
class TransaccionTrabajadorAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'transaccion', 'monto', 'periodo_inicial', 'periodo_final', 'estado')
    search_fields = ('contrato__trabajador__persona__nombres', 'contrato__trabajador__persona__paterno', 'contrato__trabajador__persona__materno', 'transaccion__descripcion')
    list_filter = ('estado', 'transaccion__tipo_transaccion')
    ordering = ('transaccion', 'correlativo')
    autocomplete_fields = ['contrato', 'transaccion']
