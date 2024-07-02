from django.core.management.base import BaseCommand
from apps.procesos.utils import generar_boletas_para_planilla
from apps.planillas.models import Planilla

class Command(BaseCommand):
    help = 'Genera boletas para todos los trabajadores en una planilla específica'

    def add_arguments(self, parser):
        parser.add_argument('planilla_id', type=int, help='ID de la planilla para la cual generar boletas')

    def handle(self, *args, **kwargs):
        planilla_id = kwargs['planilla_id']
        try:
            generar_boletas_para_planilla(planilla_id)
            self.stdout.write(self.style.SUCCESS(f'Se han generado boletas para la planilla {planilla_id}'))
        except Planilla.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Planilla con ID {planilla_id} no existe'))
