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
]