# apps/planillas/views.py
from django.db.models import Max
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PlanillaBeneficiario, Contrato, Planilla, Boleta
from .serializers import PlanillaBeneficiarioSerializer, ContratoSerializer, PlanillaSerializer, BoletaSerializer
from apps.transacciones.models import TransaccionTrabajador
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class PlanillaBeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = PlanillaBeneficiario.objects.all()
    serializer_class = PlanillaBeneficiarioSerializer
    permission_classes = [IsAuthenticated]

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin_sistema':
            return Contrato.objects.all()
        return Contrato.objects.filter(trabajador__ugel=user.ugel)

class ProcesarPlanillaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        periodo = request.data.get('periodo')
        if not periodo:
            return Response({"error": "Debe especificar un período."}, status=status.HTTP_400_BAD_REQUEST)

        transacciones = TransaccionTrabajador.objects.filter(
            periodo_inicial__lte=periodo,
            periodo_final__gte=periodo
        )

        planillas_creadas = []
        for transaccion in transacciones:
            contrato = transaccion.contrato
            clase_planilla = contrato.clase_planilla
            fuente_financiamiento = contrato.fuente_financiamiento

            planilla, created = Planilla.objects.get_or_create(
                clase_planilla=clase_planilla,
                fuente_financiamiento=fuente_financiamiento,
                periodo_id=periodo,
                estado='APERTURADO',
                defaults={'correlativo': self.generate_correlativo(periodo)}
            )

            if transaccion.transaccion.tipo == 'HABER':
                planilla.total_haberes += transaccion.monto
            elif transaccion.transaccion.tipo == 'DESCUENTO':
                planilla.total_descuentos += transaccion.monto
            elif transaccion.transaccion.tipo == 'APORTE':
                planilla.total_aportes += transaccion.monto

            planilla.contratos.add(contrato)
            planilla.save()
            planillas_creadas.append(planilla)

        return Response({"message": "Planillas procesadas exitosamente.", "planillas": PlanillaSerializer(planillas_creadas, many=True).data}, status=status.HTTP_201_CREATED)

    def generate_correlativo(self, periodo):
        ultimo_correlativo = Planilla.objects.filter(periodo=periodo).aggregate(Max('correlativo'))['correlativo__max']
        if ultimo_correlativo:
            nuevo_correlativo = int(ultimo_correlativo) + 1
        else:
            nuevo_correlativo = 1
        return str(nuevo_correlativo).zfill(6)  # Asegura que el correlativo tenga 6 dígitos

class PlanillaViewSet(viewsets.ModelViewSet):
    queryset = Planilla.objects.all()
    serializer_class = PlanillaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin_sistema':
            return Planilla.objects.all()
        return Planilla.objects.filter(boletas__contrato__trabajador__ugel=user.ugel)

class BoletaViewSet(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin_sistema':
            return Boleta.objects.all()
        return Boleta.objects.filter(contrato__trabajador__ugel=user.ugel)