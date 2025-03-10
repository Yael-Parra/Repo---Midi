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

    def test_alumno_list_view(self):
        response = self.client.get(reverse('alumno_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Juan Pérez')

    def test_alumno_detail_view(self):
        response = self.client.get(reverse('alumno_detail', args=[self.alumno.id_alumno]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Juan Pérez')

    def test_alumno_update_view(self):
        response = self.client.post(reverse('alumno_update', args=[self.alumno.id_alumno]), {
            'alumno_nombre': 'Juan',
            'alumno_apellidos': 'Pérez',
            'alumno_fecha_nacimiento': '2000-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.alumno.refresh_from_db()
        self.assertEqual(self.alumno.alumno_nombre, 'Juan')

    def test_alumno_delete_view(self):
        response = self.client.post(reverse('alumno_delete', args=[self.alumno.id_alumno]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Alumno.objects.filter(id=self.alumno.id_alumno).exists())