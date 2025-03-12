# app/terapeutas/urls.py
# app/terapeutas/urls.py
from django.urls import path
from . import views

# Rutas para las vistas basadas en funciones (HTML)
urlpatterns = [
    path('', views.lista_terapeutas, name='lista_terapeutas'),  # Lista de terapeutas
    path('detalle/<int:id>/', views.detalle_terapeuta, name='detalle_terapeuta'),  # Detalle de un terapeuta
    path('crear/', views.crear_terapeuta, name='crear_terapeuta'),  # Crear un terapeuta
    path('editar/<int:id>/', views.editar_terapeuta, name='editar_terapeuta'),  # Editar un terapeuta
    path('eliminar/<int:id>/', views.eliminar_terapeuta, name='eliminar_terapeuta'),  # Eliminar un terapeuta
]

# from django.urls import path
# from . import views  # Asegúrate de que tus vistas estén importadas

# urlpatterns = [
#     path('', views.lista_terapeutas, name='lista_terapeutas'),  # Vista para listar terapeutas
#     path('detalle/<int:id>/', views.detalle_terapeuta, name='detalle_terapeuta'),  # Vista de detalle de un terapeuta
#     path('crear/', views.crear_terapeuta, name='crear_terapeuta'),  # Vista para crear un nuevo terapeuta
#     path('editar/<int:id>/', views.editar_terapeuta, name='editar_terapeuta'),  # Vista para editar un terapeuta existente
#     path('eliminar/<int:id>/', views.eliminar_terapeuta, name='eliminar_terapeuta'),  # Vista para eliminar un terapeuta

# ]