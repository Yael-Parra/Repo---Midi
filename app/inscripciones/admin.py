from django.contrib import admin
from .models import Inscripcion

# Personalización del panel de administración para el modelo Inscripcion
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'id_alumno', 'id_curso', 'id_colegio', 'fecha_inscripcion')
    search_fields = ('id_alumno__alumno_nombre', 'id_curso__nombre_curso')
    list_filter = ('fecha_inscripcion',)

    class Meta:
        db_table = 'inscripciones'


# Registro de modelos en el panel de administración
admin.site.register(Inscripcion, InscripcionAdmin)
