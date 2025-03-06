from django.db import models
from app.alumnos.models import Alumno

# Modelo InfoPadresTutoresLegales
class InfoPadresTutoresLegales(models.Model):
    id_tutor = models.AutoField(primary_key=True, db_column="id_tutor")
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno", db_column="id_alumno") # No entiendo porqué pero es necesario meter un on_delete=models.CASCADE/PROTECT O LO QUE SEA
    mama_nombre = models.CharField(max_length=50, verbose_name="Nombre de la Madre", db_column="mama_nombre")
    mama_apellido = models.CharField(max_length=50, verbose_name="Apellido de la Madre", db_column="mama_apellido")
    mama_cedula = models.CharField(max_length=20, verbose_name="Cédula de la Madre", db_column="mama_cedula")
    mama_telefono = models.CharField(max_length=20, verbose_name="Teléfono de la Madre", db_column="mama_telefono")
    mama_email = models.EmailField(max_length=50, verbose_name="Email de la Madre", db_column="mama_email")
    mama_empresa = models.CharField(max_length=100, verbose_name="Empresa de la Madre", db_column="mama_empresa")
    papa_nombre = models.CharField(max_length=50, verbose_name="Nombre del Padre", db_column="papa_nombre")
    papa_apellido = models.CharField(max_length=50, verbose_name="Apellido del Padre", db_column="papa_apellido")
    papa_cedula = models.CharField(max_length=20, verbose_name="Cédula del Padre", db_column="papa_cedula")
    papa_telefono = models.CharField(max_length=20, verbose_name="Teléfono del Padre", db_column="papa_telefono")
    papa_email = models.EmailField(max_length=50, verbose_name="Email del Padre", db_column="papa_email")
    papa_empresa = models.CharField(max_length=100, verbose_name="Empresa del Padre", db_column="papa_empresa")
    direccion = models.CharField(max_length=100, verbose_name="Dirección", null=True, db_column="direccion")
     

    def __str__(self):
        return f"Tutor de {self.id_alumno.alumno_nombre} {self.id_alumno.alumno_apellidos}"
    
    class Meta:
        db_table = 'info_padres_tutores_legales'