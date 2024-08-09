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
