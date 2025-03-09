from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/nuevo/', views.AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/<int:id_alumno>/', views.alumno_detail, name='alumno_detail'),
    path('alumnos/<int:id_alumno>/editar/', views.AlumnoUpdateView.as_view(), name='alumno_update'),
    path('alumnos/<int:id_alumno>/eliminar/', views.AlumnoDeleteView.as_view(), name='alumno_delete'),
]