from django.db import models
from app.alumnos.models import Alumno

# Modelo InfoPadresTutoresLegales
class InfoPadresTutoresLegales(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    mama_nombre = models.CharField(max_length=50, verbose_name="Nombre de la Madre")
    mama_apellido = models.CharField(max_length=50, verbose_name="Apellido de la Madre")
    mama_cedula = models.CharField(max_length=20, verbose_name="Cédula de la Madre")
    mama_telefono = models.CharField(max_length=20, verbose_name="Teléfono de la Madre")
    mama_email = models.EmailField(max_length=50, verbose_name="Email de la Madre")
    mama_empresa = models.CharField(max_length=100, verbose_name="Empresa de la Madre")
    papa_nombre = models.CharField(max_length=50, verbose_name="Nombre del Padre")
    papa_apellido = models.CharField(max_length=50, verbose_name="Apellido del Padre")
    papa_cedula = models.CharField(max_length=20, verbose_name="Cédula del Padre")
    papa_telefono = models.CharField(max_length=20, verbose_name="Teléfono del Padre")
    papa_email = models.EmailField(max_length=50, verbose_name="Email del Padre")
    papa_empresa = models.CharField(max_length=100, verbose_name="Empresa del Padre")
    direccion = models.CharField(max_length=100, verbose_name="Dirección")
    id_alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, verbose_name="Alumno") # No entiendo porqué pero es necesario meter u on_delete=models.CASCADE

    def __str__(self):
        return f"Tutor de {self.id_alumno.alumno_nombre} {self.id_alumno.alumno_apellidos}"
    class Meta:
        db_table = 'info_padres_tutores_legales'