# apps/auditoria/admin.py
from django.contrib import admin
from .models import Auditoria

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'descripcion', 'persona', 'ip_address', 'user_agent', 'accion']
    search_fields = ['descripcion', 'persona__nombres', 'persona__paterno', 'persona__materno', 'ip_address', 'accion']
    list_filter = ['fecha', 'accion']
    ordering = ['-fecha']
