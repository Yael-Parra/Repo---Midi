# app/colegios/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_colegios, name='lista_colegios'),  # Vista para listar colegios
    path('detalle/<int:id>/', views.detalle_colegio, name='detalle_colegio'),  # Vista de detalle de un colegio
]