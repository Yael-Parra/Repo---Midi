from django.urls import path
from . import views  # Asegura que importas el módulo views

urlpatterns = [
    path('', views.home, name='home'),  # Ahora views.home estará definido correctamente
]
