# apps/transacciones/admin.py
from django.contrib import admin
from .models import TransaccionTrabajador

@admin.register(TransaccionTrabajador)
class TransaccionTrabajadorAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'transaccion', 'monto', 'periodo_inicial', 'periodo_final', 'correlativo','estado')
    search_fields = (
        'contrato__trabajador__persona__nombres',
        'contrato__trabajador__persona__apellido_paterno',
        'contrato__trabajador__persona__apellido_materno',
        'transaccion__descripcion_transaccion'
    )
    list_filter = ('estado', 'transaccion__tipo_transaccion')
    ordering = ('transaccion', 'correlativo')
    autocomplete_fields = ['contrato', 'transaccion']
