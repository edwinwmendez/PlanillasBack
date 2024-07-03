# apps/procesos/urls.py
from django.urls import path
from .views import CerrarAperturarPeriodoView, CalcularPlanillaRemuneracionesView, GenerarBoletasPagoView

urlpatterns = [
    path('cerrar-aperturar-periodo/', CerrarAperturarPeriodoView.as_view(), name='cerrar-aperturar-periodo'),
    path('calcular-planilla-remuneraciones/', CalcularPlanillaRemuneracionesView.as_view(), name='calcular-planilla-remuneraciones'),
    path('generar-boletas-pago/', GenerarBoletasPagoView.as_view(), name='generar-boletas-pago'),
]