from django.test import TestCase
from .models import Terapeuta

class TerapeutaModelTest(TestCase):

    def setUp(self):
        self.terapeuta = Terapeuta.objects.create(
            terapeuta_nombre="Ana",
            terapeuta_apellidos="García",
            terapeuta_cedula="123456789",
            terapeuta_telefono="123456789",
            terapeuta_email="ana@example.com"
        )

    def test_terapeuta_creation(self):
        self.assertEqual(self.terapeuta.terapeuta_nombre, "Ana")
        self.assertEqual(self.terapeuta.terapeuta_apellidos, "García")
        self.assertEqual(self.terapeuta.terapeuta_cedula, "123456789")
        self.assertEqual(self.terapeuta.terapeuta_telefono, "123456789")
        self.assertEqual(self.terapeuta.terapeuta_email, "ana@example.com")

    def test_terapeuta_str(self):
        self.assertEqual(str(self.terapeuta), "Ana García")

