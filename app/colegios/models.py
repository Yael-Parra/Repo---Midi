from django.db import models

# Modelo Colegio
class Colegio(models.Model):
    id_colegio = models.AutoField(primary_key=True)
    nombre_colegio = models.CharField(max_length=100, verbose_name="Nombre del Colegio")

    def __str__(self):
        return self.colegio
    class Meta:
        db_table = 'colegios'