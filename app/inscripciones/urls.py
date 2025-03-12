# app/inscripciones/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

# Configuración de las rutas de la API RESTful
router = routers.DefaultRouter()
router.register(r'inscripciones', views.InscripcionViewSet)  # Registra el ViewSet de la API

# Rutas para las vistas basadas en funciones (HTML)
urlpatterns = [
    # Rutas para la interfaz web (HTML)
    path('', views.lista_inscripciones, name='lista_inscripciones'),
    path('detalle/<int:id>/', views.detalle_inscripcion, name='detalle_inscripcion'),
    path('crear/', views.crear_inscripcion, name='crear_inscripcion'),
    path('editar/<int:id>/', views.editar_inscripcion, name='editar_inscripcion'),
    path('eliminar/<int:id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),

    # Rutas para la API RESTful
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API
]


# # app/inscripciones/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.lista_inscripciones, name='lista_inscripciones'),  # Vista para listar inscripciones
#     path('detalle/<int:id>/', views.detalle_inscripcion, name='detalle_inscripcion'),  # Vista de detalle de una inscripción
# ]