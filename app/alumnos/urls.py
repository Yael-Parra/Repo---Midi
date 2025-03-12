# app/alumnos/urls.py

# app/alumnos/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

# Configuración de las rutas de la API RESTful
router = routers.DefaultRouter()
router.register(r'alumnos', views.AlumnoViewSet)  # Registra el ViewSet de la API

# Rutas para las vistas basadas en funciones (HTML)
urlpatterns = [
    # Rutas para la interfaz web (HTML)
    path('', views.home, name='home'),
    path('registrarAlumno/', views.registrarAlumno, name='registrar_alumno'),
    path('edicionAlumno/<int:id_alumno>/', views.edicionAlumno, name='edicion_alumno'),
    path('editarAlumno/', views.editarAlumno, name='editar_alumno'),
    path('eliminarAlumno/<int:id_alumno>/', views.eliminarAlumno, name='eliminar_alumno'),

    # Rutas para la API RESTful
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API
]





# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('registrarAlumno/', views.registrarAlumno, name='registrar_alumno'),
#     path('edicionAlumno/<int:id_alumno>/', views.edicionAlumno, name='edicion_alumno'),
#     path('editarAlumno/', views.editarAlumno, name='editar_alumno'),
#     path('eliminarAlumno/<int:id_alumno>/', views.eliminarAlumno, name='eliminar_alumno'),
# ]