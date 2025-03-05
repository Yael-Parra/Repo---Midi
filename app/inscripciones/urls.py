# app/inscripciones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_inscripciones, name='lista_inscripciones'),  # Vista para listar inscripciones
    path('detalle/<int:id>/', views.detalle_inscripcion, name='detalle_inscripcion'),  # Vista de detalle de una inscripción
]