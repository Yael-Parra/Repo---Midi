# app/colegios/urls.py

from django.urls import path, include
from rest_framework import routers
from . import views

# Configuración de las rutas de la API RESTful
router = routers.DefaultRouter()
router.register(r'colegios', views.ColegioViewSet)  # Registra el ViewSet de la API

# Rutas para las vistas basadas en funciones (HTML)
urlpatterns = [
    # Rutas para la interfaz web (HTML)
    path('', views.lista_colegios, name='lista_colegios'),
    path('detalle/<int:id>/', views.detalle_colegio, name='detalle_colegio'),

    # Rutas para la API RESTful
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.lista_colegios, name='lista_colegios'),  # Vista para listar colegios
#     path('detalle/<int:id>/', views.detalle_colegio, name='detalle_colegio'),  # Vista de detalle de un colegio
# ]