# apps/trabajadores/admin.py
from django.contrib import admin
from .models import Trabajador

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('persona', 'estado')
    search_fields = ('persona__nombres', 'persona__apellido_paterno', 'persona__materno', 'cargo__nombre_cargo')
    list_filter = ('estado',)
    ordering = ('persona__apellido_paterno', 'persona__apellido_materno', 'persona__nombres')
