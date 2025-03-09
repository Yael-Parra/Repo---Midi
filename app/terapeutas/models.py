from django.db import models

class Terapeuta(models.Model):
    id_terapeuta = models.AutoField(primary_key=True, db_column="id_terapeuta")
    terapeuta_nombre = models.CharField(max_length=50, verbose_name="Nombre del Terapeuta", db_column="terapeuta_nombre")
    terapeuta_apellidos = models.CharField(max_length=50, verbose_name="Apellidos del Terapeuta", db_column="terapeuta_apellidos")
    terapeuta_cedula = models.CharField(max_length=20, verbose_name="Cédula del Terapeuta", db_column="terapeuta_cedula")
    terapeuta_telefono = models.CharField(max_length=20, verbose_name="Teléfono del Terapeuta", db_column="terapeuta_telefono")
    terapeuta_email = models.EmailField(max_length=50, verbose_name="Email del Terapeuta", db_column="terapeuta_email")

    def __str__(self):
        return f"{self.terapeuta_nombre} {self.terapeuta_apellidos}"
    
    class Meta:
        db_table = 'terapeutas'