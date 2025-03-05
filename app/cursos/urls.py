# app/cursos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),  # Vista para listar cursos
    path('detalle/<int:id>/', views.detalle_curso, name='detalle_curso'),  # Vista de detalle de un curso
    path('crear/', views.crear_curso, name='crear_curso'),  # Vista para crear un nuevo curso
]