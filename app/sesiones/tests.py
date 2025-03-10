from django.test import TestCase
from .models import Sesion
from app.alumnos.models import Alumno
from app.cursos.models import Curso
from app.terapeutas.models import Terapeuta
from django.urls import reverse

class SesionModelTest(TestCase):

    def setUp(self):
        self.alumno = Alumno.objects.create(
            alumno_nombre="Juan",
            alumno_apellidos="Pérez",
            alumno_fecha_nacimiento="2000-01-01"
        )
        self.curso = Curso.objects.create(nombre_curso="Matemáticas")
        self.terapeuta = Terapeuta.objects.create(
            terapeuta_nombre="Ana",
            terapeuta_apellidos="García",
            terapeuta_cedula="123456789",
            terapeuta_telefono="123456789",
            terapeuta_email="ana@example.com"
        )
        self.sesion = Sesion.objects.create(
            id_alumno=self.alumno,
            id_curso=self.curso,
            id_terapeuta=self.terapeuta,
            fecha_sesion="2025-01-01 10:00:00",
            asistencia=True,
            observaciones="Buena sesión"
        )

    def test_sesion_creation(self):
        self.assertEqual(self.sesion.id_alumno.alumno_nombre, "Juan")
        self.assertEqual(self.sesion.id_curso.nombre_curso, "Matemáticas")
        self.assertEqual(self.sesion.id_terapeuta.terapeuta_nombre, "Ana")
        self.assertEqual(str(self.sesion.fecha_sesion), "2025-01-01 10:00:00")
        self.assertTrue(self.sesion.asistencia)
        self.assertEqual(self.sesion.observaciones, "Buena sesión")

    def test_sesion_str(self):
        self.assertEqual(str(self.sesion), "Sesión para Juan en Matemáticas con Ana el 2025-01-01 10:00:00")

    def test_sesion_list_view(self):
        response = self.client.get(reverse('sesion_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Juan')

    def test_sesion_detail_view(self):
        response = self.client.get(reverse('sesion_detail', args=[self.sesion.id_sesion]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Juan')

    def test_sesion_update_view(self):
        response = self.client.post(reverse('sesion_update', args=[self.sesion.id_sesion]), {
            'id_alumno': self.alumno.id_alumno,
            'id_curso': self.curso.id_curso,
            'id_terapeuta': self.terapeuta.id_terapeuta,
            'fecha_sesion': '2025-01-01 10:00:00',
            'asistencia': True,
            'observaciones': 'Buena sesión'
        })
        self.assertEqual(response.status_code, 302)
        self.sesion.refresh_from_db()
        self.assertEqual(self.sesion.id_alumno.alumno_nombre, 'Juan')

    def test_sesion_delete_view(self):
        response = self.client.post(reverse('sesion_delete', args=[self.sesion.id_sesion]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Sesion.objects.filter(id=self.sesion.id_sesion).exists())