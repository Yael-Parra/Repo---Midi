from django.test import TestCase
from .models import Curso
from app.colegios.models import Colegio
from django.urls import reverse

class CursoModelTest(TestCase):

    def setUp(self):
        self.colegio = Colegio.objects.create(nombre_colegio="Colegio Nacional")
        self.curso = Curso.objects.create(nombre_curso="Matemáticas", id_colegio=self.colegio)

    def test_curso_creation(self):
        self.assertEqual(self.curso.nombre_curso, "Matemáticas")
        self.assertEqual(self.curso.id_colegio.nombre_colegio, "Colegio Nacional")

    def test_curso_str(self):
        self.assertEqual(str(self.curso), "Matemáticas")

    def test_curso_creation_view(self):
        response = self.client.post(reverse('curso_create'), {
            'nombre_curso': 'Ciencias',
            'id_colegio': self.colegio.id_colegio
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Curso.objects.filter(nombre_curso='Ciencias').exists())

    def test_curso_list_view(self):
        response = self.client.get(reverse('curso_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Matemáticas')

    def test_curso_detail_view(self):
        response = self.client.get(reverse('curso_update', args=[self.curso.id_curso]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Matemáticas')

    def test_curso_update_view(self):
        response = self.client.post(reverse('curso_update', args=[self.curso.id_curso]), {
            'nombre_curso': 'Física',
            'id_colegio': self.colegio.id_colegio
        })
        self.assertEqual(response.status_code, 302)
        self.curso.refresh_from_db()
        self.assertEqual(self.curso.nombre_curso, 'Física')

    def test_curso_delete_view(self):
        response = self.client.post(reverse('curso_delete', args=[self.curso.id_curso]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Curso.objects.filter(id=self.curso.id_curso).exists())