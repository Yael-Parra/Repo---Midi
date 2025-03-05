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
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye las URLs de las aplicaciones
    path('alumnos/', include('app.alumnos.urls')),  # Asegúrate de que exista un archivo urls.py en app/alumnos
    path('cursos/', include('app.cursos.urls')),    # Asegúrate de que exista un archivo urls.py en app/cursos
    path('colegios/', include('app.colegios.urls')), # Asegúrate de que exista un archivo urls.py en app/colegios
    path('inscripciones/', include('app.inscripciones.urls')), # Asegúrate de que exista un archivo urls.py en app/inscripciones
    path('info_padres_tutores_legales/', include('app.info_padres_tutores_legales.urls')), # Asegúrate de que exista un archivo urls.py en app/info_padres_tutores_legales
    path('terapeutas/', include('app.terapeutas.urls')), # Asegúrate de que exista un archivo urls.py en app/terapeutas
]