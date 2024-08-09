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
}