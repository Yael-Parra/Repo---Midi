from django.contrib import admin
from .models import Terapeuta


# Personalización del panel de administración para el modelo Terapeuta
class TerapeutaAdmin(admin.ModelAdmin):
    list_display = ('id_terapeuta', 'terapeuta_nombre', 'terapeuta_apellidos', 'terapeuta_cedula')
    search_fields = ('terapeuta_nombre', 'terapeuta_apellidos')
    list_filter = ('terapeuta_nombre',)

    class Meta:
        db_table = 'terapeutas'


admin.site.register(Terapeuta, TerapeutaAdmin)