# models.py
from django.db import models
from app.colegios.models import Colegio

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True, db_column='id_curso')
    id_colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, verbose_name="Colegio", null=True, blank=True, db_column="id_colegio")
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre del Curso", null=True, blank=True, db_column="nombre_curso")
    
    def __str__(self):
        return self.nombre_curso
    
    class Meta:
        db_table = 'cursos'





'''
from django.db import models
from app.colegios.models import Colegio  # Importa el modelo Colegio desde la carpeta app

# Modelo Curso
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True, db_column='id_curso')
    id_colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, verbose_name="Colegio", null=True, blank=True, db_column="id_colegio")
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre del Curso", null=True, blank=True, db_column="nombre_curso")

    def __str__(self):
        return self.nombre_curso

    class Meta:
        db_table = 'cursos''
        ''
        '''