# app/alumnos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarAlumno/', views.registrarAlumno, name='registrar_alumno'),
    path('edicionAlumno/<int:id_alumno>/', views.edicionAlumno, name='edicion_alumno'),
    path('editarAlumno/', views.editarAlumno, name='editar_alumno'),
    path('eliminarAlumno/<int:id_alumno>/', views.eliminarAlumno, name='eliminar_alumno'),
]