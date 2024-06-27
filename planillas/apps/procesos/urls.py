# apps/procesos/urls.py
from django.urls import path
from .views import ProcesarPlanillaView

urlpatterns = [
    path('procesar-planilla/', ProcesarPlanillaView.as_view(), name='procesar-planilla'),
]
