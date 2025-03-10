from django.contrib import admin
from .models import Colegio


# Personalización del panel de administración para el modelo Colegio
class ColegioAdmin(admin.ModelAdmin):
    list_display = ('id_colegio', 'nombre_colegio')
    search_fields = ('nombre_colegio',)
    list_filter = ('nombre_colegio',)

    class Meta:
        db_table = 'colegios'


admin.site.register(Colegio, ColegioAdmin)
