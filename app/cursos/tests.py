from django.test import TestCase
from .models import Curso
from app.colegios.models import Colegio

class CursoModelTest(TestCase):

    def setUp(self):
        self.colegio = Colegio.objects.create(nombre_colegio="Colegio Nacional")
        self.curso = Curso.objects.create(nombre_curso="Matemáticas", id_colegio=self.colegio)

    def test_curso_creation(self):
        self.assertEqual(self.curso.nombre_curso, "Matemáticas")
        self.assertEqual(self.curso.id_colegio.nombre_colegio, "Colegio Nacional")

    def test_curso_str(self):
        self.assertEqual(str(self.curso), "Matemáticas")
