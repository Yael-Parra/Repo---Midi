# app/terapeutas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.TerapeutaListView.as_view(), name='lista_terapeutas'),
    path('terapeutas/buscar/', views.buscar_terapeutas, name='buscar_terapeutas'),
    path('terapeutas/<int:id_terapeuta>/', views.TerapeutaDetailView.as_view(), name='detalle_terapeuta'),
    path('terapeutas/crear/', views.TerapeutaCreateView.as_view(), name='crear_terapeuta'),
    path('terapeutas/<int:id_terapeuta>/editar/', views.TerapeutaUpdateView.as_view(), name='editar_terapeuta'),
    path('terapeutas/<int:id_terapeuta>/eliminar/', views.TerapeutaDeleteView.as_view(), name='eliminar_terapeuta'),
]