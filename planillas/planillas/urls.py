# planillas/urls.py (o el archivo principal de urls del proyecto)
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sistema de Planillas API",
        default_version='v1',
        description="Documentación de la API del Sistema de Planillas",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
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
