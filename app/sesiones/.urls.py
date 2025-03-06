# app/sesiones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('sesiones/', views.lista_sesiones, name='lista_sesiones'),  # Lista de todas las sesiones
    path('sesiones/detalle/<int:id>/', views.detalle_sesion, name='detalle_sesion'),  # Detalle de una sesión
    path('sesiones/crear/', views.crear_sesion, name='crear_sesion'),  # Crear una nueva sesión
    path('sesiones/editar/<int:id>/', views.editar_sesion, name='editar_sesion'),  # Editar una sesión
    path('sesiones/eliminar/<int:id>/', views.eliminar_sesion, name='eliminar_sesion'),  # Eliminar una sesión
]
