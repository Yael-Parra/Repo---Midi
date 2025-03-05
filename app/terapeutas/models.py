from django.db import models

# Modelo Terapeuta
class Terapeuta(models.Model):
    id_terapeuta = models.AutoField(primary_key=True)
    terapeuta_nombre = models.CharField(max_length=50, verbose_name="Nombre del Terapeuta")
    terapeuta_apellidos = models.CharField(max_length=50, verbose_name="Apellidos del Terapeuta")
    terapeuta_cedula = models.CharField(max_length=20, verbose_name="Cédula del Terapeuta")
    terapeuta_telefono = models.CharField(max_length=20, verbose_name="Teléfono del Terapeuta")
    terapeuta_email = models.EmailField(max_length=50, verbose_name="Email del Terapeuta")

    def __str__(self):
        return f"{self.terapeuta_nombre} {self.terapeuta_apellidos}"
    class Meta:
        db_table = 'terapeutas'
