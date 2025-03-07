from django.db import models

# Modelo Alumno
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True, db_column='id_alumno')
    alumno_nombre = models.CharField(max_length=50, verbose_name="Nombre del Alumno", db_column='alumno_nombre')
    alumno_apellidos = models.CharField(max_length=50, verbose_name="Apellidos del Alumno", db_column='alumno_apellidos')
    alumno_fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Nacimiento", db_column="alumno_fecha_nacimiento")  # Permitir nulos

    def __str__(self):
        return f"{self.alumno_nombre} {self.alumno_apellidos}"

    class Meta:
        db_table = "alumnos"