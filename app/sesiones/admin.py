from django.db import models
from app.alumnos.models import Alumno
from app.cursos.models import Curso
from app.terapeutas.models import Terapeuta

# app/sesiones/admin.py

from django.contrib import admin
from .models import Sesion


# Personalización del panel de administración para el modelo Sesion
class SesionAdmin(admin.ModelAdmin):
    list_display = (
        "id_sesion", 
        "id_alumno", 
        "id_curso", 
        "id_terapeuta", 
        "fecha_sesion", 
        "asistencia", 
        "observaciones"
    )
    search_fields = ("id_alumno__alumno_nombre", "id_terapeuta__terapeuta_nombre", "id_curso__nombre_curso")
    list_filter = ("fecha_sesion", "asistencia", "id_curso")

    class Meta:
        db_table = "sesion"

# Registra el modelo en el admin
admin.site.register(Sesion, SesionAdmin)
