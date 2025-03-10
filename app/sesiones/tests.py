from django.test import TestCase
from .models import Sesion
from app.alumnos.models import Alumno
from app.cursos.models import Curso
from app.terapeutas.models import Terapeuta

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
