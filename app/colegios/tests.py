from django.test import TestCase
from .models import Colegio

class ColegioModelTest(TestCase):

    def setUp(self):
        self.colegio = Colegio.objects.create(nombre_colegio="Colegio Nacional")

    def test_colegio_creation(self):
        self.assertEqual(self.colegio.nombre_colegio, "Colegio Nacional")

    def test_colegio_str(self):
        self.assertEqual(str(self.colegio), "Colegio Nacional")