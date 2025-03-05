from django.contrib import admin
from .models import (Curso)


# Personalización del panel de administración para el modelo Curso
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id_curso", "nombre_curso", "id_colegio")
    search_fields = ("nombre_curso",)
    list_filter = ("id_colegio",)

    class Meta:
        db_table = "cursos"


# Registro de modelos en el panel de administración

admin.site.register(Curso, CursoAdmin)
