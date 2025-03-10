from django.test import TestCase
from .models import Alumno
from django.urls import reverse
from django.core.management import call_command

class AlumnoModelTest(TestCase):

    def setUp(self):
        self.alumno = Alumno.objects.create(
            alumno_nombre="Juan",
            alumno_apellidos="Pérez",
            alumno_fecha_nacimiento="2000-01-01"
        )

    def test_alumno_creation(self):
        self.assertEqual(self.alumno.alumno_nombre, "Juan")
        self.assertEqual(self.alumno.alumno_apellidos, "Pérez")
        self.assertEqual(str(self.alumno.alumno_fecha_nacimiento), "2000-01-01")

    def test_alumno_str(self):
        self.assertEqual(str(self.alumno), "Juan Pérez")

    def test_alumno_creation_view(self):
        response = self.client.post(reverse('alumno_create'), {
            'alumno_nombre': 'Carlos',
            'alumno_apellidos': 'Gómez',
            'alumno_fecha_nacimiento': '1995-05-15'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Alumno.objects.filter(alumno_nombre='Carlos').exists())