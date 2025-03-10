from django.test import TestCase
from .models import Inscripcion
from app.alumnos.models import Alumno
from app.cursos.models import Curso
from app.colegios.models import Colegio
from django.urls import reverse

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

    # def test_inscripcion_str(self):
    #     self.assertEqual(str(self.inscripcion), "Inscripción 1 - Juan en Matemáticas")

    # def test_inscripcion_creation_view(self):
    #     response = self.client.post(reverse('inscripcion_create'), {
    #         'id_alumno': self.alumno.id_alumno,
    #         'id_curso': self.curso.id_curso,
    #         'id_colegio': self.colegio.id_colegio
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(Inscripcion.objects.filter(id_alumno=self.alumno, id_curso=self.curso).exists())

    # def test_inscripcion_list_view(self):
    #     response = self.client.get(reverse('inscripcion_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Juan')

    # def test_inscripcion_detail_view(self):
    #     response = self.client.get(reverse('inscripcion_detail', args=[self.inscripcion.id_inscripcion]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Juan')

    # def test_inscripcion_update_view(self):
    #     response = self.client.post(reverse('inscripcion_update', args=[self.inscripcion.id_inscripcion]), {
    #         'id_alumno': self.alumno.id_alumno,
    #         'id_curso': self.curso.id_curso,
    #         'id_colegio': self.colegio.id_colegio
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.inscripcion.refresh_from_db()
    #     self.assertEqual(self.inscripcion.id_alumno.alumno_nombre, 'Juan')

    # def test_inscripcion_delete_view(self):
    #     response = self.client.post(reverse('inscripcion_delete', args=[self.inscripcion.id_inscripcion]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(Inscripcion.objects.filter(id=self.inscripcion.id_inscripcion).exists())