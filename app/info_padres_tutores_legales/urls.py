# app/info_padres_tutores_legales/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_info, name='lista_info'),  # Vista para listar información de padres/tutores
    path('detalle/<int:id>/', views.detalle_info, name='detalle_info'),  # Vista de detalle de información
]