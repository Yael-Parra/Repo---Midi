from django.contrib import admin
from .models import (InfoPadresTutoresLegales)


# Personalización del panel de administración para el modelo InfoPadresTutoresLegales
class InfoPadresTutoresLegalesAdmin(admin.ModelAdmin):
    list_display = (
        "id_tutor",
        "id_alumno",
        "mama_nombre",
        "mama_apellido",
        "papa_nombre",
        "papa_apellido",
        "mama_telefono",
        "papa_telefono",
    )
    search_fields = ("mama_nombre", "mama_apellido", "papa_nombre", "papa_apellido")
    list_filter = ("id_alumno",)

    class Meta:
        db_table = "info_padres_tutores_legales"

# Registro de modelos en el panel de administración
admin.site.register(InfoPadresTutoresLegales, InfoPadresTutoresLegalesAdmin)

