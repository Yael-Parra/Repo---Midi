from django.contrib import admin
from .models import Alumno


# Customization of the administration panel for the Alumno model
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("id_alumno","alumno_nombre","alumno_apellidos", "alumno_fecha_nacimiento",)
    search_fields = ("alumno_nombre", "alumno_apellidos")
    list_filter = ("alumno_nombre",)

    class Meta:
        db_table = "alumno"

admin.site.register(Alumno, AlumnoAdmin)