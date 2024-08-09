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


### Persona:

Donde se colocaran los datos personales de todos los usuarios y trabajadores, los campos que se tendrán son:

### Trabajador:

Esta tabla servira para registrar a todos nuestros trabajadores, y se tomaran los datos personales de la tabla persona, sus campos son:

### Transaccion:

Que permitirá registrar todos los haberes y descuentos que existen, estas transacciones se registran de la tabla nacional de haberes que tienen todos los trabajadores de estado, Luego desde acá se tomaran los haberes de cada trabajador. Esta es la base de haberes. Los campos que tenemos son:

### Periodo:

Sirve para registrar todos los periodos en el que se están trabajando las planillas, por ejemplo, en el mes de enero se apresurara la planilla 202401, para febrero será la planilla 202402, si es adicional se sumara 20, ejemplo, para adicional de febrero será 202422, para junio será 202426. Con esta tabla podremos tener registrados todos los haberes y descuentos de nuestros trabajadores organizados por periodos laborales o periodos de pagos. Sus campos son:

### TransaccionTrabajador:

Sirve para designar que haber o descuento le corresponde a cada trabajador de acuerdo al periodo de las planillas, por ejemplo, si un trabajador es contratado de marzo a diciembre, su periodo será esas mismas fechas. Los campos son:

### Beneficiario:

Esta tabla sirve para registrar Beneficiarios de trabajadores, quiero decir, se pueden registrar judiciales, tutores entre otros tipos de beneficiarios para que al profesor se le descuente un monto fijo o un valor porcentual de su sueldo y luego sea depositado en la cuenta del beneficiario. Al agregar a un beneficiario, se registrara un descuento para el trabajador en la tabla 'DescuentoTrabajador'. Sus campos son:

### PlanillaTrabajador:

Esta tabla estoy pensando registrar todos los detalles de la remuneracion de cada trabajador, sean todos los haberes y descuentos asi como los pagos de essalud(q no esta siendo descontado del trabajador). Esta tabla servirá para que cuando el trabajador inicie sesión y quiera ver el detalle de sus pagos, pueda revisar sin problemas, ademas, el trabajador podrá seleccionar el periodo del q quiere revisar el detalle de su remuneracion. Sus campos son:

### PlanillaBeneficiario:

Permite registrar el detalle de la planilla de los beneficiarios, ellos también tendrán acceso al sistema para q puedan revisar el detalle de sus pagos por concepto de descuento a los titulares. Los campos que estoy pensando por mientras son:


### UGEL:

En esta tabla se registraran las diferentes UGELes que quieran usar el sistema (si asi lo desean). Los campos actuales son:


### Cargo:

Se almacenaran todos los cargos disponibles de todos nuestros trabajadores(Todavía no estoy seguro si acá debo agregar los montos para cada cargo). sus campos actuales son:


### RegimenLaboral:

Agregaremos todos los regímenes laborales que tenemos en nuestro país. Creo que se debería considerar cada 'Haber' debe estar relacionada a un Regimen Laboral. Ya que por ejemplo, el Haber "135: Remuneracion CAS" debe estar asociado al Regimen Laboral "DL 1057 - CAS" eso para ordenar un poco. Por ahora, mis campos actuales son:

### TipoServidor

En esta tabla se almacenaran todos los tipos de servidores, tendremos servidores nombrados que pertenecen a los Regímenes laborales de "DL 276 - Personal Administrativo" o al regimen laboral "Ley 29944 - Ley de la Reforma Magisterial". Un "DL 1057 - CAS" no tiene trabajadores nombrados, mas bien tiene Permanentes, te paso un cuadro de quienes pueden estar en qué regimen laboral:

| Regimen Laboral                            | Tipo Servidor                       |
| ------------------------------------------ | ----------------------------------- |
| "DL 1057 - CAS"                            | Contratado y Permanentes            |
| Ley 29944 - Ley de la Reforma Magisterial" | Contratados y Nombrados             |
| "DL 276 - Personal Administrativo"         | Contratados, Nombrados y Designados |

etc etc

### RegimenPensionario:

En el país solo tenemos dos Regímenes pensionario, "AFP(SPP) y ONP(SNP)", antiguamente existía un tercero que era el "DL 20530" que ya no existe. Esta tabla registra esos regímenes, quizá pienses que crear una tabla para dos registros no sea buena idea pero yo si lo creo. Sus campos Actuales son:

_Asimismo, el regimen AFP tiene otros 8 tipos de AFP, cada uno con sus respectivos porcentajes de descuento al trabajador, no se si sea buena idea agregar en esta misma tabla esos 8 AFP con sus porcentajes que se descuentan o no, asi q espero tu apoyo_

### AFP:


### ComisionAFP:

Permite registrar Todas las comisiones que tiene cada AFP, Cada AFP tiene diferentes comisiones. Los porcentajes de las comisiones son actualizadas y cambian según orden del gobierno central nacional es por eso que se esta agregando un campo Periodo, asi que cada periodo de planilla se tendrán diferentes comisiones, En cada apertura de planilla estas comisiones podrán ser modificadas, si en caso no se requiere modificación, solo se copiara del periodo anterior. Sus campos actuales son:

### TipoPlanilla:

Nos servira para almacenar todos los tipos de planilla q tenemos, la primera planilla que el sistema permitirá hacer es una planilla tipo "ACTIVOS". Tenemos estos Tipos de Planilla:

-   Activos(01)
-   Pensionistas(02)
-   Beneficiarios Judiciales y Tutores(04)
-   Pagos únicos(06)
-   Provisionales
-   Reconocimientos Estatales

etc etc

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


### FuenteFinanciamiento:

Cada trabajador pertenece a una fuente de financiamiento, de esta manera identificaremos y generaremos las diferentes planillas, al agregar a un trabajador, seleccionaremos la clase de planilla y luego también seleccionaremos la "Fuente de Financiamiento" al cual pertenece.

### Banco:

Permite registrar todos los bancos disponibles para pago. 

### Auditoria:

Esta tabla servira para realizar auditoria del sistema, aun no pensé en los campos pero pienso que debe tener:

-   fecha
-   descripcion
-   persona(Identificara a la persona de la tabla persona que hizo alguna modificación)
-   etc etc

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