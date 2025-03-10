from django.db import models
from app.alumnos.models import Alumno  
from app.cursos.models import Curso  
from app.colegios.models import Colegio

# Modelo Inscripcion
class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True, verbose_name="ID de Inscripción", db_column="id_inscripcion")
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno", db_column="id_alumno")
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso", db_column="id_curso")
    id_colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, verbose_name="Colegio", null=True, blank=True, db_column="id_colegio")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inscripción", db_column="fecha_inscripcion")
    fecha_baja = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Baja", db_column="fecha_baja")

    def __str__(self):
        return f"Inscripción {self.id_inscripcion} - {self.id_alumno.alumno_nombre} en {self.id_curso.nombre_curso}"

    class Meta:
        db_table = 'inscripciones'