from django.db import models

# Modelo Alumno
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=50, verbose_name="Nombre del Alumno")
    alumno_apellidos = models.CharField(max_length=50, verbose_name="Apellidos del Alumno")
    alumno_fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento")  # Permitir nulos

    def __str__(self):
        return f"{self.alumno_nombre} {self.alumno_apellidos}"

    class Meta:
        db_table = "alumnos"