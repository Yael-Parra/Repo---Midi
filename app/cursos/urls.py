# app/cursos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.CursoListView.as_view(), name='curso_list'),
    path('crear/', views.CursoCreateView.as_view(), name='curso_create'),
    path('<int:curso_id>/editar/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('<int:curso_id>/eliminar/', views.CursoDeleteView.as_view(), name='curso_delete'),
]