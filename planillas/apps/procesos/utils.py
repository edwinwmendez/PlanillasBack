from django.db import transaction
from apps.planillas.models import Planilla, Contrato, Boleta

@transaction.atomic
def generar_boletas_para_planilla(planilla_id):
    # Obtener la planilla específica usando el ID de la planilla
    planilla = Planilla.objects.get(id=planilla_id)

    # Filtrar contratos que coincidan con la clase de planilla y la fuente de financiamiento de la planilla,
    # que el trabajador esté activo, y que no estén en situación de "Suspendido" o "Baja"
    contratos = Contrato.objects.filter(
        clase_planilla=planilla.clase_planilla,
        fuente_financiamiento=planilla.fuente_financiamiento,
        trabajador__estado=True
    ).exclude(situacion__nombre_situacion__in=['Suspendido', 'Baja'])

    # Iterar sobre los contratos filtrados
    for contrato in contratos:
        # Obtener o crear una boleta para el contrato y la planilla específicos
        boleta, created = Boleta.objects.get_or_create(
            contrato=contrato,
            planilla=planilla
        )
        # Si la boleta fue creada, guardar la boleta
        if created:
            boleta.save()
