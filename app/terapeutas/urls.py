# app/terapeutas/urls.py

from django.urls import path
from . import views  # Asegúrate de que tus vistas estén importadas

urlpatterns = [
    path('', views.lista_terapeutas, name='lista_terapeutas'),  # Vista para listar terapeutas
    path('detalle/<int:id>/', views.detalle_terapeuta, name='detalle_terapeuta'),  # Vista de detalle de un terapeuta
    path('crear/', views.crear_terapeuta, name='crear_terapeuta'),  # Vista para crear un nuevo terapeuta
    path('editar/<int:id>/', views.editar_terapeuta, name='editar_terapeuta'),  # Vista para editar un terapeuta existente
    path('eliminar/<int:id>/', views.eliminar_terapeuta, name='eliminar_terapeuta'),  # Vista para eliminar un terapeuta
]