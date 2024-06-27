# Sistema de Planillas

El proyecto que estoy creando es para un Sistema de Planilla de Remuneraciones (API REST para el Backend con Django), el cual tendrá varias tablas que te comento a continuación:

## Descripción del Proyecto

El Sistema de Planillas es una aplicación diseñada para gestionar las remuneraciones de los trabajadores de la UGEL y otras instituciones relacionadas. Este sistema permite a los administradores y técnicos registrar, gestionar y consultar datos de usuarios, trabajadores, transacciones de haberes y descuentos, generación de planillas y reportes, así como la gestión de beneficiarios.

## Requerimientos Funcionales

### Autenticación y Autorización

-   **RF-001**: El sistema debe permitir a los usuarios autenticarse mediante email o nombre de usuario y contraseña.
-   **RF-002**: El sistema debe permitir la recuperación de contraseña a través del email.
-   **RF-003**: El sistema debe permitir que solo los usuarios con roles de Administrador puedan acceder a la administración de usuarios.

### Gestión de Usuarios

-   **RF-004**: El sistema debe permitir al Administrador UGEL registrar nuevos usuarios.
-   **RF-005**: El sistema debe enviar un correo electrónico de confirmación al nuevo usuario después de registrarse.
-   **RF-006**: El sistema debe permitir al Administrador UGEL editar la información de los usuarios.
-   **RF-007**: El sistema debe permitir al Administrador UGEL eliminar usuarios del sistema.

### Gestión de Trabajadores

-   **RF-008**: El sistema debe permitir registrar nuevos trabajadores con datos personales, situación laboral, fecha de ingreso y cargo.
-   **RF-009**: El sistema debe permitir editar la información de los trabajadores.
-   **RF-010**: El sistema debe permitir eliminar registros de trabajadores.
-   **RF-011**: El sistema debe permitir asignar haberes y descuentos a los trabajadores.

### Gestión de Transacciones

-   **RF-012**: El sistema debe permitir registrar haberes y descuentos en la base de datos.
-   **RF-013**: El sistema debe permitir editar la información de los haberes y descuentos.
-   **RF-014**: El sistema debe permitir eliminar haberes y descuentos del sistema.

### Generación y Consulta de Planillas

-   **RF-015**: El sistema debe permitir generar planillas de remuneraciones para un período seleccionado.
-   **RF-016**: El sistema debe calcular las remuneraciones de cada trabajador basado en sus haberes y descuentos.
-   **RF-017**: El sistema debe permitir a los trabajadores consultar los detalles de sus remuneraciones por período.
-   **RF-018**: El sistema debe permitir a los trabajadores descargar sus boletas de pago en formato PDF.

### Gestión de Beneficiarios

-   **RF-019**: El sistema debe permitir registrar beneficiarios asociados a un trabajador.
-   **RF-020**: El sistema debe permitir editar la información de los beneficiarios.
-   **RF-021**: El sistema debe permitir eliminar beneficiarios del sistema.

### Reportes

-   **RF-022**: El sistema debe permitir generar reportes de planillas basados en criterios seleccionados por el usuario.
-   **RF-023**: El sistema debe permitir descargar reportes en formatos PDF y Excel.

## Requerimientos No Funcionales

### Seguridad

-   **RNF-001**: El sistema debe asegurar la transmisión de datos utilizando HTTPS.
-   **RNF-002**: El sistema debe almacenar las contraseñas de los usuarios de manera segura utilizando algoritmos de hash.
-   **RNF-003**: El sistema debe implementar control de acceso basado en roles para proteger los recursos sensibles.
-   **RNF-004**: El sistema debe enviar un correo electrónico de confirmación al nuevo usuario después de registrarse.

### Rendimiento

-   **RNF-005**: El sistema debe responder a las consultas de datos en menos de 2 segundos bajo carga normal.
-   **RNF-006**: El sistema debe ser capaz de manejar al menos 500 usuarios concurrentes sin degradación significativa del rendimiento.

### Usabilidad

-   **RNF-007**: El sistema debe ser accesible desde dispositivos móviles y de escritorio.
-   **RNF-008**: El sistema debe tener una interfaz de usuario intuitiva y fácil de usar.

### Mantenibilidad

-   **RNF-009**: El sistema debe estar diseñado siguiendo principios de código limpio y modular para facilitar su mantenimiento.
-   **RNF-010**: El sistema debe contar con una suite de pruebas automatizadas para garantizar la calidad del código.

### Escalabilidad

-   **RNF-011**: El sistema debe ser escalable horizontalmente para soportar el crecimiento en el número de usuarios y transacciones.
-   **RNF-012**: El sistema debe permitir la adición de nuevos módulos y funcionalidades sin afectar los módulos existentes.

### Compatibilidad

-   **RNF-013**: El sistema debe ser compatible con las versiones más recientes de los navegadores web más utilizados (Chrome, Firefox, Safari, Edge).
-   **RNF-014**: El sistema debe ser compatible con bases de datos PostgreSQL y MySQL.

### Disponibilidad

-   **RNF-015**: El sistema debe estar disponible al menos el 99.5% del tiempo durante el horario laboral.
-   **RNF-016**: El sistema debe incluir mecanismos de respaldo y recuperación ante desastres para garantizar la disponibilidad de los datos.

## Requerimientos de Implementación

-   **RI-001**: El sistema debe ser desarrollado utilizando Django y Django REST Framework para el backend.
-   **RI-002**: El frontend debe ser desarrollado utilizando Vue.js y Vite.
-   **RI-003**: El sistema debe utilizar PostgreSQL como base de datos principal.
-   **RI-004**: El sistema debe ser desplegado en un entorno de contenedores utilizando Docker.
-   **RI-005**: El sistema debe incluir documentación detallada para desarrolladores y usuarios finales.
-   **RI-006**: El sistema debe implementar un pipeline de CI/CD para facilitar la integración y el despliegue continuo.

## Casos de Uso

### Caso de Uso 1: Iniciar sesión en el sistema

**Título:** **Iniciar sesión en el sistema**

**Actores:** Administrador del Sistema, Administrador UGEL, Técnico de Procesos, Técnico de Planillas, Trabajadores

**Precondiciones:**

-   El usuario debe estar registrado en el sistema.

**Flujo Principal:**

1. El usuario navega a la página de inicio de sesión.
2. El usuario ingresa su correo electrónico y contraseña.
3. El usuario envía el formulario de inicio de sesión.
4. El sistema valida las credenciales.
5. El sistema autentica al usuario y lo redirige a la página principal.

**Flujo Alternativo:**
4a. Si las credenciales son incorrectas, el sistema muestra un mensaje de error y solicita al usuario que intente nuevamente.

**Postcondiciones:**

-   El usuario está autenticado y puede acceder a las funcionalidades del sistema.

### Caso de Uso 2: Registrar nuevo Usuario

**Título:** **Registrar nuevo Usuario**

**Actores:** Administrador UGEL

**Precondiciones:**

-   El Administrador UGEL debe estar autenticado.

**Flujo Principal:**

1. El Administrador UGEL navega a la página de registro de usuarios.
2. El Administrador UGEL completa el formulario de registro con la información del nuevo usuario.
3. El Administrador UGEL envía el formulario.
4. El sistema valida los datos ingresados.
5. El sistema crea un nuevo registro de usuario en la base de datos.
6. El sistema envía un correo electrónico de confirmación al nuevo usuario.

**Flujo Alternativo:**
4a. Si los datos son inválidos o el correo electrónico ya está en uso, el sistema muestra un mensaje de error y solicita al Administrador UGEL que corrija los datos.

**Postcondiciones:**

-   El nuevo usuario está registrado en el sistema y puede iniciar sesión.

### Caso de Uso 3: Registrar nuevo trabajador

**Título:** **Registrar nuevo trabajador**

**Actores:** Administrador del Sistema, Técnico de Planillas

**Precondiciones:**

-   El actor debe estar autenticado.

**Flujo Principal:**

1. El actor navega a la página de registro de trabajadores.
2. El actor completa el formulario con la información del trabajador, incluyendo datos personales, situación laboral, fecha de ingreso, y cargo.
3. El actor envía el formulario.
4. El sistema valida los datos ingresados.
5. El sistema crea un nuevo registro de trabajador en la base de datos.

**Flujo Alternativo:**
4a. Si los datos son inválidos, el sistema muestra un mensaje de error y solicita al actor que corrija los datos.

**Postcondiciones:**

-   El trabajador está registrado en el sistema y se le puede asignar haberes y descuentos.

### Caso de Uso 4: Consultar detalle de remuneraciones

**Título:** **Consultar detalle de remuneraciones**

**Actores:** Trabajadores

**Precondiciones:**

-   El trabajador debe estar autenticado.
-   La planilla debe estar generada para el período seleccionado.

**Flujo Principal:**

1. El trabajador navega a la página de consulta de remuneraciones.
2. El trabajador selecciona el período que desea revisar.
3. El sistema muestra los detalles de la remuneración, incluyendo haberes, descuentos y el total neto.

**Flujo Alternativo:**
3a. Si no hay planilla generada para el período seleccionado, el sistema muestra un mensaje informando al trabajador.

**Postcondiciones:**

-   El trabajador puede visualizar los detalles de su remuneración para el período seleccionado.

### Caso de Uso 5: Gestionar Transacciones - Haberes y descuentos

**Título:** **Gestionar Transacciones - Haberes y descuentos**

**Actores:** Administrador del Sistema

**Precondiciones:**

-   El Administrador del Sistema debe estar autenticado.

**Flujo Principal:**

1. El Administrador del Sistema navega a la página de gestión de transacciones.
2. El Administrador del Sistema completa el formulario con la información del haber o descuento.
3. El Administrador del Sistema envía el formulario.
4. El sistema valida los datos ingresados.
5. El sistema crea un nuevo registro de transacción en la base de datos.

**Flujo Alternativo:**
4a. Si los datos son inválidos, el sistema muestra un mensaje de error y solicita al Administrador del Sistema que corrija los datos.

**Postcondiciones:**

-   El haber o descuento está registrado en el sistema y puede ser asignado a los trabajadores.

### Caso de Uso 6: Asignación de Haberes y Descuentos a cada trabajador

**Título:** **Asignación de Haberes y Descuentos a cada trabajador**

**Actores:** Administrador del Sistema, Técnico de Planillas

**Precondiciones:**

-   El actor debe estar autenticado.
-   El trabajador debe estar registrado en el sistema.

**Flujo Principal:**

1. El actor navega a la página de asignación de haberes y descuentos.
2. El actor selecciona un trabajador de la lista.
3. El actor selecciona los haberes y descuentos aplicables para el trabajador.
4. El actor especifica los montos y períodos correspondientes.
5. El actor envía el formulario.
6. El sistema valida los datos ingresados.
7. El sistema crea registros de transacciones para los haberes y descuentos en la base de datos.

**Flujo Alternativo:**
6a. Si los datos son inválidos, el sistema muestra un mensaje de error y solicita al actor que corrija los datos.

**Postcondiciones:**

-   Los haberes y descuentos están asignados al trabajador para los períodos especificados.

### Caso de Uso 7: Generación de Planillas

**Título:** **Generación de Planillas**

**Actores:** Administrador del Sistema, Técnico de Procesos

**Precondiciones:**

-   El actor debe estar autenticado.
-   Todos los trabajadores deben tener asignados haberes y descuentos para el período.

**Flujo Principal:**

1. El actor navega a la página de generación de planillas.
2. El actor selecciona el período para el cual desea generar la planilla.
3. El actor inicia el proceso de generación de planilla.
4. El sistema calcula las remuneraciones de cada trabajador basado en sus haberes y descuentos.
5. El sistema genera la planilla y la guarda en la base de datos.
6. El sistema muestra un resumen de la planilla generada.

**Flujo Alternativo:**
4a. Si hay errores en los datos de los trabajadores, el sistema muestra un mensaje de error y detiene el proceso.

**Postcondiciones:**

-   La planilla está generada y disponible para su revisión y aprobación.

### Caso de Uso 8: Generar Reporte de Planillas

**Título:** **Generar Reporte de Planillas**

**Actores:** Administrador del Sistema, Técnico de Procesos

**Precondiciones:**

-   El actor debe estar autenticado.
-   Debe existir al menos una planilla generada.

**Flujo Principal:**

1. El actor navega a la página de reportes de planillas.
2. El actor selecciona el período y los criterios del reporte.
3. El actor solicita la generación del reporte.
4. El sistema genera el reporte basado en los criterios seleccionados.
5. El sistema muestra el reporte generado y proporciona opciones para descargarlo.

**Flujo Alternativo:**
4a. Si no existen datos para los criterios seleccionados, el sistema muestra un mensaje informando al actor.

**Postcondiciones:**

-   El actor obtiene el reporte de planillas generado.

### Caso de Uso 9: Registrar Beneficiarios

**Título:** **Registrar Beneficiarios**

**Actores:** Administrador del Sistema, Técnico de Planillas

**Precondiciones:**

-   El actor debe estar autenticado.
-   El trabajador debe estar registrado en el sistema.

**Flujo Principal:**

1. El actor navega a la página de registro de beneficiarios.
2. El actor completa el formulario con la información del beneficiario, incluyendo tipo de beneficiario, relación con el trabajador, y detalles del descuento.
3. El actor envía el formulario.
4. El sistema valida los datos ingresados.
5. El sistema crea un nuevo registro de beneficiario en la base de datos.
6. El sistema asocia el beneficiario con el trabajador y registra el descuento correspondiente.

**Flujo Alternativo:**
4a. Si los datos son inválidos, el sistema muestra un mensaje de error y solicita al actor que corrija los datos.

**Postcondiciones:**

-   El beneficiario está registrado en el sistema y asociado al trabajador con el descuento correspondiente.

### Caso de Uso 10: Visualización de Planilla por trabajador "Boletas de pago"

**Título:** **Visualización de Planilla por trabajador "Boletas de pago"**

**Actores:** Técnico de Planillas, Trabajadores

**Precondiciones:**

-   El actor debe estar autenticado.
-   La planilla debe estar generada para el período seleccionado.

**Flujo Principal:**

1. El actor navega a la página de visualización de boletas de pago.
2. El actor selecciona el trabajador y el período que desea revisar.
3. El sistema muestra los detalles de la boleta de pago del trabajador, incluyendo haberes, descuentos y el total neto.

**Flujo Alternativo:**
3a. Si no hay planilla generada para el período seleccionado, el sistema muestra un mensaje informando al actor.

**Postcondiciones:**

-   El actor puede visualizar los detalles de la boleta de pago del trabajador para el período seleccionado.

### Caso de Uso 11: Ver detalle de pagos por periodo

**Título:** **Ver detalle de pagos por periodo**

**Actores:** Trabajadores

**Precondiciones:**

-   El trabajador debe estar autenticado.
-   La planilla debe estar generada para el período seleccionado.

**Flujo Principal:**

1. El trabajador navega a la página de detalle de pagos por período.
2. El trabajador selecciona el período que desea revisar.
3. El sistema muestra los detalles de los pagos del trabajador para el período seleccionado.

**Flujo Alternativo:**
3a. Si no hay planilla generada para el período seleccionado, el sistema muestra un mensaje informando al trabajador.

**Postcondiciones:**

-   El trabajador puede visualizar los detalles de sus pagos para el período seleccionado.

### Caso de Uso 12: Descargar Boletas de pago

**Título:** **Descargar Boletas de pago**

**Actores:** Trabajadores

**Precondiciones:**

-   El trabajador debe estar autenticado.
-   La planilla debe estar generada para el período seleccionado.

**Flujo Principal:**

1. El trabajador navega a la página de descarga de boletas de pago.
2. El trabajador selecciona el período que desea descargar.
3. El sistema genera un archivo PDF con la boleta de pago del trabajador.
4. El trabajador descarga el archivo PDF.

**Flujo Alternativo:**
3a. Si no hay planilla generada para el período seleccionado, el sistema muestra un mensaje informando al trabajador.

**Postcondiciones:**

-   El trabajador obtiene la boleta de pago en formato PDF para el período seleccionado.

### Caso de Uso 13: Descargar Boletas de pago por periodo

**Título:** **Descargar Boletas de pago por periodo**

**Actores:** Administrador del Sistema, Técnico de Planillas

**Precondiciones:**

-   El actor debe estar autenticado.
-   La planilla debe estar generada para el período seleccionado.

**Flujo Principal:**

1. El actor navega a la página de descarga de boletas de pago por período.
2. El actor selecciona el período y el régimen laboral que desea descargar.
3. El sistema genera un archivo comprimido con las boletas de pago de todos los trabajadores para el período y régimen laboral seleccionados.
4. El actor descarga el archivo comprimido.

**Flujo Alternativo:**
3a. Si no hay planilla generada para el período seleccionado, el sistema muestra un mensaje informando al actor.

**Postcondiciones:**

-   El actor obtiene las boletas de pago en un archivo comprimido para el período y régimen laboral seleccionados.

### Caso de Uso 14: Descargar boletas de pago único de trabajadores

**Título:** **Descargar boletas de pago único de trabajadores**

**Actores:** Administrador del Sistema, Técnico de Planillas

**Precondiciones:**

-   El actor debe estar autenticado.
-   La planilla debe estar generada para el período seleccionado.

**Flujo Principal:**

1. El actor navega a la página de descarga de boletas de pago único.
2. El actor selecciona el trabajador y el período que desea descargar.
3. El sistema genera un archivo PDF con la boleta de pago del trabajador.
4. El actor descarga el archivo PDF.

**Flujo Alternativo:**
3a. Si no hay planilla generada para el período seleccionado, el sistema muestra un mensaje informando al actor.

**Postcondiciones:**

-   El actor obtiene la boleta de pago en formato PDF para el trabajador y período seleccionados.

### Caso de Uso 15: Actualización de Comisión AFP

**Título:** **Actualización de Comisión AFP**

**Actores:** Administrador del Sistema

**Precondiciones:**

-   El Administrador del Sistema debe estar autenticado.

**Flujo Principal:**

1. El Administrador del Sistema navega a la página de gestión de comisiones AFP.
2. El Administrador del Sistema selecciona la AFP que desea actualizar.
3. El Administrador del Sistema completa el formulario con los nuevos porcentajes de comisión.
4. El Administrador del Sistema envía el formulario.
5. El sistema valida los datos ingresados.
6. El sistema actualiza la comisión de la AFP en la base de datos.

**Flujo Alternativo:**
5a. Si los datos son inválidos, el sistema muestra un mensaje de error y solicita al Administrador del Sistema que corrija los datos.

**Postcondiciones:**

-   La comisión de la AFP está actualizada en el sistema.

---

## Esquema de base de datos

### Usuario:

Esta tabla servirá para que cada persona pueda ingresar al sistema, desde el administrador hasta los propios trabajadores y heredara de AbstractUser. Vamos a tener El usuario Administrador, Técnico de Planillas, Consulta y el Trabajador(Mas adelante se agregaran mas usuarios si es necesario):

```python
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
```

### Persona:

Donde se colocaran los datos personales de todos los usuarios y trabajadores, los campos que se tendrán son:

```python
class Persona(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True,
        related_name='persona'
    )

    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'DNI'),
        ('CET', 'Carnet de extranjería'),
        ('PAS', 'Pasaporte')
    ]

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]

    tipo_documento = models.CharField(
        max_length=20,
        choices=TIPO_DOCUMENTO_CHOICES,
        default='DNI',
        verbose_name='Tipo de Documento'
    )
    numero_documento = models.CharField(
        max_length=8, unique=True, db_index=True,
        verbose_name='Número de Documento'
    )
    paterno = models.CharField(
        max_length=45, blank=True, verbose_name='Apellido Paterno')
    materno = models.CharField(
        max_length=45, blank=True, verbose_name='Apellido Materno')
    nombres = models.CharField(
        max_length=45, blank=True, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(
        max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')
    direccion = models.CharField(
        max_length=100, blank=True, verbose_name='Dirección')
    email = models.EmailField(max_length=45, blank=True, verbose_name='Email')

    def __str__(self):
        return f'{self.nombres} {self.paterno} {self.materno}'

    def get_full_name(self):
        return f'{self.nombres} {self.paterno} {self.materno}'.strip()

    def clean(self):
        if self.tipo_documento == 'DNI' and len(self.numero_documento) != 8:
            raise ValidationError(_('El DNI debe tener 8 caracteres.'))
        elif self.tipo_documento == 'CET' and len(self.numero_documento) != 9:
            raise ValidationError(_('El Carnet de extranjería debe tener 9 caracteres.'))
        elif self.tipo_documento == 'PAS' and len(self.numero_documento) != 12:
            raise ValidationError(_('El pasaporte debe tener 12 caracteres.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'persona'
        ordering = ['paterno', 'materno', 'nombres']
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


```

### Trabajador:

Esta tabla servira para registrar a todos nuestros trabajadores, y se tomaran los datos personales de la tabla persona, sus campos son:

```python
class Trabajador(models.Model):
    SITUACION_CHOICES = [
        ('HAB', 'Habilitado'),
        ('LSG', 'Licencia sin goce'),
        ('LCG', 'Licencia con goce'),
        ('DES', 'Desabilitado'),
        ('VAC', 'Vacaciones')
    ]
    ugel = models.ForeignKey(
        configuration.Ugel, on_delete=models.CASCADE, verbose_name='UGEL')
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    situacion = models.CharField(
        max_length=20, null=True, default='HAB', choices=SITUACION_CHOICES,
        verbose_name='Situación'
    )
    dias_licencia = models.IntegerField(
        null=True, blank=True, verbose_name='Días de Licencia', default=0)
    fecha_ini_licencia = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Inicio de Licencia')
    tiempo_servicios = models.CharField(
        max_length=6, blank=True, verbose_name='Tiempo de Servicios')
    dias_laborados = models.IntegerField(
        null=True, blank=True, verbose_name='Días Laborados', default=30)
    cargo = models.ForeignKey(
        configuration.Cargo, on_delete=models.CASCADE, verbose_name='Cargo', related_name='empleados')
    fecha_ingreso = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Ingreso')
    fecha_cese = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Cese')
    documento_contrato = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Contrato')
    documento_cese = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Cese')
    regimen_laboral = models.ForeignKey(
        configuration.RegimenLaboral, on_delete=models.CASCADE, verbose_name='Régimen Laboral'
    )
    tipo_servidor = models.ForeignKey(
        configuration.TipoServidor, on_delete=models.CASCADE, verbose_name='Tipo de Servidor')
    regimen_pensionario = models.ForeignKey(
        configuration.RegimenPensionario, on_delete=models.CASCADE, verbose_name='Régimen Pensionario'
    )
    afp = models.ForeignKey(configuration.AFP, on_delete=models.CASCADE, verbose_name='AFP')
    cuspp = models.CharField(max_length=12, blank=True, verbose_name='CUSPP')
    fecha_afiliacion = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Afiliación')
    fecha_devengue = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Devengue')
    codigo_nexus = models.CharField(
        max_length=10, blank=True, verbose_name='Código Nexus')
    jornada_laboral = models.IntegerField(
        null=True, blank=True, verbose_name='Jornada Laboral')
    descuentos_dias = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Días', default=0)
    descuentos_horas = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Horas', default=0)
    descuentos_minutos = models.IntegerField(
        null=True, blank=True, verbose_name='Descuentos en Minutos', default=0)
    leyenda_permanente = models.CharField(
        max_length=45, blank=True, verbose_name='Leyenda Permanente')
    leyenda_mensual = models.CharField(
        max_length=45, blank=True, verbose_name='Leyenda Mensual')
    banco = models.ForeignKey(
        configuration.Banco, on_delete=models.CASCADE, verbose_name='Banco')
    numero_cuenta = models.CharField(
        max_length=45, blank=True, verbose_name='Número de Cuenta')
    ruc = models.CharField(max_length=11, blank=True, verbose_name='RUC')

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno} - {self.cargo.nombre_cargo} - {self.fecha_ingreso} - {self.fecha_cese}'

    class Meta:
        db_table = 'empleado'
        ordering = ['id']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        indexes = [
            models.Index(fields=['situacion'], name='situacion_idx'),
            models.Index(fields=['fecha_ingreso'], name='fecha_ingreso_idx'),
            models.Index(fields=['fecha_cese'], name='fecha_cese_idx'),
```

### Transaccion:

Que permitirá registrar todos los haberes y descuentos que existen, estas transacciones se registran de la tabla nacional de haberes que tienen todos los trabajadores de estado, Luego desde acá se tomaran los haberes de cada trabajador. Esta es la base de haberes. Los campos que tenemos son:

```python
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('HABER', 'Haber'),
        ('DESCUENTO', 'Descuento')
    ]
    CATEGORIA_CHOICES = [
        ('SUELDO', 'Sueldo'),
        ('BONIFICACION', 'Bonificación'),
        ('DEDUCCION', 'Deducción'),
        ('BENEFICIOS_SOCIALES', 'Beneficios Sociales'),
        ('APORTE', 'Aporte'),
        ('OTRO', 'Otro')
    ]

    tipo = models.CharField(
        max_length=10, choices=TIPO_CHOICES, verbose_name='Tipo', default='HABER'
    )
    categoria = models.CharField(
        max_length=20, choices=CATEGORIA_CHOICES, verbose_name='Categoría'
    )
    codigo = models.CharField(
        max_length=4, unique=True, verbose_name='Código', help_text='Código de Transacción'
    )
    descripcion = models.CharField(
        max_length=45, verbose_name='Descripción'
    )

    def clean(self):
        if self.tipo == 'HABER' and self.categoria not in ['SUELDO', 'BONIFICACION', 'BENEFICIOS_SOCIALES', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Haber.'))
        if self.tipo == 'DESCUENTO' and self.categoria not in ['DEDUCCION', 'APORTE', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Descuento.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'transaccion'
        ordering = ['descripcion']
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'

```

### Periodo:

Sirve para registrar todos los periodos en el que se están trabajando las planillas, por ejemplo, en el mes de enero se apresurara la planilla 202401, para febrero será la planilla 202402, si es adicional se sumara 20, ejemplo, para adicional de febrero será 202422, para junio será 202426. Con esta tabla podremos tener registrados todos los haberes y descuentos de nuestros trabajadores organizados por periodos laborales o periodos de pagos. Sus campos son:

```python
class Periodo(models.Model):
    mes = models.CharField(max_length=2, blank=True, verbose_name='Mes')
    anio = models.CharField(max_length=4, blank=True, verbose_name='Año')
    periodo = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo', editable=False)
    es_adicional = models.BooleanField(
        default=False, verbose_name='¿Es adicional?')
    periodo_actual = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Actual', editable=False, null=True, default=None)

    def __str__(self):
        return f'{self.periodo} - {self.mes}/{self.anio}'

    def clean(self):
        if not self.periodo:
            self.periodo = f'{self.anio}{self.mes}'
        if not self.es_adicional and Periodo.objects.filter(mes=self.mes, anio=self.anio, es_adicional=False).exists():
            raise ValidationError('Ya existe un período principal para este mes y año.')


    def save(self, *args, **kwargs):
        self.clean()
        if not self.periodo:
            # Generar el valor del campo periodo a partir de mes y anio
            self.periodo = f'{self.anio}{self.mes}'

        if not self.es_adicional:
            # Actualizar el campo periodo_actual con el valor del último período principal
            last_principal_periodo = Periodo.objects.filter(
                es_adicional=False).order_by('-id').first()
            self.periodo_actual = last_principal_periodo.periodo if last_principal_periodo else None
            print(last_principal_periodo)

        # Validar si ya existe un periodo principal con la misma combinación de mes y año
        if not self.es_adicional and Periodo.objects.filter(mes=self.mes, anio=self.anio, es_adicional=False).exists():
            raise ValidationError(
                'Ya existe un período principal para este mes y año.')

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'periodo'
        ordering = ['anio', 'mes']
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'

```

### TransaccionTrabajador:

Sirve para designar que haber o descuento le corresponde a cada trabajador de acuerdo al periodo de las planillas, por ejemplo, si un trabajador es contratado de marzo a diciembre, su periodo será esas mismas fechas. Los campos son:

```python
class TransaccionTrabajador(models.Model):
    trabajador = models.ForeignKey(
        Trabajador, on_delete=models.CASCADE, verbose_name='Trabajador', related_name='transacciones', null=True, blank=True
    )
    transaccion = models.ForeignKey(
        Transaccion, on_delete=models.CASCADE, verbose_name='Transacción'
    )
    monto = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto'
    )
    periodo_inicial = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Inicial'
    )
    periodo_final = models.CharField(
        max_length=6, blank=True, verbose_name='Periodo Final'
    )
    correlativo = models.IntegerField(
        verbose_name='Correlativo', editable=False, null=True, blank=True
    )
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return f'{self.correlativo} - {self.trabajador} - {self.transaccion.descripcion} - {self.monto}'

    class Meta:
        db_table = 'transacciones_trabajadores'
        verbose_name = 'Transacción del Trabajador'
        verbose_name_plural = 'Transacciones de los Trabajadores'
        ordering = ['transaccion', 'correlativo']

    def save(self, *args, **kwargs):
        if not self.pk:
            ultimo_correlativo = TransaccionTrabajador.objects.filter(transaccion=self.transaccion).aggregate(Max('correlativo'))['correlativo__max']
            self.correlativo = (ultimo_correlativo or 0) + 1
        super().save(*args, **kwargs)

```

### Beneficiario:

Esta tabla sirve para registrar Beneficiarios de trabajadores, quiero decir, se pueden registrar judiciales, tutores entre otros tipos de beneficiarios para que al profesor se le descuente un monto fijo o un valor porcentual de su sueldo y luego sea depositado en la cuenta del beneficiario. Al agregar a un beneficiario, se registrara un descuento para el trabajador en la tabla 'DescuentoTrabajador'. Sus campos son:

```python
class Beneficiario(models.Model):
    TIPO_BENEFICIARIO_CHOICES = [
        ('JUDICIAL', 'Judicial'),
        ('TUTOR', 'Tutor'),
    ]

    empleado = models.ForeignKey(
        Trabajador, on_delete=models.CASCADE, verbose_name='Empleado', related_name='beneficiarios'
    )
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona'
    )
    relacion_trabajador = models.CharField(
        max_length=45, blank=True, verbose_name='Relación del Trabajador'
    )
    documento_descuento = models.CharField(
        max_length=45, blank=True, verbose_name='Documento de Descuento'
    )
    numero_cuenta = models.CharField(
        max_length=11, blank=True, verbose_name='Número de Cuenta'
    )
    tipo_beneficiario = models.CharField(
        max_length=10, choices=TIPO_BENEFICIARIO_CHOICES, default='JUDICIAL', verbose_name='Tipo de Beneficiario'
    )

    TIPO_DESCUENTO_CHOICES = [
        ('MF', 'Monto Fijo'),
        ('DP', 'Descuento Porcentual')
    ]

    tipo_descuento = models.CharField(
        max_length=2, choices=TIPO_DESCUENTO_CHOICES, default='MF', verbose_name='Tipo de Descuento'
    )
    descuento_fijo = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Descuento Fijo'
    )
    porcentaje_descuento = models.IntegerField(
        null=True, blank=True, verbose_name='Porcentaje de Descuento'
    )
    fecha_inicio = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Inicio'
    )
    fecha_fin = models.DateField(
        null=True, blank=True, verbose_name='Fecha de Fin'
    )
    estado = models.BooleanField(
        verbose_name='Estado', default=True, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    banco = models.ForeignKey(
        configuration.Banco, on_delete=models.CASCADE, verbose_name='Banco'
    )

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno}'

    class Meta:
        db_table = 'beneficiario'
        ordering = ['id']
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'

    def clean(self):
        if self.tipo_descuento == 'MF' and not self.descuento_fijo:
            raise ValidationError('Debe especificar un monto fijo para el descuento.')
        if self.tipo_descuento == 'DP' and not self.porcentaje_descuento:
            raise ValidationError('Debe especificar un porcentaje para el descuento.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

```

### PlanillaTrabajador:

Esta tabla estoy pensando registrar todos los detalles de la remuneracion de cada trabajador, sean todos los haberes y descuentos asi como los pagos de essalud(q no esta siendo descontado del trabajador). Esta tabla servirá para que cuando el trabajador inicie sesión y quiera ver el detalle de sus pagos, pueda revisar sin problemas, ademas, el trabajador podrá seleccionar el periodo del q quiere revisar el detalle de su remuneracion. Sus campos son:

```python
class PlanillaTrabajador(models.Model):
    total_haberes = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total de Haberes'
    )
    total_descuentos = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total de Descuentos'
    )
    essalud = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='ESSALUD'
    )
    emitio_boleta = models.SmallIntegerField(
        null=True, blank=True, verbose_name='Emisión de Boleta')
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE,verbose_name='Trabajador', related_name='remuneraciones', null=True, blank=True)
    tipo_planilla = models.ForeignKey(
        configuration.TipoPlanilla, on_delete=models.CASCADE, verbose_name='Tipo de Planilla')
    periodo = models.ForeignKey(
        configuration.Periodo, on_delete=models.CASCADE, verbose_name='Período')
    ugel = models.ForeignKey(
        configuration.Ugel, on_delete=models.CASCADE, verbose_name='UGEL')

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno} - {self.periodo}'

    class Meta:
        db_table = 'planilla_trabajador'
        ordering = ['id']
        verbose_name = 'Planilla del Trabajador'
        verbose_name_plural = 'Planillas de los Trabajadores'
```

### PlanillaBeneficiario:

Permite registrar el detalle de la planilla de los beneficiarios, ellos también tendrán acceso al sistema para q puedan revisar el detalle de sus pagos por concepto de descuento a los titulares. Los campos que estoy pensando por mientras son:

```python
class PlanillaBeneficiario(models.Model):
    beneficiario = models.ForeignKey( Beneficiario, on_delete=models.CASCADE, verbose_name='Beneficiario')
    periodo = models.ForeignKey(configuration.Periodo, on_delete=models.CASCADE, verbose_name='Período')
    monto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto')

    def __str__(self):
        return f'{self.beneficiario.persona.nombres} {self.beneficiario.persona.paterno} {self.beneficiario.persona.materno} - {self.periodo}'

    class Meta:
        db_table = 'planilla_beneficiario'
        ordering = ['id']
        verbose_name = 'Planilla del Beneficiario'
        verbose_name_plural = 'Planillas de los Beneficiarios'
```

### UGEL:

En esta tabla se registraran las diferentes UGELes que quieran usar el sistema (si asi lo desean). Los campos actuales son:

```python
class Ugel(models.Model):
    nombre_ugel = models.CharField(
        max_length=100, verbose_name='Nombre de Ugel')
    nombre_corto = models.CharField(
        max_length=25, verbose_name='Nombre Corto', null=True, blank=True)

    def __str__(self):
        return self.nombre_corto

    class Meta:
        db_table = 'ugel'
        ordering = ['nombre_ugel']
        verbose_name = 'UGEL'
        verbose_name_plural = 'UGELs'
```

### Cargo:

Se almacenaran todos los cargos disponibles de todos nuestros trabajadores(Todavía no estoy seguro si acá debo agregar los montos para cada cargo). sus campos actuales son:

```python
class Cargo(models.Model):
    nombre_cargo = models.CharField(
        max_length=45, verbose_name='Nombre de Cargo')

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'cargo'
        ordering = ['nombre_cargo']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
```

### RegimenLaboral:

Agregaremos todos los regímenes laborales que tenemos en nuestro país. Creo que se debería considerar cada 'Haber' debe estar relacionada a un Regimen Laboral. Ya que por ejemplo, el Haber "135: Remuneracion CAS" debe estar asociado al Regimen Laboral "DL 1057 - CAS" eso para ordenar un poco. Por ahora, mis campos actuales son:

```python
class RegimenLaboral(models.Model):
    nombre_regimen_laboral = models.CharField(
        max_length=45, verbose_name='Nombre de Régimen Laboral')

    def __str__(self):
        return self.nombre_regimen_laboral

    class Meta:
        db_table = 'regimen_laboral'
        ordering = ['nombre_regimen_laboral']
        verbose_name = 'Régimen Laboral'
        verbose_name_plural = 'Regímenes Laborales'
```

### TipoServidor

En esta tabla se almacenaran todos los tipos de servidores, tendremos servidores nombrados que pertenecen a los Regímenes laborales de "DL 276 - Personal Administrativo" o al regimen laboral "Ley 29944 - Ley de la Reforma Magisterial". Un "DL 1057 - CAS" no tiene trabajadores nombrados, mas bien tiene Permanentes, te paso un cuadro de quienes pueden estar en qué regimen laboral:

| Regimen Laboral                            | Tipo Servidor                       |
| ------------------------------------------ | ----------------------------------- |
| "DL 1057 - CAS"                            | Contratado y Permanentes            |
| Ley 29944 - Ley de la Reforma Magisterial" | Contratados y Nombrados             |
| "DL 276 - Personal Administrativo"         | Contratados, Nombrados y Designados |

Los campos actuales son:

```python
class TipoServidor(models.Model):
    nombre_tipo_servidor = models.CharField(
        max_length=45, verbose_name='Nombre de Tipo de Servidor')

    def __str__(self):
        return self.nombre_tipo_servidor

    class Meta:
        db_table = 'tipo_servidor'
        ordering = ['nombre_tipo_servidor']
        verbose_name = 'Tipo de Servidor'
        verbose_name_plural = 'Tipos de Servidores'
```

### RegimenPensionario:

En el país solo tenemos dos Regímenes pensionario, "AFP(SPP) y ONP(SNP)", antiguamente existía un tercero que era el "DL 20530" que ya no existe. Esta tabla registra esos regímenes, quizá pienses que crear una tabla para dos registros no sea buena idea pero yo si lo creo. Sus campos Actuales son:

```python
class RegimenPensionario(models.Model):
    nombre_regimen_pensionario = models.CharField(
        max_length=45, verbose_name='Nombre de Régimen Pensionario')

    def __str__(self):
        return self.nombre_regimen_pensionario

    class Meta:
        db_table = 'regimen_pensionario'
        ordering = ['nombre_regimen_pensionario']
        verbose_name = 'Régimen Pensionario'
        verbose_name_plural = 'Regímenes Pensionarios'
```

_Asimismo, el regimen AFP tiene otros 8 tipos de AFP, cada uno con sus respectivos porcentajes de descuento al trabajador, no se si sea buena idea agregar en esta misma tabla esos 8 AFP con sus porcentajes que se descuentan o no, asi q espero tu apoyo_

### AFP:

Permite registrar las 8 AFP que tiene el Regimen Pensionario AFP. Sus campos actuales son:

```python
class AFP(models.Model):
    nombre_afp = models.CharField(max_length=45, verbose_name='Nombre de AFP')

    def __str__(self):
        return self.nombre_afp

    class Meta:
        db_table = 'afp'
        ordering = ['nombre_afp']
        verbose_name = 'AFP'
        verbose_name_plural = 'AFPs'
```

### ComisionAFP:

Permite registrar Todas las comisiones que tiene cada AFP, Cada AFP tiene diferentes comisiones. Los porcentajes de las comisiones son actualizadas y cambian según orden del gobierno central nacional es por eso que se esta agregando un campo Periodo, asi que cada periodo de planilla se tendrán diferentes comisiones, En cada apertura de planilla estas comisiones podrán ser modificadas, si en caso no se requiere modificación, solo se copiara del periodo anterior. Sus campos actuales son:

```python
class ComisionAFP(models.Model):
    pension = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Pensión'
    )
    seguro = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Seguro'
    )
    comision = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Comisión'
    )
    total = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Total'
    )
    afp = models.ForeignKey(AFP, on_delete=models.CASCADE, verbose_name='AFP')
    periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE, verbose_name='Período')

    def __str__(self):
        return f'{self.afp} - {self.periodo}'

    def save(self, *args, **kwargs):
        self.total = self.pension + self.seguro + self.comision
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'comision_afp'
        ordering = ['id']
        verbose_name = 'Comisión AFP'
        verbose_name_plural = 'Comisiones AFP'
```

### TipoPlanilla:

Nos servira para almacenar todos los tipos de planilla q tenemos, la primera planilla que el sistema permitirá hacer es una planilla tipo "ACTIVOS". Tenemos estos Tipos de Planilla:

-   Activos(01)
-   Pensionistas(02)
-   Beneficiarios Judiciales y Tutores(04)
-   Pagos únicos(06)
-   Provisionales
-   Reconocimientos Estatales

Sus campos actuales son

-   nombre_tipo_planilla
-   codigo_tipo_planilla

_Ayúdame a generar el modelo para django_

### ClasePlanilla

Sirve para almacenar todas las clases de planillas, esta tabla almacena todas las clases de planilla que el sistema puede realizar, y cada clase de planilla esta relacionada a un tipo de planilla. Al momento de agregar a un trabajador, se deberá seleccionar una de estas opciones. La relacion con el tipo de planilla es de esta manera:

| CODIGO_TIPO_PLANILLA | TIPO_PLANILLA                      | CODIGO_CLASE_PLANILLA | CLASE_PLANILLA                                       |
| -------------------- | ---------------------------------- | --------------------- | ---------------------------------------------------- |
| 01                   | ACTIVOS                            | 01                    | HABERES                                              |
| 01                   | ACTIVOS                            | 03                    | CAS                                                  |
| 01                   | ACTIVOS                            | 04                    | CONTRATOS FAG - PAC                                  |
| 01                   | ACTIVOS                            | 06                    | MODALIDADES FORMATIVAS Y OTROS DE SIMILAR NATURALEZA |
| 01                   | ACTIVOS                            | 16                    | OCASIONALES                                          |
| 01                   | ACTIVOS                            | 20                    | OCASIONALES CTS                                      |
| 02                   | PENSIONISTAS                       | 07                    | PENSIONISTAS                                         |
| 02                   | PENSIONISTAS                       | 21                    | SOBREVIVIENTES                                       |
| 02                   | PENSIONISTAS                       | 22                    | OCASIONALES                                          |
| 04                   | BENEFICIARIOS JUDICIALES Y TUTORES | 12                    | ALIMENTOS                                            |
| 04                   | BENEFICIARIOS JUDICIALES Y TUTORES | 26                    | TUTORES                                              |
| 06                   | PAGOS ÚNICOS                       | 17                    | LIQUIDACIONES                                        |
| 06                   | PAGOS ÚNICOS                       | 18                    | REINTEGROS                                           |
| 06                   | PAGOS ÚNICOS                       | 27                    | ADEUDOS JUDICIALES                                   |
| 07                   | PROVISIONALES                      | 19                    | PROVISIONAL                                          |
| 08                   | RECONOCIMIENTOS ESTATALES          | 23                    | PENSIONES DE GRACIA                                  |
| 08                   | RECONOCIMIENTOS ESTATALES          | 24                    | DEFENSORES DE LA PATRIA                              |
| 08                   | RECONOCIMIENTOS ESTATALES          | 25                    | PALMAS MAGISTERIALES                                 |

Sus campos actuales son:

```python
class ClasePlanilla(models.Model):
    nombre_clase_planilla = models.CharField(
        max_length=45, blank=True, verbose_name='Nombre de Clase de Planilla')
    codigo_clase_planilla = models.CharField(max_length=2, blank=True, verbose_name='Código de Clase de Planilla')
    tipo_planilla = models.ForeignKey(
        TipoPlanilla, on_delete=models.CASCADE, verbose_name='Tipo de Planilla', null=True, blank=True)

    def __str__(self):
        return self.nombre_clase_planilla

    class Meta:
        db_table = 'clase_planilla'
        ordering = ['nombre_clase_planilla']
        verbose_name = 'Clases de Planilla'
        verbose_name_plural = 'Clases de Planilla'
```

### FuenteFinanciamiento:

Cada trabajador pertenece a una fuente de financiamiento, de esta manera identificaremos y generaremos las diferentes planillas, al agregar a un trabajador, seleccionaremos la clase de planilla y luego también seleccionaremos la "Fuente de Financiamiento" al cual pertenece.

Los campos actuales son:

```python
class FuenteFinanciamiento(models.Model):
    nombre_fuente_financiamiento = models.CharField(
        max_length=45, blank=True, verbose_name='Nombre de Fuente de Financiamiento')
    tipo_planilla = models.ForeignKey(
        ClasePlanilla, on_delete=models.CASCADE, verbose_name='Clase de Planilla', null=True, blank=True)

    def __str__(self):
        return self.nombre_fuente_financiamiento

    class Meta:
        db_table = 'fuente_financiamiento'
        ordering = ['nombre_fuente_financiamiento']
        verbose_name = 'Fuente de Financiamiento'
        verbose_name_plural = 'Fuentes de Financiamiento'
```

### Banco:

Permite registrar todos los bancos disponibles para pago. Sus campos son:

```python
class Banco(models.Model):
    nombre_banco = models.CharField(
        max_length=45, verbose_name='Nombre de Banco')

    def __str__(self):
        return self.nombre_banco

    class Meta:
        db_table = 'banco'
        ordering = ['nombre_banco']
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
```

### Auditoria:

Esta tabla servira para realizar auditoria del sistema, aun no pensé en los campos pero pienso que debe tener:

-   fecha
-   descripcion
-   persona(Identificara a la persona de la tabla persona que hizo alguna modificación)
-   etc etc

Sus campos actuales son:

```python
class Auditoria(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    descripcion = models.TextField(verbose_name='Descripción')
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name='Persona'
    )
    ip_address = models.GenericIPAddressField(
        null=True, blank=True, verbose_name='Dirección IP'
    )
    user_agent = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='User Agent'
    )
    accion = models.CharField(
        max_length=50, verbose_name='Acción'
    )

    class Meta:
        db_table = 'auditoria'
        ordering = ['-fecha']
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
```

## Estructura del Proyecto
```plaintext
planillas/
│
├── manage.py
├── planillas/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── apps/
│   ├── __init__.py
│   ├── autenticacion/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│   │
│   ├── usuarios/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│   │
│   ├── trabajadores/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│   │
│   ├── transacciones/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│   │
│   ├── planillas/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│   │
│   ├── reportes/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│   │
│   ├── procesos/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── permissions.py
│   │   ├── tests.py
│
├── static/
│   ├── css/
│   ├── js/
│
├── templates/
│   ├── base.html
│   ├── ...
│
├── requirements.txt
└── Dockerfile
```