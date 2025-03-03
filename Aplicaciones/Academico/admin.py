from django.contrib import admin
from .models import Alumno, InfoPadresTutoresLegales, Terapeuta, Colegio, Curso, Inscripcion, Sesion

# Registro de modelos en el panel de administración
admin.site.register(Alumno)
admin.site.register(InfoPadresTutoresLegales)
admin.site.register(Terapeuta)
admin.site.register(Colegio)
admin.site.register(Curso)
admin.site.register(Inscripcion)
admin.site.register(Sesion)