from django.db import models

# Modelo Colegio
class Colegio(models.Model):
    id_colegio = models.AutoField(primary_key=True, db_column='id_colegio')
    nombre_colegio = models.CharField(max_length=100, verbose_name="Nombre del Colegio", db_column='nombre_colegio')

    def __str__(self):
        return self.nombre_colegio
    class Meta:
        db_table = 'colegios'