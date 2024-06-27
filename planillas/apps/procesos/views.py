# apps/procesos/views.py
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.planillas.models import PlanillaTrabajador, Periodo, TipoPlanilla
from apps.trabajadores.models import Trabajador
from apps.transacciones.models import TransaccionTrabajador
from .serializers import ProcesarPlanillaSerializer

class ProcesarPlanillaView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProcesarPlanillaSerializer(data=request.data)
        if serializer.is_valid():
            periodo = serializer.validated_data['periodo']
            tipo_planilla_id = serializer.validated_data['tipo_planilla']

            try:
                periodo_obj = Periodo.objects.get(periodo=periodo)
                tipo_planilla_obj = TipoPlanilla.objects.get(id=tipo_planilla_id)
            except (Periodo.DoesNotExist, TipoPlanilla.DoesNotExist) as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            trabajadores = Trabajador.objects.filter(situacion='HAB')
            for trabajador in trabajadores:
                total_haberes = TransaccionTrabajador.objects.filter(
                    trabajador=trabajador,
                    transaccion__tipo='HABER',
                    periodo_inicial__lte=periodo,
                    periodo_final__gte=periodo
                ).aggregate(total=models.Sum('monto'))['total'] or 0

                total_descuentos = TransaccionTrabajador.objects.filter(
                    trabajador=trabajador,
                    transaccion__tipo='DESCUENTO',
                    periodo_inicial__lte=periodo,
                    periodo_final__gte=periodo
                ).aggregate(total=models.Sum('monto'))['total'] or 0

                essalud = total_haberes * 0.09  # Ejemplo de cálculo de ESSALUD

                PlanillaTrabajador.objects.create(
                    total_haberes=total_haberes,
                    total_descuentos=total_descuentos,
                    essalud=essalud,
                    emitio_boleta=0,
                    trabajador=trabajador,
                    tipo_planilla=tipo_planilla_obj,
                    periodo=periodo_obj,
                    ugel=trabajador.ugel
                )

            return Response({"message": "Planillas procesadas exitosamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
