from django.test import TestCase
from .models import Inscripcion
from app.alumnos.models import Alumno
from app.cursos.models import Curso
from app.colegios.models import Colegio

class InscripcionModelTest(TestCase):

    def setUp(self):
        self.alumno = Alumno.objects.create(
            alumno_nombre="Juan",
            alumno_apellidos="Pérez",
            alumno_fecha_nacimiento="2000-01-01"
        )
        self.colegio = Colegio.objects.create(nombre_colegio="Colegio Nacional")
        self.curso = Curso.objects.create(nombre_curso="Matemáticas", id_colegio=self.colegio)
        self.inscripcion = Inscripcion.objects.create(
            id_alumno=self.alumno,
            id_curso=self.curso,
            id_colegio=self.colegio
        )

    def test_inscripcion_creation(self):
        self.assertEqual(self.inscripcion.id_alumno.alumno_nombre, "Juan")
        self.assertEqual(self.inscripcion.id_curso.nombre_curso, "Matemáticas")
        self.assertEqual(self.inscripcion.id_colegio.nombre_colegio, "Colegio Nacional")

    def test_inscripcion_str(self):
        self.assertEqual(str(self.inscripcion), "Inscripción 1 - Juan en Matemáticas")
