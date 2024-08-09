# Estructura del Directorio y Contenido de Archivos

## Estructura del Directorio:

```
├── logs/
│   ├── error.log
│   ├── debug.log.4
│   ├── debug.log.3
│   ├── debug.log.2
│   ├── debug.log.5
│   ├── debug.log
│   └── debug.log.1
├── static/
├── planillas/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── development.py
│   │   ├── base.py
│   │   └── production.py
│   ├── swagger.py
│   ├── asgi.py
│   ├── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── procesos/
│   │   ├── periodo_normal/
│   │   │   ├── generar_boletas_pago.py
│   │   │   ├── __init__.py
│   │   │   ├── cerrar_aperturar_periodo.py
│   │   │   └── calcular_planilla_remuneraciones.py
│   │   ├── periodo_adicional/
│   │   │   └── __init__.py
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── generar_boletas.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── utils.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── reportes/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── configuracion/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── usuarios/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── trabajadores/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── transacciones/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── planillas/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── auditoria/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __init__.py
│   └── middleware.py
├── media/
├── db_planillas.sqlite3
├── Tablas Parametricas.xlsx
├── estructura_de_proyecto.md
└── manage.py
```

## Contenido de los Archivos:

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/swagger.py**
```python
# planillas/swagger.py
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Sistema de Planillas API",
        default_version='v1',
        description="Documentación de la API del Sistema de Planillas",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JWTAuthentication,),
)
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/urls.py**
```python
# planillas/urls.py (en el archivo principal de urls del proyecto)
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from .swagger import schema_view  # Asegúrate de que esta importación apunte correctamente a tu archivo swagger.py

from apps.usuarios.views import CustomLoginView, CustomLogoutView, CustomUserDetail, ProtectedView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', CustomLoginView.as_view(), name='custom_login'),  # Ruta para login
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar token
    path('api/auth/user/', CustomUserDetail.as_view(), name='custom_user_detail'),  # Ruta para obtener detalles del usuario autenticado

    path('api/configuracion/', include('apps.configuracion.urls')),
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('api/trabajadores/', include('apps.trabajadores.urls')),
    path('api/transacciones/', include('apps.transacciones.urls')),
    path('api/planillas/', include('apps.planillas.urls')),
    path('api/reportes/', include('apps.reportes.urls')),
    path('api/procesos/', include('apps.procesos.urls')),
    path('api/auditoria/', include('apps.auditoria.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-redirect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/wsgi.py**
```python
"""
WSGI config for planillas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planillas.settings.production')

application = get_wsgi_application()
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/settings/__init__.py**
```python
import os
from decouple import config

ENVIRONMENT = config('ENVIRONMENT', default='development')

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/settings/development.py**
```python
# planillas/settings/development.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_planillas.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Configuración de correo para desarrollo
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Permite todas las origenes en desarrollo
CORS_ALLOW_ALL_ORIGINS = True

# Configuración de CORS para desarrollo
CORS_ALLOW_CREDENTIALS = True


CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',  # Añade aquí el origen de tu frontend
    'http://localhost:9000',
    'http://192.168.28.129:9000'
]```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/settings/base.py**
```python
import os
from pathlib import Path
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'rest_framework',
    'rest_framework.authtoken',  # Necesario para la autenticación con token
    'corsheaders',
    'auditlog',
    'drf_yasg',
    'apps.usuarios',
    'apps.trabajadores',
    'apps.transacciones',
    'apps.planillas',
    'apps.reportes',
    'apps.procesos',
    'apps.auditoria',
    'apps.configuracion',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'planillas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'planillas.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.TokenAuthentication',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/minute',  # Ajusta esto según tus necesidades
        'anon': '50/minute',
    }
    
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '1000/day'
    # }
}

AUTH_USER_MODEL = 'usuarios.User'

# Configuración básica de CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',  # URL de tu frontend
    'http://localhost:9000',
    'http://192.168.28.129:9000'
    
]
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',  # URL de tu frontend
    'http://localhost:9000',
    'http://192.168.28.129:9000'
]

# Permitir todas las métodos en CORS
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


# Configuracion de Logging
import logging

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'request'):
            record.http_status = getattr(record, 'status_code', '')
            record.http_user = record.request.user if hasattr(record.request, 'user') else ''
            record.http_host = record.request.get_host() if hasattr(record.request, 'get_host') else ''
            record.http_path = record.request.path if hasattr(record.request, 'path') else ''
        else:
            record.http_status = ''
            record.http_user = ''
            record.http_host = ''
            record.http_path = ''
        return super().format(record)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            '()': CustomFormatter,
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message} {http_status} {http_user} {http_host} {http_path}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'rotating_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/debug.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/error.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['rotating_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['rotating_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['rotating_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'apps': {
            'handlers': ['rotating_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'security': {
            'handlers': ['rotating_file', 'error_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.contrib.auth': {
            'handlers': ['rotating_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['rotating_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

from datetime import timedelta

# Configuración detallada de Simple JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),  # Tiempo de vida del token de acceso
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=6),     # Tiempo de vida del token de refresco
    'ROTATE_REFRESH_TOKENS': True,  # No rotamos los tokens de refresco automáticamente
    'BLACKLIST_AFTER_ROTATION': True,  # Ponemos en lista negra los tokens después de la rotación
    'ALGORITHM': 'HS256',  # Algoritmo de encriptación usado
    'SIGNING_KEY': SECRET_KEY,  # Clave para firmar los tokens (usamos la SECRET_KEY de Django)
    'VERIFYING_KEY': None,  # Clave de verificación (no necesaria con HS256)
    'AUTH_HEADER_TYPES': ('Bearer',),  # Tipo de header de autenticación
    'USER_ID_FIELD': 'id',  # Campo que usamos como ID de usuario
    'USER_ID_CLAIM': 'user_id',  # Nombre del claim para el ID de usuario en el token
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# # Configuración de JWT
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Duración del token de acceso
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Duración del token de refresco
#     'ROTATE_REFRESH_TOKENS': False,  # No rotar tokens de refresco automáticamente
#     'BLACKLIST_AFTER_ROTATION': True,  # Invalidar token de refresco después de rotación
#     'AUTH_HEADER_TYPES': ('Bearer',),  # Tipo de encabezado de autorización
# }

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/planillas/settings/production.py**
```python
# planillas/settings/production.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': config('MEMCACHED_LOCATION'),
    }
}

# Configuración de seguridad para producción
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Configuración de correo para producción
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# En producción, especifica los orígenes permitidos
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
    # Añade aquí los dominios desde los que se accederá a tu API en producción
]```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/middleware.py**
```python
# apps/middleware.py
from django.http import HttpResponseForbidden

class UgelRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated and user.role != 'admin_sistema':
            if 'ugel' in request.GET and request.GET['ugel'] != str(user.ugel.id):
                return HttpResponseForbidden("No tiene permiso para acceder a esta UGEL.")
        response = self.get_response(request)
        return response
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/models.py**
```python
from django.db import models
from apps.planillas.models import Planilla

class ProcesosPlanilla(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    planillas = models.ManyToManyField(Planilla, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proceso de Planilla"
        verbose_name_plural = "Procesos de Planillas"```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/serializers.py**
```python
# apps/procesos/serializers.py
from rest_framework import serializers

class ProcesarPlanillaSerializer(serializers.Serializer):
    periodo = serializers.CharField(max_length=6)
    tipo_planilla = serializers.IntegerField()
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/apps.py**
```python
from django.apps import AppConfig


class ProcesosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.procesos'
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/admin.py**
```python
from django.contrib import admin
from .models import ProcesosPlanilla
from apps.planillas.models import Planilla
from .periodo_normal import CalcularPlanillaRemuneraciones, GenerarBoletasPago, CerrarAperturarPeriodo

@admin.action(description='Generar boletas para las planillas seleccionadas')
def generar_boletas(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            GenerarBoletasPago.generar(planilla.id)
    modeladmin.message_user(request, "Boletas generadas exitosamente.")

@admin.action(description='Calcular planilla de remuneraciones para las planillas seleccionadas')
def calcular_planilla_remuneraciones(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            CalcularPlanillaRemuneraciones.calcular(planilla.id)
    modeladmin.message_user(request, "Planillas de remuneraciones calculadas exitosamente.")


@admin.action(description='Cerrar y aperturar nuevo periodo')
def cerrar_aperturar_periodo(modeladmin, request, queryset):
    for proceso in queryset:
        try:
        # Asumiendo que se obtienen mes, anio y es_adicional de algún formulario o método
            periodo = "202407"
            es_adicional = False  # Ejemplo de valor, cambiar según sea necesario
            CerrarAperturarPeriodo.cerrar_aperturar(periodo, es_adicional)
            modeladmin.message_user(request, "Periodo cerrado y nuevo periodo creado exitosamente.")
        except Exception as e:
            modeladmin.message_user(request, f"Error al cerrar y aperturar periodo: {str(e)}", level='error')

@admin.action(description='Revertir cálculo de planilla de remuneraciones para las planillas seleccionadas')
def revertir_calculo(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            CalcularPlanillaRemuneraciones.revertir_calculo(planilla.id)
    modeladmin.message_user(request, "Cálculo de planillas de remuneraciones revertido exitosamente.")

@admin.action(description='Revertir boletas generadas para las planillas seleccionadas')
def revertir_boletas_generadas(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            GenerarBoletasPago.revertir_boletas_generadas(planilla.id)
    modeladmin.message_user(request, "Boletas generadas revertidas exitosamente.")

@admin.action(description='Revertir Cierre/Apertura de periodos')
def revertir_cierre_apertura(modeladmin, request, queryset):
    for proceso in queryset:
        for planilla in proceso.planillas.all():
            CerrarAperturarPeriodo.revertir_cierre_apertura(planilla.periodo)
    modeladmin.message_user(request, "Cierre/Apertura de periodos revertidos exitosamente.")


class PlanillaInline(admin.TabularInline):
    model = ProcesosPlanilla.planillas.through
    extra = 1

@admin.register(ProcesosPlanilla)
class ProcesosPlanillaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'planillas_count')
    actions = [cerrar_aperturar_periodo, calcular_planilla_remuneraciones, revertir_calculo, generar_boletas, revertir_boletas_generadas, revertir_cierre_apertura]
    inlines = [PlanillaInline]
    exclude = ('planillas',)

    def planillas_count(self, obj):
        return obj.planillas.count()
    planillas_count.short_description = 'Número de Planillas'```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/utils.py**
```python
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
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/tests.py**
```python
def generar_meses_validos(anio):
    meses_validos = {}
    for mes in range(1, 13):
        mes_str = str(mes).zfill(2)
        base_periodo = int(f"{anio}{mes_str}")
        # Generar las 5 planillas válidas para cada mes
        meses_validos[base_periodo] = [base_periodo + i * 20 for i in range(5)]
    return meses_validos

# Ejemplo de uso para el año 2024
meses_validos_2024 = generar_meses_validos(2025)
for mes, periodos in meses_validos_2024.items():
    print(f"{mes}: {periodos}")
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/urls.py**
```python
# apps/procesos/urls.py
from django.urls import path
from .views import CerrarAperturarPeriodoView, CalcularPlanillaRemuneracionesView, GenerarBoletasPagoView

urlpatterns = [
    path('cerrar-aperturar-periodo/', CerrarAperturarPeriodoView.as_view(), name='cerrar-aperturar-periodo'),
    path('calcular-planilla-remuneraciones/', CalcularPlanillaRemuneracionesView.as_view(), name='calcular-planilla-remuneraciones'),
    path('generar-boletas-pago/', GenerarBoletasPagoView.as_view(), name='generar-boletas-pago'),
]```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/views.py**
```python
# apps/procesos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .periodo_normal import CalcularPlanillaRemuneraciones, GenerarBoletasPago, CerrarAperturarPeriodo

class CerrarAperturarPeriodoView(APIView):
    def post(self, request):
        try:
            CerrarAperturarPeriodo()
            return Response({"message": "Periodo cerrado y nuevo periodo aperturado con éxito."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CalcularPlanillaRemuneracionesView(APIView):
    def post(self, request):
        try:
            CalcularPlanillaRemuneraciones()
            return Response({"message": "Planilla de remuneraciones calculada con éxito."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GenerarBoletasPagoView(APIView):
    def post(self, request):
        planilla_id = request.data.get('planilla_id')
        if not planilla_id:
            return Response({"error": "Se requiere el ID de la planilla."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            GenerarBoletasPago(planilla_id)
            return Response({"message": "Boletas de pago generadas con éxito."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/periodo_normal/generar_boletas_pago.py**
```python
from django.db import transaction
from apps.planillas.models import Planilla, Boleta, Contrato, BoletaTransaccion
from django.db.models import Sum, Max
from decimal import Decimal
from django.utils import timezone


class GenerarBoletasPago:
    @staticmethod
    @transaction.atomic
    def generar(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)
        contratos = Contrato.objects.filter(
            clase_planilla=planilla.clase_planilla,
            fuente_financiamiento=planilla.fuente_financiamiento,
            trabajador__estado=True
        ).exclude(situacion__nombre_situacion__in=['Suspendido', 'Baja'])

        boletas_generadas = 0

        for contrato in contratos:
            boleta, created = Boleta.objects.get_or_create(
                contrato=contrato,
                planilla=planilla,
                defaults={
                    'centro_de_trabajo': contrato.centro_de_trabajo,
                    'cargo': contrato.cargo.nombre_cargo if contrato.cargo else '',
                    'fecha_ingreso': contrato.fecha_ingreso,
                    'fecha_cese': contrato.fecha_cese,
                    'clase_planilla': contrato.clase_planilla.nombre_clase_planilla,
                    'fuente_financiamiento': contrato.fuente_financiamiento.nombre_fuente_financiamiento,
                    'sueldo': contrato.sueldo,
                    'dias_laborados': contrato.dias_laborados,
                    'leyenda_permanente': contrato.leyenda_permanente,
                    'jornada_laboral': contrato.jornada_laboral,
                    'trabajador_nombres': contrato.trabajador.persona.nombres,
                    'trabajador_apellidos': f"{contrato.trabajador.persona.apellido_paterno} {contrato.trabajador.persona.apellido_materno}",
                    'trabajador_dni': contrato.trabajador.persona.numero_documento,
                    'regimen_laboral': contrato.regimen_laboral.nombre_regimen_laboral,
                    'tipo_servidor': contrato.tipo_servidor.nombre_tipo_servidor,
                    'regimen_pensionario': contrato.trabajador.regimen_pensionario.nombre_regimen_pensionario,
                    'banco': contrato.trabajador.banco.nombre_banco,
                    'cuenta_bancaria': contrato.trabajador.numero_cuenta,
                }
            )

            GenerarBoletasPago.calcular_totales(boleta)
            GenerarBoletasPago.generar_numero_boleta(boleta)
            GenerarBoletasPago.registrar_transacciones_boleta(boleta)
            GenerarBoletasPago.actualizar_totales_planilla(boleta)

            boletas_generadas += 1

        return f"Se generaron o actualizaron {boletas_generadas} boletas para la planilla {planilla}."

    @staticmethod
    def calcular_totales(boleta):
        transacciones = boleta.contrato.transacciones.filter(
            periodo_inicial__lte=boleta.planilla.periodo.periodo,
            periodo_final__gte=boleta.planilla.periodo.periodo,
            estado=True
        )
        boleta.total_haberes = transacciones.filter(transaccion__tipo_transaccion='HABER').aggregate(Sum('monto'))['monto__sum'] or Decimal('0')
        boleta.total_descuentos = transacciones.filter(transaccion__tipo_transaccion='DESCUENTO').aggregate(Sum('monto'))['monto__sum'] or Decimal('0')
        boleta.total_aportes = transacciones.filter(transaccion__tipo_transaccion='APORTE').aggregate(Sum('monto'))['monto__sum'] or Decimal('0')
        boleta.neto_a_pagar = boleta.total_haberes - boleta.total_descuentos
        boleta.save()

    @staticmethod
    def generar_numero_boleta(boleta):
        max_numero_boleta = Boleta.objects.filter(planilla=boleta.planilla).aggregate(Max('numero_boleta'))['numero_boleta__max']
        if max_numero_boleta:
            boleta.numero_boleta = str(int(max_numero_boleta) + 1).zfill(3)
        else:
            boleta.numero_boleta = '001'
        boleta.save()

    @staticmethod
    def registrar_transacciones_boleta(boleta):
        transacciones = boleta.contrato.transacciones.filter(
            periodo_inicial__lte=boleta.planilla.periodo.periodo,
            periodo_final__gte=boleta.planilla.periodo.periodo,
            estado=True
        )
        for transaccion in transacciones:
            BoletaTransaccion.objects.create(
                boleta=boleta,
                tipo=transaccion.transaccion.tipo_transaccion,
                codigo=transaccion.transaccion.codigo_transaccion_mcpp,
                descripcion=transaccion.transaccion.descripcion_transaccion,
                monto=transaccion.monto
            )

    @staticmethod
    def actualizar_totales_planilla(boleta):
        planilla = boleta.planilla
        planilla.total_haberes = Boleta.objects.filter(planilla=planilla).aggregate(Sum('total_haberes'))['total_haberes__sum'] or Decimal('0')
        planilla.total_descuentos = Boleta.objects.filter(planilla=planilla).aggregate(Sum('total_descuentos'))['total_descuentos__sum'] or Decimal('0')
        planilla.total_aportes = Boleta.objects.filter(planilla=planilla).aggregate(Sum('total_aportes'))['total_aportes__sum'] or Decimal('0')
        planilla.save()

    @staticmethod
    def marcar_como_visualizada(boleta):
        boleta.visualizada = True
        boleta.fecha_visualizacion = timezone.now()
        boleta.save()

    @staticmethod
    def marcar_como_descargada(boleta):
        boleta.descargada = True
        boleta.fecha_descarga = timezone.now()
        boleta.save()


    @staticmethod
    @transaction.atomic
    def revertir_boletas_generadas(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)

        # Obtener todas las boletas asociadas a la planilla
        boletas = Boleta.objects.filter(planilla=planilla)

        # Eliminar todas las transacciones de boletas asociadas a las boletas
        BoletaTransaccion.objects.filter(boleta__in=boletas).delete()

        # Eliminar todas las boletas asociadas a la planilla
        boletas.delete()

        # Restaurar los valores originales de la planilla (esto asume que tienes una forma de obtener los valores originales)
        planilla.total_haberes = 0
        planilla.total_descuentos = 0
        planilla.total_aportes = 0
        planilla.save()```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/periodo_normal/__init__.py**
```python
from apps.procesos.periodo_normal.calcular_planilla_remuneraciones import CalcularPlanillaRemuneraciones
from apps.procesos.periodo_normal.generar_boletas_pago import GenerarBoletasPago
from apps.procesos.periodo_normal.cerrar_aperturar_periodo import CerrarAperturarPeriodo
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/periodo_normal/cerrar_aperturar_periodo.py**
```python
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
            raise ValidationError(f"Error al revertir el cierre y apertura de periodo: {str(e)}")   ```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/periodo_normal/calcular_planilla_remuneraciones.py**
```python
from django.db import transaction
from decimal import Decimal
from apps.configuracion.models import Periodo, Transaccion, ComisionAfp
from apps.planillas.models import Contrato, Planilla
from apps.transacciones.models import TransaccionContrato


class CalcularPlanillaRemuneraciones:
    @staticmethod
    @transaction.atomic
    def calcular(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)

        try:
            periodo_actual = Periodo.objects.get(estado=True)
        except Periodo.DoesNotExist:
            raise ValueError("No hay un periodo activo para procesar las planillas.")

        contratos = Contrato.objects.filter(
            clase_planilla=planilla.clase_planilla,
            fuente_financiamiento=planilla.fuente_financiamiento,
            trabajador__estado=True
        ).exclude(situacion__nombre_situacion__in=['Suspendido', 'Baja'])

        for contrato in contratos:
            sueldo_proporcional = (contrato.sueldo * Decimal(contrato.dias_laborados)) / Decimal('30')

            transacciones = {
                'remuneracion': Transaccion.objects.get(id=1),
                'onp': Transaccion.objects.get(id=6),
                'afp': Transaccion.objects.get(id=3),
            }

            CalcularPlanillaRemuneraciones.registrar_transaccion(contrato, transacciones['remuneracion'], sueldo_proporcional, periodo_actual.periodo)

            regimen_pensionario = contrato.trabajador.regimen_pensionario.codigo_regimen_pensionario

            if regimen_pensionario == '02':  # ONP
                monto_descuento = sueldo_proporcional * Decimal('0.13')
                CalcularPlanillaRemuneraciones.registrar_transaccion(contrato, transacciones['onp'], monto_descuento, periodo_actual.periodo)
            elif regimen_pensionario == '03':  # AFP
                try:
                    comision_afp = ComisionAfp.objects.get(afp=contrato.trabajador.afp, periodo=periodo_actual)
                    monto_descuento = sueldo_proporcional * (comision_afp.total_comision / Decimal('100'))
                    CalcularPlanillaRemuneraciones.registrar_transaccion(contrato, transacciones['afp'], monto_descuento, periodo_actual.periodo)
                except ComisionAfp.DoesNotExist:
                    print(f"No se encontró comisión AFP para {contrato.trabajador.afp} en el periodo {periodo_actual.periodo}")

        planilla.total_haberes = sum(t.monto for t in TransaccionContrato.objects.filter(
            contrato__in=contratos,
            transaccion__tipo_transaccion='HABER',
            periodo_inicial=periodo_actual.periodo
        ))
        planilla.total_descuentos = sum(t.monto for t in TransaccionContrato.objects.filter(
            contrato__in=contratos,
            transaccion__tipo_transaccion='DESCUENTO',
            periodo_inicial=periodo_actual.periodo
        ))
        planilla.total_aportes = sum(t.monto for t in TransaccionContrato.objects.filter(
            contrato__in=contratos,
            transaccion__tipo_transaccion='APORTE',
            periodo_inicial=periodo_actual.periodo
        ))
        planilla.save()

    @staticmethod
    def registrar_transaccion(contrato, transaccion, monto, periodo):
        TransaccionContrato.objects.update_or_create(
            contrato=contrato,
            transaccion=transaccion,
            periodo_inicial=periodo,
            periodo_final=periodo,
            defaults={
                'monto': monto,
                'estado': True
            }
        )
        
    @staticmethod
    @transaction.atomic
    def revertir_calculo(planilla_id):
        planilla = Planilla.objects.get(id=planilla_id)
        periodo_actual = Periodo.objects.get(estado=True)

        # Obtener contratos asociados a esta planilla
        contratos = Contrato.objects.filter(
            clase_planilla=planilla.clase_planilla,
            fuente_financiamiento=planilla.fuente_financiamiento,
            trabajador__estado=True
        ).exclude(situacion__nombre_situacion__in=['Suspendido', 'Baja'])

        # Eliminar transacciones relacionadas con estos contratos y el periodo actual
        TransaccionContrato.objects.filter(
            contrato__in=contratos,
            periodo_inicial=periodo_actual.periodo
        ).delete()

        # Restaurar los valores originales de la planilla (esto asume que tienes una forma de obtener los valores originales)
        planilla.total_haberes = 0
        planilla.total_descuentos = 0
        planilla.total_aportes = 0
        planilla.save()
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/periodo_adicional/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/procesos/management/commands/generar_boletas.py**
```python
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
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/models.py**
```python
from django.db import models

# Create your models here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/serializers.py**
```python
# apps/reportes/serializers.py
from rest_framework import serializers
from apps.trabajadores.models import Trabajador
from apps.transacciones.models import TransaccionContrato
from apps.planillas.models import PlanillaBeneficiario

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField(source='transaccion.codigo')
    descripcion = serializers.CharField(source='transaccion.descripcion')

    class Meta:
        model = TransaccionContrato
        fields = ['codigo', 'descripcion', 'monto']
        ref_name = 'TransaccionTrabajadorSerializerReportes'

class TrabajadorSerializer(serializers.ModelSerializer):
    transacciones = TransaccionTrabajadorSerializer(many=True, read_only=True)

    class Meta:
        model = Trabajador
        fields = ['id', 'persona', 'estado', 'transacciones']
        ref_name = 'TrabajadorSerializerReportes'


class PlanillaTrabajadorSerializer(serializers.ModelSerializer):
    transacciones = TransaccionTrabajadorSerializer(many=True, source='transacciones')

    class Meta:
        model = Trabajador  # PlanillaTrabajador si es un modelo separado
        fields = ['total_haberes', 'total_descuentos', 'essalud', 'emitio_boleta', 'trabajador', 'tipo_planilla', 'periodo', 'ugel', 'transacciones']
        ref_name = 'PlanillaTrabajadorSerializerReportes'

class PlanillaBeneficiarioSerializer(serializers.ModelSerializer):
    beneficiario = serializers.StringRelatedField()

    class Meta:
        model = PlanillaBeneficiario
        fields = ['id', 'beneficiario', 'monto', 'periodo']
        ref_name = 'PlanillaBeneficiarioSerializerReportes'```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/apps.py**
```python
from django.apps import AppConfig


class ReportesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.reportes'
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/admin.py**
```python
# apps/reportes/admin.py
from django.contrib import admin
from apps.trabajadores.models import Trabajador
from apps.planillas.models import Contrato
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/tests.py**
```python
from django.test import TestCase

# Create your tests here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/urls.py**
```python
# apps/reportes/urls.py
from rest_framework.routers import DefaultRouter
from .views import (
    ReporteRemuneracionActivosViewSet, ReportePlanillaBeneficiariosViewSet,
    ReporteTrabajadoresPorClasePlanillaViewSet, ReporteTrabajadoresPorFuenteFinanciamientoViewSet,
    ReporteTrabajadoresPorVinculoViewSet
)

router = DefaultRouter()
router.register(r'remuneracion-activos', ReporteRemuneracionActivosViewSet, basename='reporte-remuneracion-activos')
router.register(r'planilla-beneficiarios', ReportePlanillaBeneficiariosViewSet, basename='reporte-planilla-beneficiarios')
router.register(r'trabajadores-clase-planilla', ReporteTrabajadoresPorClasePlanillaViewSet, basename='reporte-trabajadores-clase-planilla')
router.register(r'trabajadores-fuente-financiamiento', ReporteTrabajadoresPorFuenteFinanciamientoViewSet, basename='reporte-trabajadores-fuente-financiamiento')
router.register(r'trabajadores-vinculo', ReporteTrabajadoresPorVinculoViewSet, basename='reporte-trabajadores-vinculo')

urlpatterns = router.urls
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/reportes/views.py**
```python
# apps/reportes/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TrabajadorSerializer, PlanillaBeneficiarioSerializer
from apps.trabajadores.models import Trabajador
from apps.planillas.models import PlanillaBeneficiario, Contrato

class ReporteRemuneracionActivosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        
        user = self.request.user
        queryset = Trabajador.objects.filter(contratos__situacion__codigo='HAB')\
            .select_related('persona', 'ugel', 'regimen_pensionario', 'afp')\
            .prefetch_related('contratos', 'contratos__transacciones')
        
        if user.role != 'admin_sistema':
            queryset = queryset.filter(ugel=user.ugel)
        
        return queryset.distinct()

class ReportePlanillaBeneficiariosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlanillaBeneficiarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return PlanillaBeneficiario.objects.none()
        return PlanillaBeneficiario.objects.all()

class ReporteTrabajadoresPorClasePlanillaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        clase_planilla = self.request.query_params.get('clase_planilla')
        if clase_planilla:
            return Trabajador.objects.filter(contratos__clase_planilla__nombre_clase_planilla=clase_planilla).distinct()
        return Trabajador.objects.none()

class ReporteTrabajadoresPorFuenteFinanciamientoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        fuente_financiamiento = self.request.query_params.get('fuente_financiamiento')
        if fuente_financiamiento:
            return Trabajador.objects.filter(contratos__fuente_financiamiento__nombre_fuente_financiamiento=fuente_financiamiento).distinct()
        return Trabajador.objects.none()

class ReporteTrabajadoresPorVinculoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Trabajador.objects.none()
        dias_restantes = self.request.query_params.get('dias_restantes')
        if dias_restantes is not None:
            try:
                dias_restantes = int(dias_restantes)
                return Trabajador.objects.filter(contratos__dias_laborados__lte=dias_restantes).distinct()
            except ValueError:
                pass
        return Trabajador.objects.none()
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/models.py**
```python
# apps/configuracion/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from auditlog.registry import auditlog

class TipoDocumento(models.Model):
    codigo_tipo_documento = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion_tipo_documento = models.CharField(max_length=50, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion_tipo_documento

    class Meta:
        db_table = 'tipo_documento'
        ordering = ['descripcion_tipo_documento']
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'


class Sexo(models.Model):
    codigo_sexo = models.CharField(max_length=1, unique=True, verbose_name='Código')
    descripcion_sexo = models.CharField(max_length=20, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion_sexo

    class Meta:
        db_table = 'sexo'
        ordering = ['descripcion_sexo']
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'


class TipoDescuento(models.Model):
    codigo_tipo_descuento = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion_tipo_descuento = models.CharField(max_length=20, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_descuento'
        ordering = ['descripcion_tipo_descuento']
        verbose_name = 'Tipo de Descuento'
        verbose_name_plural = 'Tipos de Descuento'


class TipoBeneficiario(models.Model):
    codigo_tipo_beneficiario = models.CharField(max_length=2, unique=True, verbose_name='Código')
    descripcion_tipo_beneficiario = models.CharField(max_length=20, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_beneficiario'
        ordering = ['descripcion_tipo_beneficiario']
        verbose_name = 'Tipo de Beneficiario'
        verbose_name_plural = 'Tipos de Beneficiario'


class Ugel(models.Model):
    nombre_ugel = models.CharField(max_length=100, verbose_name='Nombre de UGEL')
    nombre_corto_ugel = models.CharField(max_length=25, verbose_name='Nombre Corto de UGEL', null=True, blank=True)
    codigo_ugel = models.CharField(max_length=3, verbose_name='Código de Ugel', unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_corto_ugel

    class Meta:
        db_table = 'ugel'
        ordering = ['nombre_ugel']
        verbose_name = 'UGEL'
        verbose_name_plural = 'UGELs'
        indexes = [
            models.Index(fields=['codigo_ugel'], name='idx_ugel_codigo'),
        ]


class Periodo(models.Model):
    periodo = models.CharField(max_length=6, unique=True, blank=True, verbose_name='Periodo', editable=False)
    es_adicional = models.BooleanField(default=False, verbose_name='¿Es adicional?')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.periodo} - {self.estado}'

    class Meta:
        db_table = 'periodo'
        ordering = ['periodo', 'es_adicional']
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
        indexes = [
            models.Index(fields=['periodo', 'estado'], name='idx_periodo_estado'),
        ]


class TipoPlanilla(models.Model):
    nombre_tipo_planilla = models.CharField(max_length=45, blank=True, verbose_name='Nombre de Tipo de Planilla')
    codigo_tipo_planilla = models.CharField(max_length=2, unique=True, blank=True, verbose_name='Código de Tipo de Planilla')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_tipo_planilla

    class Meta:
        db_table = 'tipo_planilla'
        ordering = ['nombre_tipo_planilla']
        verbose_name = 'Tipo de Planilla'
        verbose_name_plural = 'Tipos de Planilla'


class ClasePlanilla(models.Model):
    nombre_clase_planilla = models.CharField(max_length=45, blank=True, verbose_name='Nombre de Clase de Planilla')
    codigo_clase_planilla = models.CharField(max_length=2, unique=True, blank=True, verbose_name='Código de Clase de Planilla')
    tipo_planilla = models.ForeignKey(TipoPlanilla, on_delete=models.CASCADE, verbose_name='Tipo de Planilla', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_clase_planilla

    class Meta:
        db_table = 'clase_planilla'
        ordering = ['nombre_clase_planilla']
        verbose_name = 'Clase de Planilla'
        verbose_name_plural = 'Clases de Planilla'


class FuenteFinanciamiento(models.Model):
    nombre_fuente_financiamiento = models.CharField(max_length=45, blank=True, verbose_name='Nombre de Fuente de Financiamiento')
    codigo_fuente_financiamiento = models.CharField(max_length=2, unique=True, blank=True, verbose_name='Código de Fuente de Financiamiento')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_fuente_financiamiento

    class Meta:
        db_table = 'fuente_financiamiento'
        ordering = ['nombre_fuente_financiamiento']
        verbose_name = 'Fuente de Financiamiento'
        verbose_name_plural = 'Fuentes de Financiamiento'


class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('HABER', 'Haber'),
        ('DESCUENTO', 'Descuento'),
        ('APORTE', 'Aporte')
    ]
    CATEGORIA_CHOICES = [
        ('SUELDO', 'Sueldo'),
        ('BONIFICACION', 'Bonificación'),
        ('DEDUCCION', 'Deducción'),
        ('BENEFICIOS_SOCIALES', 'Beneficios Sociales'),
        ('APORTE', 'Aporte'),
        ('OTRO', 'Otro')
    ]

    tipo_transaccion = models.CharField(max_length=10, choices=TIPO_CHOICES, verbose_name='Tipo', default='HABER')
    categoria_transaccion = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, verbose_name='Categoría', default='SUELDO')
    codigo_transaccion_mcpp = models.CharField(max_length=4, unique=True, verbose_name='Código MCPP', help_text='Código MCPP')
    codigo_transaccion_plame = models.CharField(max_length=4, unique=True, verbose_name='Codigo PLAME', help_text='Codigo PLAME')
    descripcion_transaccion = models.CharField(max_length=45, verbose_name='Descripción')
    imponible = models.BooleanField(default=False, verbose_name='Es Imponible?')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.tipo_transaccion == 'HABER' and self.categoria_transaccion not in ['SUELDO', 'BONIFICACION', 'BENEFICIOS_SOCIALES', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Haber.'))
        if self.tipo_transaccion == 'DESCUENTO' and self.categoria_transaccion not in ['DEDUCCION', 'APORTE', 'OTRO']:
            raise ValidationError(_('Categoría inválida para tipo Descuento.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descripcion_transaccion

    class Meta:
        db_table = 'transaccion'
        ordering = ['descripcion_transaccion']
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'
        indexes = [
            models.Index(fields=['codigo_transaccion_mcpp'], name='idx_transaccion_codigo_mcpp'),
            models.Index(fields=['tipo_transaccion'], name='idx_transaccion_tipo'),
        ]


class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=45, verbose_name='Nombre de Cargo')
    codigo_cargo = models.CharField(max_length=3, unique=True, verbose_name='Código de Cargo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'cargo'
        ordering = ['nombre_cargo']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class RegimenLaboral(models.Model):
    nombre_regimen_laboral = models.CharField(max_length=45, verbose_name='Nombre de Régimen Laboral')
    codigo_regimen_laboral = models.CharField(max_length=2, unique=True, verbose_name='Código de Régimen Laboral')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_regimen_laboral

    class Meta:
        db_table = 'regimen_laboral'
        ordering = ['nombre_regimen_laboral']
        verbose_name = 'Régimen Laboral'
        verbose_name_plural = 'Regímenes Laborales'


class TipoServidor(models.Model):
    nombre_tipo_servidor = models.CharField(max_length=45, verbose_name='Nombre de Tipo de Servidor')
    codigo_tipo_servidor = models.CharField(max_length=2, unique=True, verbose_name='Código de Tipo de Servidor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_tipo_servidor

    class Meta:
        db_table = 'tipo_servidor'
        ordering = ['nombre_tipo_servidor']
        verbose_name = 'Tipo de Servidor'
        verbose_name_plural = 'Tipos de Servidores'


class RegimenPensionario(models.Model):
    nombre_regimen_pensionario = models.CharField(max_length=45, verbose_name='Nombre de Régimen Pensionario')
    codigo_regimen_pensionario = models.CharField(max_length=2, unique=True, verbose_name='Código de Régimen Pensionario')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_regimen_pensionario

    class Meta:
        db_table = 'regimen_pensionario'
        ordering = ['nombre_regimen_pensionario']
        verbose_name = 'Régimen Pensionario'
        verbose_name_plural = 'Regímenes Pensionarios'


class Afp(models.Model):
    nombre_afp = models.CharField(max_length=45, verbose_name='Nombre de AFP')
    codigo_afp = models.CharField(max_length=2, unique=True, verbose_name='Código de AFP')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_afp

    class Meta:
        db_table = 'afp'
        ordering = ['nombre_afp']
        verbose_name = 'AFP'
        verbose_name_plural = 'AFPs'


class Banco(models.Model):
    nombre_banco = models.CharField(max_length=45, verbose_name='Nombre de Banco')
    codigo_banco = models.CharField(max_length=3, unique=True, verbose_name='Código de Banco')
    abreviatura_banco = models.CharField(max_length=10, verbose_name='Abreviatura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_banco

    class Meta:
        db_table = 'banco'
        ordering = ['nombre_banco']
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

class Situacion(models.Model):
    nombre_situacion = models.CharField(max_length=45, verbose_name='Nombre de Situación')
    abreviatura_situacion = models.CharField(max_length=10, verbose_name='Abreviatura')
    codigo_situacion = models.CharField(max_length=10, unique=True, verbose_name='Código')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_situacion

    class Meta:
        db_table = 'situacion'
        ordering = ['nombre_situacion']
        verbose_name = 'Situación'
        verbose_name_plural = 'Situaciones'

class EstadoCivil(models.Model):
    # el codigo de estado civil debe ser unico
    codigo_estado_civil = models.CharField(max_length=2, unique=True, verbose_name='Código de Estado Civil', null=True, blank=True)
    nombre_estado_civil = models.CharField(max_length=45, verbose_name='Nombre de Estado Civil')
    abreviatura_estado_civil = models.CharField(max_length=10, verbose_name='Abreviatura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_estado_civil

    class Meta:
        db_table = 'estado_civil'
        ordering = ['nombre_estado_civil']
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'

# MCPP Web

class TipoRegistroAirhsp(models.Model):
    pass

class ConceptoRemunerativo(models.Model):
    tipo = models.CharField(max_length=45, verbose_name='Tipo(Si es Haber o Descuento)')
    codigo_mcpp = models.CharField(max_length=4, unique=True, verbose_name='Código MCPP Web')
    codigo_plame = models.CharField(max_length=4, verbose_name='Código Plame')
    descripcion= models.CharField(max_length=100, verbose_name='Descripción de la Norma')
    imponible = models.BooleanField(default=False, verbose_name='Es Imponible?')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class TipoDeCuenta(models.Model):
    pass


class ComisionAfp(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name='Periodo')
    afp = models.ForeignKey(Afp, on_delete=models.CASCADE, verbose_name='AFP')
    comision_flujo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Comisión por Flujo')
    comision_mixta = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Comisión Mixta')
    prima_seguro = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Prima de Seguro')
    aporte_obligatorio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Aporte Obligatorio')
    total_comision = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total Comisión')
    estado = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.afp.nombre_afp + ' - ' + self.periodo.periodo + ' - ' + str(self.total_comision)

    def save(self, *args, **kwargs):
        # Calcular el total_comision
        self.total_comision = self.comision_flujo + self.comision_mixta + self.prima_seguro + self.aporte_obligatorio
        # Llamar al método save de la superclase
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'comision_afp'
        ordering = ['periodo']
        verbose_name = 'Comisión AFP'
        verbose_name_plural = 'Comisiones AFP'
        indexes = [
            models.Index(fields=['periodo', 'afp'], name='idx_comisionafp_periodo_afp'),
        ]


class ConfiguracionGlobal(models.Model):
    clave = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    tipo_dato = models.CharField(max_length=20, choices=[
        ('NUMERIC', 'Numérico'),
        ('TEXT', 'Texto'),
        ('JSON', 'JSON'),
        ('BOOLEAN', 'Booleano'),
        ('DATE', 'Fecha'),
    ])

    def __str__(self):
        return self.clave

class ValorConfiguracionGlobal(models.Model):
    configuracion = models.ForeignKey(ConfiguracionGlobal, on_delete=models.CASCADE, related_name='valores')
    valor = models.TextField()
    norma = models.CharField(max_length=100, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    creado_por = models.ForeignKey('usuarios.User', on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"{self.configuracion.clave}: {self.valor} (desde {self.fecha_inicio})"

    def save(self, *args, **kwargs):
        # Si es un nuevo registro (no tiene ID), cerrar el valor anterior
        if not self.pk:
            ValorConfiguracionGlobal.objects.filter(
                configuracion=self.configuracion,
                fecha_fin__isnull=True
            ).update(fecha_fin=self.fecha_inicio - timezone.timedelta(days=1))

        super().save(*args, **kwargs)


auditlog.register(Ugel)
auditlog.register(ComisionAfp)
auditlog.register(Cargo)
auditlog.register(Periodo)
auditlog.register(TipoPlanilla)
auditlog.register(ClasePlanilla)
auditlog.register(FuenteFinanciamiento)
auditlog.register(Transaccion)
auditlog.register(Banco)
auditlog.register(ConfiguracionGlobal)
auditlog.register(ValorConfiguracionGlobal)```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/serializers.py**
```python
# apps/configuracion/serializers.py
from rest_framework import serializers
from .models import Ugel, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Periodo, Transaccion, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion, TipoDocumento, Sexo, TipoDescuento, TipoBeneficiario, EstadoCivil, ComisionAfp, ConfiguracionGlobal, ValorConfiguracionGlobal

class UgelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugel
        fields = ['id', 'nombre_ugel', 'nombre_corto_ugel']
        ref_name = 'UgelSerializerConfiguracion'

    def validate_codigo_ugel(self, value):
        if not value.isdigit() or len(value) != 3:
            raise serializers.ValidationError("El código de UGEL debe ser un número de 3 dígitos.")
        return value

    def validate_nombre_ugel(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El nombre de la UGEL debe tener al menos 5 caracteres.")
        return value

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

    def validate_periodo(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("El periodo debe ser un número de 6 dígitos (YYYYMM).")
        return value

    def validate(self, data):
        if data.get('es_adicional') and not data.get('estado'):
            raise serializers.ValidationError("Un periodo adicional debe estar activo al crearse.")
        return data

class TipoPlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPlanilla
        fields = '__all__'

class ClasePlanillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasePlanilla
        fields = '__all__'

class FuenteFinanciamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteFinanciamiento
        fields = '__all__'


class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'
        ref_name = 'TransaccionSerializerTransacciones'


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class RegimenLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegimenLaboral
        fields = '__all__'

class TipoServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServidor
        fields = '__all__'

class RegimenPensionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegimenPensionario
        fields = '__all__'

class AfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afp
        fields = '__all__'

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'

class SituacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacion
        fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = '__all__'

class TipoDescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDescuento
        fields = '__all__'

class TipoBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBeneficiario
        fields = '__all__'

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'

class ComisionAfpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComisionAfp
        fields = '__all__'

class ConfiguracionGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionGlobal
        fields = '__all__'

class ValorConfiguracionGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorConfiguracionGlobal
        fields = '__all__'```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/apps.py**
```python
from django.apps import AppConfig


class ConfiguracionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.configuracion'
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/admin.py**
```python
from django.contrib import admin
from .models import Ugel, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Periodo, Transaccion, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion, TipoDocumento, Sexo, EstadoCivil, ComisionAfp, ConfiguracionGlobal, ValorConfiguracionGlobal
from apps.transacciones.models import TransaccionContrato

# Register your models here.
@admin.register(Ugel)
class UgelAdmin(admin.ModelAdmin):
    list_display = ['nombre_ugel', 'nombre_corto_ugel']
    search_fields = ['nombre_ugel', 'nombre_corto_ugel']
    ordering = ['nombre_ugel']

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'es_adicional', 'estado')
    search_fields = ('periodo',)
    list_filter = ('es_adicional',)
    ordering = ('periodo', 'es_adicional')


@admin.register(TipoPlanilla)
class TipoPlanillaAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_planilla', 'codigo_tipo_planilla')
    search_fields = ('nombre_tipo_planilla', 'codigo_tipo_planilla')
    ordering = ('nombre_tipo_planilla',)

@admin.register(ClasePlanilla)
class ClasePlanillaAdmin(admin.ModelAdmin):
    list_display = ('nombre_clase_planilla', 'codigo_clase_planilla', 'tipo_planilla')
    search_fields = ('nombre_clase_planilla', 'codigo_clase_planilla')
    list_filter = ('tipo_planilla',)
    ordering = ('nombre_clase_planilla',)

@admin.register(FuenteFinanciamiento)
class FuenteFinanciamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre_fuente_financiamiento',)
    search_fields = ('nombre_fuente_financiamiento',)
    list_filter = ('nombre_fuente_financiamiento',)
    ordering = ('nombre_fuente_financiamiento',)



class TransaccionTrabajadorInline(admin.TabularInline):
    model = TransaccionContrato
    extra = 1  # Número de formularios adicionales vacíos que se mostrarán

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('codigo_transaccion_mcpp', 'codigo_transaccion_plame', 'descripcion_transaccion', 'tipo_transaccion')
    search_fields = ('codigo_transaccion_mcpp', 'codigo_transaccion_plame', 'descripcion_transaccion', 'tipo_transaccion')
    list_filter = ('tipo_transaccion','imponible')
    ordering = ('codigo_transaccion_mcpp','codigo_transaccion_plame')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cargo',)
    search_fields = ('nombre_cargo',)
    ordering = ('nombre_cargo',)

@admin.register(RegimenLaboral)
class RegimenLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombre_regimen_laboral',)
    search_fields = ('nombre_regimen_laboral',)
    ordering = ('nombre_regimen_laboral',)

@admin.register(TipoServidor)
class TipoServidorAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_servidor',)
    search_fields = ('nombre_tipo_servidor',)
    ordering = ('nombre_tipo_servidor',)

@admin.register(RegimenPensionario)
class RegimenPensionarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_regimen_pensionario',)
    search_fields = ('nombre_regimen_pensionario',)
    ordering = ('nombre_regimen_pensionario',)

@admin.register(Afp)
class AfpAdmin(admin.ModelAdmin):
    list_display = ('nombre_afp',)
    search_fields = ('nombre_afp',)
    ordering = ('nombre_afp',)

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre_banco','codigo_banco','abreviatura_banco')
    search_fields = ('nombre_banco',)
    ordering = ('nombre_banco',)

@admin.register(Situacion)
class SituacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_situacion', 'abreviatura_situacion', 'codigo_situacion', 'created', 'updated')
    search_fields = ('nombre_situacion', 'abreviatura_situacion', 'codigo_situacion')
    ordering = ('nombre_situacion',)

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('descripcion_tipo_documento', 'codigo_tipo_documento')
    search_fields = ('descripcion_tipo_documento', 'codigo_tipo_documento')
    ordering = ('descripcion_tipo_documento',)

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display = ('descripcion_sexo', 'codigo_sexo')
    search_fields = ('descripcion_sexo', 'codigo_sexo')
    ordering = ('descripcion_sexo',)

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado_civil', 'codigo_estado_civil')
    search_fields = ('nombre_estado_civil', 'codigo_estado_civil')
    ordering = ('nombre_estado_civil',)

@admin.register(ComisionAfp)
class ComisionAfpAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'afp', 'total_comision', 'estado')
    search_fields = ('periodo', 'afp')
    list_filter = ('afp','estado')
    ordering = ('periodo', 'afp')

@admin.register(ConfiguracionGlobal)
class ConfiguracionGlobalAdmin(admin.ModelAdmin):
    list_display = ('clave', 'descripcion')
    search_fields = ('clave', 'descripcion')
    ordering = ('clave',)

@admin.register(ValorConfiguracionGlobal)
class ValorConfiguracionGlobalAdmin(admin.ModelAdmin):
    list_display = ('configuracion', 'valor', 'fecha_inicio', 'fecha_fin')
    search_fields = ('configuracion', 'valor')
    list_filter = ('configuracion',)
    ordering = ('configuracion', 'fecha_inicio', 'fecha_fin')```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/tests.py**
```python
from django.test import TestCase

# Create your tests here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/urls.py**
```python
# apps/configuracion/urls.py
from rest_framework.routers import DefaultRouter
from .views import UgelViewSet, TipoPlanillaViewSet, ClasePlanillaViewSet, FuenteFinanciamientoViewSet, PeriodoViewSet, TransaccionViewSet, CargoViewSet, RegimenLaboralViewSet, TipoServidorViewSet, RegimenPensionarioViewSet, AFPViewSet, BancoViewSet, SituacionViewSet, TipoDocumentoViewSet, SexoViewSet, TipoDescuentoViewSet, TipoBeneficiarioViewSet, EstadoCivilViewSet, ComisionAfpViewSet

router = DefaultRouter()
router.register(r'ugels', UgelViewSet)
router.register(r'periodos', PeriodoViewSet)
router.register(r'transacciones', TransaccionViewSet)
router.register(r'tipos-planilla', TipoPlanillaViewSet)
router.register(r'clases-planilla', ClasePlanillaViewSet)
router.register(r'fuentes-financiamiento', FuenteFinanciamientoViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'regimenes-laborales', RegimenLaboralViewSet)
router.register(r'tipos-documento', TipoDocumentoViewSet)
router.register(r'tipos-servidores', TipoServidorViewSet)
router.register(r'regimenes-pensionarios', RegimenPensionarioViewSet)
router.register(r'afps', AFPViewSet)
router.register(r'bancos', BancoViewSet)
router.register(r'situaciones', SituacionViewSet)
router.register(r'sexos', SexoViewSet)
router.register(r'estados-civiles', EstadoCivilViewSet)
router.register(r'tipos-descuento', TipoDescuentoViewSet)
router.register(r'tipos-beneficiario', TipoBeneficiarioViewSet)
router.register(r'comisiones-afp', ComisionAfpViewSet)

urlpatterns = router.urls
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/configuracion/views.py**
```python
from django.shortcuts import render
from rest_framework import viewsets
from .models import Ugel, TipoPlanilla, ClasePlanilla, FuenteFinanciamiento, Periodo, Transaccion, Cargo, RegimenLaboral, TipoServidor, RegimenPensionario, Afp, Banco, Situacion, TipoDocumento, Sexo, TipoDescuento, TipoBeneficiario, EstadoCivil, ComisionAfp, ConfiguracionGlobal, ValorConfiguracionGlobal
from .serializers import UgelSerializer, TipoPlanillaSerializer, ClasePlanillaSerializer, FuenteFinanciamientoSerializer, PeriodoSerializer, TransaccionSerializer, CargoSerializer, RegimenLaboralSerializer, TipoServidorSerializer, RegimenPensionarioSerializer, AfpSerializer, BancoSerializer, SituacionSerializer, TipoDocumentoSerializer, SexoSerializer, TipoDescuentoSerializer, TipoBeneficiarioSerializer, EstadoCivilSerializer, ComisionAfpSerializer, ConfiguracionGlobalSerializer, ValorConfiguracionGlobalSerializer
from rest_framework.permissions import IsAuthenticated

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Create your views here.
class UgelViewSet(viewsets.ModelViewSet):
    queryset = Ugel.objects.all()
    serializer_class = UgelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin_sistema':
            return self.queryset
        return self.queryset.filter(id=user.ugel.id)

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by('-periodo')

class TipoPlanillaViewSet(viewsets.ModelViewSet):
    queryset = TipoPlanilla.objects.all()
    serializer_class = TipoPlanillaSerializer
    permission_classes = [IsAuthenticated]

class ClasePlanillaViewSet(viewsets.ModelViewSet):
    queryset = ClasePlanilla.objects.all()
    serializer_class = ClasePlanillaSerializer
    permission_classes = [IsAuthenticated]

class FuenteFinanciamientoViewSet(viewsets.ModelViewSet):
    queryset = FuenteFinanciamiento.objects.all()
    serializer_class = FuenteFinanciamientoSerializer
    permission_classes = [IsAuthenticated]

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    permission_classes = [IsAuthenticated]

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]

class RegimenLaboralViewSet(viewsets.ModelViewSet):
    queryset = RegimenLaboral.objects.all()
    serializer_class = RegimenLaboralSerializer
    permission_classes = [IsAuthenticated]

class TipoServidorViewSet(viewsets.ModelViewSet):
    queryset = TipoServidor.objects.all()
    serializer_class = TipoServidorSerializer
    permission_classes = [IsAuthenticated]

class RegimenPensionarioViewSet(viewsets.ModelViewSet):
    queryset = RegimenPensionario.objects.all()
    serializer_class = RegimenPensionarioSerializer
    permission_classes = [IsAuthenticated]

class AFPViewSet(viewsets.ModelViewSet):
    queryset = Afp.objects.all()
    serializer_class = AfpSerializer
    permission_classes = [IsAuthenticated]

class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    permission_classes = [IsAuthenticated]

class SituacionViewSet(viewsets.ModelViewSet):
    queryset = Situacion.objects.all()
    serializer_class = SituacionSerializer
    permission_classes = [IsAuthenticated]

class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    serializer_class = SexoSerializer
    permission_classes = [IsAuthenticated]

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    permission_classes = [IsAuthenticated]

class TipoDescuentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDescuento.objects.all()
    serializer_class = TipoDescuentoSerializer
    permission_classes = [IsAuthenticated]

class TipoBeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = TipoBeneficiario.objects.all()
    serializer_class = TipoBeneficiarioSerializer
    permission_classes = [IsAuthenticated]

class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer
    permission_classes = [IsAuthenticated]

class ComisionAfpViewSet(viewsets.ModelViewSet):
    queryset = ComisionAfp.objects.all()
    serializer_class = ComisionAfpSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.select_related('periodo', 'afp').order_by('-periodo__periodo', 'afp__nombre_afp')

class ConfiguracionGlobalViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracionGlobal.objects.all()
    serializer_class = ConfiguracionGlobalSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 15))  # Cache por 15 minutos
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.order_by('clave')

class ValorConfiguracionGlobalViewSet(viewsets.ModelViewSet):
    queryset = ValorConfiguracionGlobal.objects.all()
    serializer_class = ValorConfiguracionGlobalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.select_related('configuracion').order_by('configuracion__clave', '-fecha_inicio', '-fecha_fin')```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/models.py**
```python
# apps/usuarios/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.configuracion.models import TipoDocumento, Sexo, TipoDescuento, TipoBeneficiario, Ugel, EstadoCivil
from django.contrib.auth.models import AbstractUser

from auditlog.registry import auditlog

class User(AbstractUser):
    ADMINISTRADOR_DEL_SISTEMA = 'admin_sistema'
    ADMINISTRADOR_UGEL = 'admin_ugel'
    TECNICO_DE_PROCESOS = 'tecnico_procesos'
    TECNICO_DE_PLANILLAS = 'tecnico_planillas'
    TRABAJADOR = 'trabajador'

    ROLE_CHOICES = [
        (ADMINISTRADOR_DEL_SISTEMA, 'Administrador del Sistema'),
        (ADMINISTRADOR_UGEL, 'Administrador UGEL'),
        (TECNICO_DE_PROCESOS, 'Técnico de Procesos'),
        (TECNICO_DE_PLANILLAS, 'Técnico de Planillas'),
        (TRABAJADOR, 'Trabajador'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=TRABAJADOR,
        verbose_name='Rol'
    )
    ugel = models.ForeignKey(Ugel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='UGEL')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos concedidos a cada uno de sus grupos.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario',
    )
    class Meta:
        indexes = [
            models.Index(fields=['role'], name='idx_user_role'),
            models.Index(fields=['ugel'], name='idx_user_ugel'),
        ]


class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,related_name='persona')
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name='Tipo de Documento')
    numero_documento = models.CharField(max_length=12, unique=True, db_index=True,verbose_name='Número de Documento')
    apellido_paterno = models.CharField(max_length=45, blank=True, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=45, blank=True, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=45, blank=True, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, verbose_name='Sexo')
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, verbose_name='Estado Civil')
    direccion = models.CharField(max_length=100, blank=True, verbose_name='Dirección')
    email = models.EmailField(max_length=45, blank=True, verbose_name='Email')
    telefono = models.CharField(max_length=9, blank=True, verbose_name='Teléfono')

    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'


    def get_full_name(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'.strip()

    def clean(self):
        if self.tipo_documento.codigo_tipo_documento == 'DNI' and len(self.numero_documento) != 8:
            raise ValidationError(_('El DNI debe tener 8 caracteres.'))
        elif self.tipo_documento.codigo_tipo_documento == 'CET' and len(self.numero_documento) != 9:
            raise ValidationError(_('El Carnet de extranjería debe tener 9 caracteres.'))
        elif self.tipo_documento.codigo_tipo_documento == 'PAS' and len(self.numero_documento) != 12:
            raise ValidationError(_('El pasaporte debe tener 12 caracteres.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'persona'
        ordering = ['apellido_paterno', 'apellido_materno', 'nombres']
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        indexes = [
            models.Index(fields=['numero_documento'], name='idx_persona_documento'),
            models.Index(fields=['apellido_paterno', 'apellido_materno', 'nombres'], name='idx_persona_nombre_completo'),
        ]


class Beneficiario(models.Model):
    trabajador = models.ForeignKey(
        'trabajadores.Trabajador', on_delete=models.CASCADE, verbose_name='Empleado', related_name='beneficiarios'
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
    numero_cuenta = models.CharField(max_length=20, blank=True, verbose_name='Número de Cuenta')
    tipo_beneficiario = models.ForeignKey(TipoBeneficiario, on_delete=models.CASCADE, default=1, verbose_name='Tipo de Beneficiario')
    tipo_descuento = models.ForeignKey(TipoDescuento, on_delete=models.CASCADE, default=1, verbose_name='Tipo de Descuento')
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
        'configuracion.Banco', on_delete=models.CASCADE, verbose_name='Banco'
    )

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.paterno} {self.persona.materno}'

    class Meta:
        db_table = 'beneficiario'
        ordering = ['id']
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'
        indexes = [
            models.Index(fields=['trabajador'], name='idx_beneficiario_trabajador'),
            models.Index(fields=['estado'], name='idx_beneficiario_estado'),
        ]

    def clean(self):
        if self.tipo_descuento.codigo == 'MF' and not self.descuento_fijo:
            raise ValidationError('Debe especificar un monto fijo para el descuento.')
        if self.tipo_descuento.codigo == 'DP' and not self.porcentaje_descuento:
            raise ValidationError('Debe especificar un porcentaje para el descuento.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


auditlog.register(User)
auditlog.register(Persona)
auditlog.register(Beneficiario)```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/serializers.py**
```python
# apps/usuarios/serializers.py
from rest_framework import serializers
from .models import Persona, Beneficiario, User
from apps.configuracion.models import Ugel
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UgelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ugel
        fields = ['id', 'nombre_ugel', 'nombre_corto_ugel']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [
            'id', 'user', 'tipo_documento', 'numero_documento', 'apellido_paterno', 
            'apellido_materno', 'nombres', 'fecha_nacimiento', 'sexo', 'estado_civil', 
            'direccion', 'email', 'telefono'
        ]

    def validate_numero_documento(self, value):
        tipo_documento = self.initial_data.get('tipo_documento')
        if tipo_documento == 'DNI' and (not value.isdigit() or len(value) != 8):
            raise serializers.ValidationError("El DNI debe ser un número de 8 dígitos.")
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Ingrese una dirección de correo electrónico válida.")
        return value

    def validate(self, data):
        if data.get('fecha_nacimiento'):
            from datetime import date
            today = date.today()
            age = today.year - data['fecha_nacimiento'].year - ((today.month, today.day) < (data['fecha_nacimiento'].month, data['fecha_nacimiento'].day))
            if age < 18:
                raise serializers.ValidationError("La persona debe ser mayor de 18 años.")
        return data
    
class UserSerializer(serializers.ModelSerializer):
    # persona = PersonaSerializer(read_only=True)
    ugel = UgelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'date_joined', 'ugel']

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 5 caracteres.")
        return value

    def validate(self, data):
        if data.get('role') == 'admin_ugel' and not data.get('ugel'):
            raise serializers.ValidationError("Un administrador UGEL debe tener una UGEL asignada.")
        return data
class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['id', 'trabajador', 'persona', 'relacion_trabajador', 'documento_descuento', 'numero_cuenta', 'tipo_beneficiario', 'tipo_descuento', 'descuento_fijo', 'porcentaje_descuento', 'fecha_inicio', 'fecha_fin', 'estado', 'banco', 'created', 'updated']

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 5 caracteres.")
        return value

    def validate(self, data):
        if data.get('role') == 'admin_ugel' and not data.get('ugel'):
            raise serializers.ValidationError("Un administrador UGEL debe tener una UGEL asignada.")
        return data


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/apps.py**
```python
from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.usuarios'```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/admin.py**
```python
# apps/usuarios/admin.py
from django.contrib import admin
from .models import Persona, Beneficiario, User, Ugel
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('role', 'ugel')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Additional info', {
            'fields': ('role', 'ugel')
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role', 'ugel')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellido_paterno', 'apellido_materno', 'tipo_documento', 'numero_documento', 'email']
    search_fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'numero_documento']
    list_filter = ['tipo_documento', 'sexo']
    ordering = ['apellido_paterno', 'apellido_materno', 'nombres']

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ['persona', 'trabajador', 'tipo_beneficiario', 'tipo_descuento', 'descuento_fijo', 'porcentaje_descuento', 'estado']
    search_fields = ['persona__nombres', 'persona__apellido_paterno', 'persona__apellido_materno', 'empleado__persona__nombres', 'empleado__persona__apellido_paterno', 'empleado__persona__apellido_materno']
    list_filter = ['tipo_beneficiario', 'tipo_descuento', 'estado']
    ordering = ['persona', 'trabajador']```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/tests.py**
```python
from django.test import TestCase

# Create your tests here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/urls.py**
```python
# apps/usuarios/urls.py
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, BeneficiarioViewSet, UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'beneficiarios', BeneficiarioViewSet)


urlpatterns = router.urls
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/usuarios/views.py**
```python
# apps/usuarios/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Persona, Beneficiario, User
from .serializers import PersonaSerializer, BeneficiarioSerializer, UserSerializer

import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

# apps/usuarios/views.py

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

from rest_framework.decorators import action

# Vista personalizada para el login
class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Obtener el nombre de usuario y la contraseña del request
        username = request.data.get("username")
        password = request.data.get("password")

        # Autenticar al usuario
        user = authenticate(username=username, password=password)
        if user is not None:
            # Crear tokens de acceso y refresco para el usuario autenticado
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),  # Token de refresco
                'access': str(refresh.access_token),  # Token de acceso
            }, status=status.HTTP_200_OK)
        # Retornar un error si las credenciales no son válidas
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Vista personalizada para obtener detalles del usuario autenticado
class CustomUserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Serializar y retornar los datos del usuario autenticado
        serializer = UserSerializer(request.user)
        return Response(serializer.data)




class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Sesión cerrada exitosamente"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('ugel')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(ugel=user.ugel)
        return queryset

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('tipo_documento', 'sexo', 'estado_civil')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(user__ugel=user.ugel)
        return queryset
    
    # @action(detail=False, methods=['get', 'put'], url_path='me')
    # def me(self, request):
    #     user = request.user
    #     try:
    #         persona = user.persona  # Asegúrate de que el usuario tenga una persona asociada
    #     except Persona.DoesNotExist:
    #         return Response({"detail": "Perfil no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
    #     if request.method == 'GET':
    #         serializer = self.get_serializer(persona)
    #         return Response(serializer.data)
        
    #     elif request.method == 'PUT':
    #         serializer = self.get_serializer(persona, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)

class BeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('trabajador', 'persona', 'tipo_beneficiario', 'tipo_descuento', 'banco')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(trabajador__ugel=user.ugel)
        return queryset
    
    

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Esta vista requiere autenticación

    def get(self, request):
        # Devolvemos información del usuario autenticado
        return Response({
            "message": "Esta es una vista protegida",
            "user": request.user.username
        })```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/models.py**
```python
# apps/trabajadores/models.py
from django.db import models
from apps.usuarios.models import Persona
from auditlog.registry import auditlog

class Trabajador(models.Model):
    ugel = models.ForeignKey('configuracion.Ugel', on_delete=models.CASCADE, verbose_name='UGEL')
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    #persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Persona', related_name='empleados')
    tiempo_servicios = models.IntegerField(null=True, blank=True, verbose_name='Tiempo de Servicios')
    regimen_pensionario = models.ForeignKey('configuracion.RegimenPensionario', on_delete=models.CASCADE, verbose_name='Régimen Pensionario')
    afp = models.ForeignKey('configuracion.Afp', on_delete=models.CASCADE, verbose_name='AFP')
    cuspp = models.CharField(max_length=12, blank=True, verbose_name='CUSPP')
    fecha_afiliacion = models.DateField(null=True, blank=True, verbose_name='Fecha de Afiliación')
    banco = models.ForeignKey('configuracion.Banco', on_delete=models.CASCADE, verbose_name='Banco')
    numero_cuenta = models.CharField(max_length=45, blank=True, verbose_name='Número de Cuenta')
    ruc = models.CharField(max_length=11, blank=True, verbose_name='RUC')
    estado = models.BooleanField(verbose_name='Estado', default=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.persona.nombres} {self.persona.apellido_paterno} {self.persona.apellido_materno}'

    class Meta:
        db_table = 'trabajador'
        ordering = ['id']
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        indexes = [
            models.Index(fields=['persona'], name='idx_trabajador_persona'),
            models.Index(fields=['ugel'], name='idx_trabajador_ugel'),
            models.Index(fields=['estado'], name='idx_trabajador_estado'),
        ]

auditlog.register(Trabajador)```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/serializers.py**
```python
# apps/trabajadores/serializers.py
from rest_framework import serializers
from .models import Trabajador
from apps.usuarios.serializers import PersonaSerializer
from apps.configuracion.serializers import UgelSerializer, RegimenPensionarioSerializer, AfpSerializer, BancoSerializer

class TrabajadorSerializer(serializers.ModelSerializer):

    persona = PersonaSerializer(read_only=True)
    ugel = UgelSerializer(read_only=True)
    regimen_pensionario = RegimenPensionarioSerializer(read_only=True)
    afp = AfpSerializer(read_only=True)
    banco = BancoSerializer(read_only=True)
    class Meta:
        model = Trabajador
        fields = '__all__'

    def validate_tiempo_servicios(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("El tiempo de servicios no puede ser negativo.")
        return value

    def validate_cuspp(self, value):
        if value and not value.isalnum():
            raise serializers.ValidationError("El CUSPP debe contener solo letras y números.")
        return value

    def validate_numero_cuenta(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("El número de cuenta debe contener solo dígitos.")
        return value

    def validate_ruc(self, value):
        if value and (not value.isdigit() or len(value) != 11):
            raise serializers.ValidationError("El RUC debe ser un número de 11 dígitos.")
        return value
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/apps.py**
```python
from django.apps import AppConfig


class TrabajadoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.trabajadores'
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/admin.py**
```python
# apps/trabajadores/admin.py
from django.contrib import admin
from .models import Trabajador

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('persona', 'estado')
    search_fields = ('persona__nombres', 'persona__apellido_paterno', 'persona__apellido_materno')
    list_filter = ('estado',)
    ordering = ('persona__apellido_paterno', 'persona__apellido_materno', 'persona__nombres')
    autocomplete_fields = ['persona']
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/tests.py**
```python
from django.test import TestCase

# Create your tests here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/urls.py**
```python
from rest_framework.routers import DefaultRouter
from .views import (
    TrabajadorViewSet
)

router = DefaultRouter()
router.register(r'trabajadores', TrabajadorViewSet)

urlpatterns = router.urls
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/trabajadores/views.py**
```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Trabajador
from .serializers import TrabajadorSerializer

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Trabajador.objects.select_related('persona', 'ugel', 'regimen_pensionario', 'afp', 'banco')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(ugel=user.ugel)
        return queryset

```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/models.py**
```python
# apps/transacciones/models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Max
from apps.planillas.models import Contrato
from apps.configuracion.models import Transaccion

from auditlog.registry import auditlog

class TransaccionContrato(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, verbose_name='Contrato', related_name='transacciones')
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, verbose_name='Transacción')
    monto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto')
    periodo_inicial = models.CharField(max_length=6, blank=True, verbose_name='Periodo Inicial')
    periodo_final = models.CharField(max_length=6, blank=True, verbose_name='Periodo Final')
    secuencia = models.IntegerField(verbose_name='Correlativo', editable=False, null=True, blank=True)
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return f'{self.secuencia} - {self.contrato} - {self.monto}'

    class Meta:
        db_table = 'transacciones_trabajadores'
        verbose_name = 'Transacción del Trabajador'
        verbose_name_plural = 'Transacciones de los Trabajadores'
        ordering = ['transaccion', 'secuencia']
        indexes = [
            models.Index(fields=['contrato', 'transaccion'], name='idx_transac_contrato_transac'),
            models.Index(fields=['periodo_inicial', 'periodo_final'], name='idx_transac_contrato_periodo'),
        ]

    def save(self, *args, **kwargs):
        if not self.pk:
            ultimo_secuencia = TransaccionContrato.objects.filter(transaccion=self.transaccion).aggregate(Max('secuencia'))['secuencia__max']
            self.secuencia = (ultimo_secuencia or 0) + 1
        super().save(*args, **kwargs)


auditlog.register(TransaccionContrato)```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/serializers.py**
```python
# apps/transacciones/serializers.py
from rest_framework import serializers
from .models import TransaccionContrato

class TransaccionTrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionContrato
        fields = '__all__'
        ref_name = 'TransaccionTrabajadorSerializerTransacciones'

    def validate(self, data):
        if data['periodo_final'] < data['periodo_inicial']:
            raise serializers.ValidationError("El periodo final no puede ser anterior al periodo inicial.")
        if data['monto'] < 0:
            raise serializers.ValidationError("El monto no puede ser negativo.")
        return data```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/apps.py**
```python
from django.apps import AppConfig


class TransaccionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.transacciones'
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/admin.py**
```python
# apps/transacciones/admin.py
from django.contrib import admin
from .models import TransaccionContrato

@admin.register(TransaccionContrato)
class TransaccionTrabajadorAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'transaccion', 'monto', 'periodo_inicial', 'periodo_final', 'secuencia','estado')
    search_fields = (
        'contrato__trabajador__persona__nombres',
        'contrato__trabajador__persona__apellido_paterno',
        'contrato__trabajador__persona__apellido_materno',
        'transaccion__descripcion_transaccion'
    )
    list_filter = ('estado', 'transaccion__tipo_transaccion')
    ordering = ('transaccion', 'secuencia')
    autocomplete_fields = ['contrato', 'transaccion']
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/tests.py**
```python
from django.test import TestCase

# Create your tests here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/urls.py**
```python
# apps/transacciones/urls.py
from rest_framework.routers import DefaultRouter
from .views import  TransaccionTrabajadorViewSet

router = DefaultRouter()
router.register(r'transacciones-trabajadores', TransaccionTrabajadorViewSet)

urlpatterns = router.urls
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/transacciones/views.py**
```python
# apps/transacciones/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TransaccionContrato
from .serializers import TransaccionTrabajadorSerializer

class TransaccionTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = TransaccionContrato.objects.all()
    serializer_class = TransaccionTrabajadorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = TransaccionContrato.objects.select_related(
            'contrato', 'transaccion', 'contrato__trabajador', 'contrato__trabajador__persona'
        )
        
        if user.role != 'admin_sistema':
            queryset = queryset.filter(contrato__trabajador__ugel=user.ugel)
        
        return queryset.distinct()```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/models.py**
```python
# apps/planillas/models.py
from django.db import models
from apps.trabajadores.models import Trabajador
from apps.usuarios.models import Beneficiario
from apps.configuracion.models import Cargo, RegimenLaboral, TipoServidor, ClasePlanilla, FuenteFinanciamiento, Situacion, Periodo

from auditlog.registry import auditlog



class Contrato(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='contratos')
    centro_de_trabajo = models.CharField(max_length=255, blank=True, verbose_name='Centro de Trabajo')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo')
    fecha_ingreso = models.DateField(null=True, blank=True, verbose_name='Fecha de Ingreso')
    fecha_cese = models.DateField(null=True, blank=True, verbose_name='Fecha de Cese')
    documento_contrato = models.CharField(max_length=45, blank=True, verbose_name='Documento de Contrato')
    documento_cese = models.CharField(max_length=45, blank=True, verbose_name='Documento de Cese')
    regimen_laboral = models.ForeignKey(RegimenLaboral, on_delete=models.CASCADE, verbose_name='Régimen Laboral')
    tipo_servidor = models.ForeignKey(TipoServidor, on_delete=models.CASCADE, verbose_name='Tipo de Servidor')
    clase_planilla = models.ForeignKey(ClasePlanilla, on_delete=models.CASCADE, verbose_name='Clase de Planilla')
    fuente_financiamiento = models.ForeignKey(FuenteFinanciamiento, on_delete=models.CASCADE, verbose_name='Fuente de Financiamiento')
    sueldo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Sueldo')
    dias_laborados = models.IntegerField(null=True, blank=True, verbose_name='Días Laborados', default=30)
    leyenda_permanente = models.CharField(max_length=255, blank=True, verbose_name='Leyenda Permanente')
    jornada_laboral = models.IntegerField(null=True, blank=True, verbose_name='Jornada Laboral', default=48)
    situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE, verbose_name='Situación')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.trabajador.persona.get_full_name()} - {self.cargo} - {self.fecha_ingreso} - {self.fecha_cese}'

    class Meta:
        db_table = 'contrato'
        ordering = ['id']
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        indexes = [
            models.Index(fields=['trabajador'], name='idx_contrato_trabajador'),
            models.Index(fields=['clase_planilla', 'fuente_financiamiento'], name='idx_contrato_clase_fuente'),
            models.Index(fields=['fecha_ingreso', 'fecha_cese'], name='idx_contrato_fechas'),
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



class Planilla(models.Model):
    ESTADO_CHOICES = [
        ('APERTURADO', 'Aperturado'),
        ('CERRADO', 'Cerrado')
    ]

    correlativo = models.CharField(max_length=5, verbose_name='Correlativo')
    clase_planilla = models.ForeignKey(ClasePlanilla, on_delete=models.CASCADE, verbose_name='Clase de Planilla')
    fuente_financiamiento = models.ForeignKey(FuenteFinanciamiento, on_delete=models.CASCADE, verbose_name='Fuente de Financiamiento')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name='Período')
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes')
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos')
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='APERTURADO', verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('correlativo', 'periodo')
        db_table = 'planilla'
        indexes = [
            models.Index(fields=['periodo', 'estado'], name='idx_planilla_periodo_estado'),
            models.Index(fields=['clase_planilla', 'fuente_financiamiento'], name='idx_planilla_clase_fuente'),
        ]

    def __str__(self):
        return f'{self.correlativo} - {self.clase_planilla} - {self.fuente_financiamiento} - {self.periodo} - {self.estado}'

class Boleta(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='boletas')
    planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, related_name='boletas')
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes')
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos')
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes')
    neto_a_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Neto a Pagar')
    numero_boleta = models.CharField(max_length=3, verbose_name='Número de Boleta', editable=False)
    visualizada = models.BooleanField(default=False, verbose_name='Visualizada', editable=False)
    fecha_visualizacion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Visualización', editable=False)
    descargada = models.BooleanField(default=False, verbose_name='Descargada', editable=False)
    fecha_descarga = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Descarga', editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Datos del contrato en el momento de la generación de la boleta
    centro_de_trabajo = models.CharField(max_length=255, blank=True, verbose_name='Centro de Trabajo')
    cargo = models.CharField(max_length=255, blank=True, verbose_name='Cargo')
    fecha_ingreso = models.DateField(null=True, blank=True, verbose_name='Fecha de Ingreso')
    fecha_cese = models.DateField(null=True, blank=True, verbose_name='Fecha de Cese')
    clase_planilla = models.CharField(max_length=255, blank=True, verbose_name='Clase de Planilla')
    fuente_financiamiento = models.CharField(max_length=255, blank=True, verbose_name='Fuente de Financiamiento')
    sueldo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Sueldo')
    dias_laborados = models.IntegerField(null=True, blank=True, verbose_name='Días Laborados', default=30)
    leyenda_permanente = models.CharField(max_length=255, blank=True, verbose_name='Leyenda Permanente')
    jornada_laboral = models.IntegerField(null=True, blank=True, verbose_name='Jornada Laboral', default=48)

    # Datos del trabajador en el momento de la generación de la boleta
    trabajador_nombres = models.CharField(max_length=255, verbose_name='Nombres del Trabajador')
    trabajador_apellidos = models.CharField(max_length=255, verbose_name='Apellidos del Trabajador')
    trabajador_dni = models.CharField(max_length=20, verbose_name='DNI del Trabajador')
    regimen_laboral = models.CharField(max_length=255, blank=True, verbose_name='Régimen Laboral')
    tipo_servidor = models.CharField(max_length=255, blank=True, verbose_name='Tipo de Servidor')
    regimen_pensionario = models.CharField(max_length=255, blank=True, verbose_name='Régimen Pensionario')
    banco = models.CharField(max_length=255, blank=True, verbose_name='Banco')
    cuenta_bancaria = models.CharField(max_length=255, blank=True, verbose_name='Cuenta Bancaria')

    # Totales calculados
    total_haberes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Haberes', editable=False)
    total_descuentos = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Descuentos', editable=False)
    total_aportes = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Total Aportes', editable=False)
    neto_a_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Neto a Pagar', editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.contrato} - {self.planilla} - {self.planilla.periodo}'

    class Meta:
        db_table = 'boleta'
        ordering = ['planilla', 'contrato']
        unique_together = ('contrato', 'planilla')
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'
        indexes = [
            models.Index(fields=['contrato', 'planilla'], name='idx_boleta_contrato_planilla'),
            models.Index(fields=['visualizada', 'descargada'], name='idx_boleta_estado'),
        ]

class BoletaTransaccion(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, related_name='transacciones')
    tipo = models.CharField(max_length=50, verbose_name='Tipo de Transacción')
    codigo = models.CharField(max_length=50, verbose_name='Código de Transacción')
    descripcion = models.CharField(max_length=255, verbose_name='Descripción de Transacción')
    monto = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Monto')

    class Meta:
        db_table = 'boleta_transacciones'
        verbose_name = 'Boleta Transacción'
        verbose_name_plural = 'Boleta Transacciones'


class PlanillaBeneficiario(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name='Beneficiario')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name='Período')
    monto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Monto')

    def __str__(self):
        return f'{self.beneficiario.persona.nombres} {self.beneficiario.persona.paterno} {self.beneficiario.persona.materno} - {self.periodo}'

    class Meta:
        db_table = 'planilla_beneficiario'
        ordering = ['id']
        verbose_name = 'Planilla del Beneficiario'
        verbose_name_plural = 'Planillas de los Beneficiarios'


auditlog.register(Contrato)
auditlog.register(Planilla)
auditlog.register(Boleta)
auditlog.register(BoletaTransaccion)
auditlog.register(PlanillaBeneficiario)
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/serializers.py**
```python
# apps/planillas/serializers.py
from rest_framework import serializers
from .models import Periodo, PlanillaBeneficiario, Contrato, Planilla, Boleta, BoletaTransaccion
from django.db import transaction
from apps.transacciones.models import TransaccionContrato

class BoletaTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoletaTransaccion
        fields = '__all__'
        extra_kwargs = {
            'contrato': {'required': False, 'allow_null': True},
            'transaccion': {'required': False, 'allow_null': True},
        }
        ref_name = 'BoletaTransaccionSerializerPlanillas'
# La clase de abajo se usa para poder registrar transacciones al momento de crear o actualizar un contrato
class TransaccionContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionContrato
        fields = '__all__'

class PlanillaBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanillaBeneficiario
        fields = '__all__'
        ref_name = 'PlanillaBeneficiarioSerializerPlanillas'

    def validate_monto(self, value):
        if value < 0:
            raise serializers.ValidationError("El monto no puede ser negativo.")
        return value

class ContratoSerializer(serializers.ModelSerializer):
    transacciones = TransaccionContratoSerializer(many=True, write_only=True, required=False)
    transacciones_detalles = TransaccionContratoSerializer(many=True, read_only=True, source='transacciones')

    class Meta:
        model = Contrato
        fields = '__all__'

    def validate(self, data):
        if 'fecha_cese' in data and data['fecha_cese'] and data['fecha_cese'] <= data['fecha_ingreso']:
            raise serializers.ValidationError("La fecha de cese debe ser posterior a la fecha de ingreso.")
        if data['dias_laborados'] < 0 or data['dias_laborados'] > 30:
            raise serializers.ValidationError("Los días laborados deben estar entre 0 y 30.")
        if data.get('sueldo') and data['sueldo'] <= 0:
            raise serializers.ValidationError("El sueldo debe ser mayor que cero.")
        if data['jornada_laboral'] < 0 or data['jornada_laboral'] > 48:
            raise serializers.ValidationError("La jornada laboral debe estar entre 0 y 48 horas.")
        return data


    def validate_sueldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("El sueldo debe ser mayor que cero.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        transacciones_data = validated_data.pop('transacciones', [])
        contrato = Contrato.objects.create(**validated_data)
        for transaccion_data in transacciones_data:
            if transaccion_data:
                TransaccionContrato.objects.create(contrato=contrato, **transaccion_data)
        return contrato

    @transaction.atomic
    def update(self, instance, validated_data):
        transacciones_data = validated_data.pop('transacciones', [])
        instance = super().update(instance, validated_data)

        if transacciones_data:
            instance.transacciones.all().delete()
            for transaccion_data in transacciones_data:
                if transaccion_data:
                    TransaccionContrato.objects.create(contrato=instance, **transaccion_data)

        return instance

class PlanillaSerializer(serializers.ModelSerializer):
    contratos = ContratoSerializer(many=True, required=False)

    class Meta:
        model = Planilla
        fields = '__all__'

    def validate_correlativo(self, value):
        if len(value) != 3:
            raise serializers.ValidationError("El correlativo debe tener 3 caracteres.")
        return value

    def validate(self, data):
        if data['total_haberes'] < 0:
            raise serializers.ValidationError("El total de haberes no puede ser negativo.")
        if data['total_descuentos'] < 0:
            raise serializers.ValidationError("El total de descuentos no puede ser negativo.")
        if data['total_aportes'] < 0:
            raise serializers.ValidationError("El total de aportes no puede ser negativo.")
        if data['estado'] not in dict(Planilla.ESTADO_CHOICES):
            raise serializers.ValidationError("El estado no es válido.")
        return data

    def create(self, validated_data):
        contratos_data = validated_data.pop('contratos', [])
        planilla = Planilla.objects.create(**validated_data)
        for contrato_data in contratos_data:
            if contrato_data:  # Verificar que contrato_data no esté vacío
                contrato = Contrato.objects.create(**contrato_data)
                planilla.contratos.add(contrato)
        return planilla

    def update(self, instance, validated_data):
        contratos_data = validated_data.pop('contratos', [])
        instance = super().update(instance, validated_data)

        if contratos_data:
            instance.contratos.all().delete()  # Elimina los contratos existentes
            for contrato_data in contratos_data:
                if contrato_data:  # Verificar que contrato_data no esté vacío
                    contrato = Contrato.objects.create(**contrato_data)
                    instance.contratos.add(contrato)

        return instance




class BoletaSerializer(serializers.ModelSerializer):
    planilla = PlanillaSerializer(read_only=True)
    contrato = ContratoSerializer(read_only=True)

    class Meta:
        model = Boleta
        fields = '__all__'

    def validate(self, data):
        if data['total_haberes'] < 0:
            raise serializers.ValidationError("El total de haberes no puede ser negativo.")
        if data['total_descuentos'] < 0:
            raise serializers.ValidationError("El total de descuentos no puede ser negativo.")
        if data['total_aportes'] < 0:
            raise serializers.ValidationError("El total de aportes no puede ser negativo.")
        if data['neto_a_pagar'] < 0:
            raise serializers.ValidationError("El neto a pagar no puede ser negativo.")
        return data```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/apps.py**
```python
from django.apps import AppConfig


class PlanillasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.planillas'
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/admin.py**
```python
# apps/planillas/admin.py
from django.contrib import admin
from .models import  PlanillaBeneficiario, Contrato, Planilla, Boleta, BoletaTransaccion
from apps.configuracion.admin import TransaccionTrabajadorInline

@admin.register(PlanillaBeneficiario)
class PlanillaBeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('beneficiario', 'periodo', 'monto')
    search_fields = ('beneficiario__persona__nombres', 'beneficiario__persona__paterno', 'beneficiario__persona__materno')
    list_filter = ('periodo',)
    ordering = ('beneficiario', 'periodo')
# apps/trabajadores/admin.py

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'fuente_financiamiento', 'cargo', 'fecha_ingreso', 'fecha_cese', 'situacion')
    search_fields = ('trabajador__persona__nombres', 'trabajador__persona__apellido_paterno', 'trabajador__persona__apellido_materno', 'cargo__nombre_cargo')
    list_filter = ('situacion', 'cargo', 'fecha_ingreso', 'fecha_cese')
    ordering = ('trabajador', 'fecha_ingreso')
    autocomplete_fields = ['trabajador', 'cargo', 'clase_planilla', 'fuente_financiamiento']
    inlines = [TransaccionTrabajadorInline]


@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display = ('numero_boleta', 'planilla', 'contrato', 'total_haberes', 'total_descuentos', 'total_aportes', 'neto_a_pagar')
    search_fields = ('numero_boleta', 'planilla__correlativo', 'contrato__trabajador__persona__nombres')
    list_filter = ('visualizada', 'descargada', 'planilla__periodo')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('contrato', 'planilla')
        return queryset



from apps.procesos.periodo_normal import CalcularPlanillaRemuneraciones, GenerarBoletasPago

@admin.action(description='Generar boletas para esta planilla')
def generar_boletas(modeladmin, request, queryset):
    for planilla in queryset:
        GenerarBoletasPago(planilla.id)
    modeladmin.message_user(request, "Boletas generadas exitosamente.")

@admin.action(description='Calcular planilla de remuneraciones')
def calcular_planilla_remuneraciones(modeladmin, request, queryset):
    for planilla in queryset:
        CalcularPlanillaRemuneraciones(planilla.id)
    modeladmin.message_user(request, "Planillas de remuneraciones calculadas exitosamente.")


@admin.register(Planilla)
class PlanillaAdmin(admin.ModelAdmin):
    list_display = ('correlativo', 'clase_planilla', 'fuente_financiamiento', 'periodo', 'total_haberes', 'total_descuentos', 'total_aportes', 'estado')
    actions = [generar_boletas, calcular_planilla_remuneraciones]
    search_fields = ('correlativo', 'clase_planilla__nombre', 'fuente_financiamiento__nombre')
    list_filter = ('estado', 'periodo', 'clase_planilla', 'fuente_financiamiento')
    ordering = ('correlativo', 'periodo')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('clase_planilla', 'fuente_financiamiento', 'periodo')
        return queryset


@admin.register(BoletaTransaccion)
class BoletaTransaccionAdmin(admin.ModelAdmin):
    list_display = ('boleta', 'tipo', 'codigo', 'descripcion', 'monto')
    search_fields = ('boleta__numero_boleta', 'tipo', 'codigo', 'descripcion')
    list_filter = ('tipo', 'codigo')
    ordering = ('boleta', 'tipo', 'codigo')```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/tests.py**
```python
from django.test import TestCase

# Create your tests here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/urls.py**
```python
# apps/planillas/urls.py
from rest_framework.routers import DefaultRouter
from .views import PlanillaBeneficiarioViewSet,ContratoViewSet, PlanillaViewSet, BoletaViewSet, BoletaTransaccionViewSet

router = DefaultRouter()
router.register(r'contratos', ContratoViewSet)
router.register(r'planillas', PlanillaViewSet)
router.register(r'boletas', BoletaViewSet)

router.register(r'planillas-beneficiarios', PlanillaBeneficiarioViewSet)
router.register(r'boleta-transaccion', BoletaTransaccionViewSet)


urlpatterns = router.urls
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/planillas/views.py**
```python
# apps/planillas/views.py
from django.db.models import Max
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PlanillaBeneficiario, Contrato, Planilla, Boleta, BoletaTransaccion
from .serializers import PlanillaBeneficiarioSerializer, ContratoSerializer, PlanillaSerializer, BoletaSerializer, BoletaTransaccionSerializer
from apps.transacciones.models import TransaccionContrato
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
        queryset = Contrato.objects.select_related(
            'trabajador', 'trabajador__persona', 'cargo', 'regimen_laboral',
            'tipo_servidor', 'clase_planilla', 'fuente_financiamiento', 'situacion'
        ).prefetch_related('transacciones')
        
        if user.role != 'admin_sistema':
            queryset = queryset.filter(trabajador__ugel=user.ugel)
        
        return queryset
class ProcesarPlanillaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        periodo = request.data.get('periodo')
        if not periodo:
            return Response({"error": "Debe especificar un período."}, status=status.HTTP_400_BAD_REQUEST)

        transacciones = TransaccionContrato.objects.filter(
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
        queryset = Planilla.objects.select_related('clase_planilla', 'fuente_financiamiento', 'periodo')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(boletas__contrato__trabajador__ugel=user.ugel)
        return queryset.distinct()
class BoletaViewSet(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Boleta.objects.select_related(
            'contrato', 'planilla', 'contrato__trabajador', 'contrato__trabajador__persona'
        ).prefetch_related('transacciones')
        
        if user.role != 'admin_sistema':
            queryset = queryset.filter(contrato__trabajador__ugel=user.ugel)
        
        return queryset
class BoletaTransaccionViewSet(viewsets.ModelViewSet):
    queryset = BoletaTransaccion.objects.all()
    serializer_class = BoletaTransaccionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = BoletaTransaccion.objects.select_related(
            'boleta', 'boleta__contrato', 'boleta__planilla',
            'boleta__contrato__trabajador', 'boleta__contrato__trabajador__persona'
        )
        
        if user.role != 'admin_sistema':
            queryset = queryset.filter(boleta__contrato__trabajador__ugel=user.ugel)
        
        return queryset.distinct()```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/models.py**
```python
# apps/auditoria/models.py
from django.db import models
from apps.usuarios.models import Persona

class Auditoria(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    descripcion = models.TextField(verbose_name='Descripción')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name='Persona')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name='Dirección IP')
    user_agent = models.CharField(max_length=255, null=True, blank=True, verbose_name='User Agent')
    accion = models.CharField(max_length=50, verbose_name='Acción')

    class Meta:
        db_table = 'auditoria'
        ordering = ['-fecha']
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
        indexes = [
            models.Index(fields=['fecha', 'accion'], name='idx_auditoria_fecha_accion'),
            models.Index(fields=['persona'], name='idx_auditoria_persona'),
        ]
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/serializers.py**
```python
# apps/auditoria/serializers.py
from rest_framework import serializers
from .models import Auditoria

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = ['id', 'fecha', 'descripcion', 'persona', 'ip_address', 'user_agent', 'accion']

    def validate_ip_address(self, value):
        import ipaddress
        try:
            ipaddress.ip_address(value)
        except ValueError:
            raise serializers.ValidationError("Dirección IP inválida.")
        return value```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/__init__.py**
```python
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/apps.py**
```python
from django.apps import AppConfig


class AuditoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.auditoria'
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/admin.py**
```python
# apps/auditoria/admin.py
from django.contrib import admin
from .models import Auditoria

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'descripcion', 'persona', 'ip_address', 'user_agent', 'accion']
    search_fields = ['descripcion', 'persona__nombres', 'persona__paterno', 'persona__materno', 'ip_address', 'accion']
    list_filter = ['fecha', 'accion']
    ordering = ['-fecha']
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/tests.py**
```python
from django.test import TestCase

# Create your tests here.
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/urls.py**
```python
# apps/auditoria/urls.py
from rest_framework.routers import DefaultRouter
from .views import AuditoriaViewSet

router = DefaultRouter()
router.register(r'auditorias', AuditoriaViewSet)

urlpatterns = router.urls
```

**Ruta: /Volumes/Datos/Trabajo/Sistemas/Planilla/backend/planillas/apps/auditoria/views.py**
```python
# apps/auditoria/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Auditoria
from .serializers import AuditoriaSerializer

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.select_related('persona').order_by('-fecha')
        if user.role != 'admin_sistema':
            queryset = queryset.filter(persona__user__ugel=user.ugel)
        return queryset```

