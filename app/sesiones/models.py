from django.db import models
from app.alumnos.models import Alumno
from app.terapeutas.models import Terapeuta
from app.cursos.models import Curso

class Sesion(models.Model):
    id_sesion = models.AutoField(primary_key=True)

    id_alumno = models.ForeignKey('alumnos.Alumno', on_delete=models.CASCADE, db_column="id_alumno")
    id_curso = models.ForeignKey('cursos.Curso', on_delete=models.CASCADE, db_column="id_curso")
    id_terapeuta = models.ForeignKey('terapeutas.Terapeuta', on_delete=models.CASCADE, db_column="id_terapeuta")

    fecha_sesion = models.DateTimeField(blank=True, null=True, db_column="fecha_sesion")
    asistencia = models.BooleanField(blank=True, null=True, db_column="asistencia")
    observaciones = models.TextField(blank=True, null=True, db_column="observaciones")

    def __str__(self):
        return f"Sesión para {self.id_alumno.alumno_nombre} en {self.id_curso.nombre_curso} con {self.id_terapeuta.terapeuta_nombre} el {self.fecha_sesion}"
    
    class Meta:
        db_table = 'sesiones'


    
    

