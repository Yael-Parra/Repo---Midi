# app/sesiones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.SesionListView.as_view(), name='sesion_list'),
    path('nueva/', views.SesionCreateView.as_view(), name='sesion_create'),
    path('<int:pk>/', views.SesionDetailView.as_view(), name='sesion_detail'),
    path('<int:pk>/editar/', views.SesionUpdateView.as_view(), name='sesion_update'),
    path('<int:pk>/eliminar/', views.SesionDeleteView.as_view(), name='sesion_delete'),
]