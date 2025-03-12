"""
URL configuration for config_global project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# config_global/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from app.terapeutas.views import TerapeutaViewSet
from app.alumnos.views import AlumnoViewSet
from app.cursos.views import CursoViewSet
from app.colegios.views import ColegioViewSet
from app.inscripciones.views import InscripcionViewSet
from app.info_padres_tutores_legales.views import InfoPadreTutorViewSet
from app.sesiones.views import SesionViewSet

# Configuración de las rutas de la API RESTful
router = routers.DefaultRouter()
router.register(r'terapeutas', TerapeutaViewSet)  # API para terapeutas
router.register(r'alumnos', AlumnoViewSet)  # API para alumnos
router.register(r'cursos', CursoViewSet)  # API para cursos
router.register(r'colegios', ColegioViewSet)  # API para colegios
router.register(r'inscripciones', InscripcionViewSet)  # API para inscripciones
router.register(r'info_padres_tutores_legales', InfoPadreTutorViewSet)  # API para info_padres_tutores_legales
router.register(r'sesiones', SesionViewSet)  # API para sesiones

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Rutas para la interfaz web
    path('terapeutas/', include('app.terapeutas.urls')),  # Interfaz web de terapeutas
    path('alumnos/', include('app.alumnos.urls')),  # Interfaz web de alumnos
    path('cursos/', include('app.cursos.urls')),  # Interfaz web de cursos
    path('colegios/', include('app.colegios.urls')),  # Interfaz web de colegios
    path('inscripciones/', include('app.inscripciones.urls')),  # Interfaz web de inscripciones
    path('info_padres_tutores_legales/', include('app.info_padres_tutores_legales.urls')),  # Interfaz web de info_padres_tutores_legales
    path('sesiones/', include('app.sesiones.urls')),  # Interfaz web de sesiones

    # Rutas para la API RESTful
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de la API

    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Redirección por defecto a la página de login
    path('', RedirectView.as_view(url='login/', permanent=False)),
]