# app/alumnos/urls.py

from django.urls import path
from . import views  # Asegúrate de que tus vistas estén importadas

urlpatterns = [
    path('', views.index, name='index'),  # Vista principal de alumnos
    path('detalle/<int:id>/', views.detalle, name='detalle'),  # Vista de detalle de un alumno
    path('crear/', views.crear_alumno, name='crear_alumno'),  # Vista para crear un nuevo alumno
    path('editar/<int:id>/', views.editar_alumno, name='editar_alumno'),  # Vista para editar un alumno
]