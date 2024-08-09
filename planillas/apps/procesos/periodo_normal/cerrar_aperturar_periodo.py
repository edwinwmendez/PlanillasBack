# apps/procesos/periodo_normal/cerrar_aperturar_periodo.py
from django.db import transaction, IntegrityError
from django.core.exceptions import ValidationError
from apps.configuracion.models import Periodo, ComisionAfp
from apps.planillas.models import Planilla, Contrato



class CerrarAperturarPeriodo:
    @staticmethod
    @transaction.atomic
    def cerrar_aperturar(nuevo_periodo, es_adicional):
        try:
            periodo_a_cerrar = Periodo.objects.get(estado=True)
        except Periodo.DoesNotExist:
            raise ValidationError("No hay un periodo activo para cerrar.")
        except Exception as e:
            raise ValidationError(f"Error inesperado al buscar el periodo activo: {str(e)}")

        periodo_a_cerrar_int = int(periodo_a_cerrar.periodo)
        nuevo_periodo_int = int(nuevo_periodo)

        if nuevo_periodo_int == periodo_a_cerrar_int:
            raise ValidationError(f"El nuevo periodo {nuevo_periodo} no puede ser igual que el periodo actual {periodo_a_cerrar.periodo}.")

        if es_adicional:
            periodo_adicional_esperado = periodo_a_cerrar_int + 20
            if not periodo_a_cerrar.es_adicional:
                if nuevo_periodo_int != periodo_adicional_esperado:
                    raise ValidationError(f"Para un periodo adicional, el nuevo periodo debe ser {periodo_adicional_esperado}")
            else:
                adicionales_existentes = Periodo.objects.filter(periodo__startswith=str(periodo_a_cerrar_int // 100)).count()
                if adicionales_existentes >= 5:
                    raise ValidationError("No se pueden crear más de cuatro periodos adicionales. Debes Aperturar un Periodo Normal.")
                if nuevo_periodo_int != periodo_adicional_esperado:
                    raise ValidationError(f"Para un periodo adicional, el nuevo periodo debe ser {periodo_adicional_esperado}")

        if periodo_a_cerrar.es_adicional:
            periodo_normal_anterior = Periodo.objects.filter(
                periodo__lt=periodo_a_cerrar_int,
                es_adicional=False
            ).order_by('-periodo').first()

            if not periodo_normal_anterior:
                raise ValidationError("No se encontró un periodo normal anterior.")

            periodo_normal_esperado = int(periodo_normal_anterior.periodo) + 1
        else:
            periodo_normal_esperado = periodo_a_cerrar_int + 1

        if nuevo_periodo_int != periodo_normal_esperado:
            raise ValidationError(f"El nuevo periodo normal debe ser {periodo_normal_esperado}")

        try:
            planillas_actuales = Planilla.objects.filter(periodo=periodo_a_cerrar, estado='APERTURADO')
            for planilla in planillas_actuales:
                planilla.estado = 'CERRADO'
                planilla.save()

            CerrarAperturarPeriodo.resetear_campos_contrato()

            periodo_a_cerrar.estado = False
            periodo_a_cerrar.save()

            nuevo_periodo = Periodo(
                periodo=str(nuevo_periodo),
                es_adicional=es_adicional,
                estado=True
            )
            nuevo_periodo.save()

            CerrarAperturarPeriodo.crear_nuevas_planillas(nuevo_periodo, planillas_actuales)
            CerrarAperturarPeriodo.copiar_comisiones_afp(periodo_a_cerrar, nuevo_periodo)

            return nuevo_periodo
        except IntegrityError as e:
            raise ValidationError(f"Error de integridad en la base de datos: {str(e)}")
        except ValidationError as e:
            raise ValidationError(f"Error de validación: {str(e)}")
        except Exception as e:
            raise ValidationError(f"Error inesperado: {str(e)}")

    @staticmethod
    def resetear_campos_contrato():
        try:
            Contrato.objects.update(
                dias_laborados=30,
                leyenda_permanente='',
            )
        except Exception as e:
            raise ValidationError(f"Error al resetear los campos del contrato: {str(e)}")

    @staticmethod
    def copiar_comisiones_afp(periodo_anterior, nuevo_periodo):
        try:
            # Desactivar comisiones anteriores
            ComisionAfp.objects.filter(periodo=periodo_anterior).update(estado=False)

            # Copiar comisiones del periodo anterior al nuevo periodo
            comisiones_anteriores = ComisionAfp.objects.filter(periodo=periodo_anterior)
            for comision in comisiones_anteriores:
                ComisionAfp.objects.create(
                    periodo=nuevo_periodo,
                    afp=comision.afp,
                    comision_flujo=comision.comision_flujo,
                    comision_mixta=comision.comision_mixta,
                    prima_seguro=comision.prima_seguro,
                    aporte_obligatorio=comision.aporte_obligatorio,
                    total_comision=comision.total_comision,
                    estado=True  # Nuevo campo añadido
                )
        except Exception as e:
            raise ValidationError(f"Error al copiar las comisiones de AFP: {str(e)}")

    @staticmethod
    @transaction.atomic
    def crear_nuevas_planillas(nuevo_periodo, planillas_anteriores):
        for planilla_anterior in planillas_anteriores:
            intentos = 0
            while intentos < 5:
                try:
                    correlativo = CerrarAperturarPeriodo.generar_correlativo(nuevo_periodo)
                    Planilla.objects.create(
                        correlativo=correlativo,
                        clase_planilla=planilla_anterior.clase_planilla,
                        fuente_financiamiento=planilla_anterior.fuente_financiamiento,
                        periodo=nuevo_periodo,
                        estado='APERTURADO'
                    )
                    break
                except IntegrityError:
                    intentos += 1
                    if intentos >= 5:
                        raise ValidationError("No se pudo crear una nueva planilla después de varios intentos debido a problemas de unicidad.")
                except ValidationError as e:
                    raise e
                except Exception as e:
                    raise ValidationError(f"Error al crear nuevas planillas: {str(e)}")

    @staticmethod
    def generar_correlativo(periodo):
        try:
            with transaction.atomic():
                ultimo_correlativo = Planilla.objects.filter(periodo=periodo).order_by('-correlativo').first()
                if ultimo_correlativo:
                    nuevo_correlativo = str(int(ultimo_correlativo.correlativo) + 1).zfill(3)
                else:
                    nuevo_correlativo = '001'
                return nuevo_correlativo
        except Exception as e:
            raise ValidationError(f"Error al generar el correlativo: {str(e)}")


    @staticmethod
    @transaction.atomic
    def revertir_cierre_apertura(nuevo_periodo):
        try:
            # Intentar encontrar el periodo recién creado
            periodo_recien_creado = Periodo.objects.filter(periodo=nuevo_periodo, estado=True).first()
            if not periodo_recien_creado:
                raise ValidationError("El nuevo periodo no existe o ya ha sido cerrado.")

            # Eliminar las planillas creadas para el nuevo periodo
            Planilla.objects.filter(periodo=periodo_recien_creado).delete()

            # Eliminar el nuevo periodo
            periodo_recien_creado.delete()

            # Restaurar el estado del periodo cerrado
            periodo_a_cerrar = Periodo.objects.filter(estado=False).order_by('-periodo').first()
            if periodo_a_cerrar:
                periodo_a_cerrar.estado = True
                periodo_a_cerrar.save()

            # Restaurar el estado de las planillas del periodo cerrado
            Planilla.objects.filter(periodo=periodo_a_cerrar).update(estado='APERTURADO')

            # Restaurar los campos de los contratos
            Contrato.objects.update(
                dias_laborados=30,
                leyenda_permanente='',
            )

            return "Reversión completada exitosamente."
        except Exception as e:
            raise ValidationError(f"Error al revertir el cierre y apertura de periodo: {str(e)}")   