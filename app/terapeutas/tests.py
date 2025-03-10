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

    def test_terapeuta_update(self):
        self.terapeuta.terapeuta_nombre = "Maria"
        self.terapeuta.save()
        self.assertEqual(self.terapeuta.terapeuta_nombre, "Maria")

    def test_terapeuta_delete(self):
        terapeuta_id = self.terapeuta.id_terapeuta
        self.terapeuta.delete()
        with self.assertRaises(Terapeuta.DoesNotExist):
            Terapeuta.objects.get(id_terapeuta=terapeuta_id)

    def test_terapeuta_email_format(self):
        self.terapeuta.terapeuta_email = "ana@example.com"
        self.terapeuta.full_clean()  # This will validate the model fields