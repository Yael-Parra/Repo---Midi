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

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', include('app.alumnos.urls')),  # Incluye las URLs de la aplicación alumnos
    path('cursos/', include('app.cursos.urls')),  # Incluye las URLs de la aplicación cursos
    path('colegios/', include('app.colegios.urls')),  # Incluye las URLs de la aplicación colegios
    path('inscripciones/', include('app.inscripciones.urls')),  # Incluye las URLs de la aplicación inscripciones
    path('info_padres_tutores_legales/', include('app.info_padres_tutores_legales.urls')),
    path('sesiones/', include('app.sesiones.urls')),  # Incluye las URLs de la aplicación info_padres_tutores_legales
    path('terapeutas/', include('app.terapeutas.urls')),  # Incluye las URLs de la aplicación terapeutas

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', RedirectView.as_view(url='login/', permanent=False)),
]

