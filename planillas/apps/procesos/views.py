# apps/procesos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import ProcesoPlanilla

class CerrarAperturarPeriodoView(APIView):
    def post(self, request):
        try:
            ProcesoPlanilla.cerrar_aperturar_periodo()
            return Response({"message": "Periodo cerrado y nuevo periodo aperturado con éxito."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CalcularPlanillaRemuneracionesView(APIView):
    def post(self, request):
        try:
            ProcesoPlanilla.calcular_planilla_remuneraciones()
            return Response({"message": "Planilla de remuneraciones calculada con éxito."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GenerarBoletasPagoView(APIView):
    def post(self, request):
        planilla_id = request.data.get('planilla_id')
        if not planilla_id:
            return Response({"error": "Se requiere el ID de la planilla."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ProcesoPlanilla.generar_boletas_pago(planilla_id)
            return Response({"message": "Boletas de pago generadas con éxito."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)