from django.db import models
# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    def str(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)