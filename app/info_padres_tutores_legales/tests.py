from django.test import TestCase
from .models import InfoPadresTutoresLegales
from app.alumnos.models import Alumno
from django.urls import reverse


class InfoPadresTutoresLegalesModelTest(TestCase):

    def setUp(self):
        self.alumno = Alumno.objects.create(
            alumno_nombre="Juan",
            alumno_apellidos="Pérez",
            alumno_fecha_nacimiento="2000-01-01"
        )
        self.info = InfoPadresTutoresLegales.objects.create(
            id_alumno=self.alumno,
            mama_nombre="María",
            mama_apellido="Gómez",
            papa_nombre="José",
            papa_apellido="Pérez"
        )

    def test_info_creation(self):
        self.assertEqual(self.info.mama_nombre, "María")
        self.assertEqual(self.info.mama_apellido, "Gómez")
        self.assertEqual(self.info.papa_nombre, "José")
        self.assertEqual(self.info.papa_apellido, "Pérez")

    def test_info_str(self):
        self.assertEqual(str(self.info), "Tutor de Juan Pérez")

    # def test_info_creation_view(self):
    #     response = self.client.post(reverse('info_create'), {
    #         'id_alumno': self.alumno.id_alumno,
    #         'mama_nombre': 'Ana',
    #         'mama_apellido': 'López',
    #         'papa_nombre': 'Carlos',
    #         'papa_apellido': 'Martínez'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(InfoPadresTutoresLegales.objects.filter(mama_nombre='Ana').exists())

    # def test_info_list_view(self):
    #     response = self.client.get(reverse('info_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'María Gómez')

    # def test_info_detail_view(self):
    #     response = self.client.get(reverse('info_detail', args=[self.info.id_tutor]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'María Gómez')

    # def test_info_update_view(self):
    #     response = self.client.post(reverse('info_update', args=[self.info.id_tutor]), {
    #         'id_alumno': self.alumno.id_alumno,
    #         'mama_nombre': 'María',
    #         'mama_apellido': 'Gómez',
    #         'papa_nombre': 'José',
    #         'papa_apellido': 'Pérez'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.info.refresh_from_db()
    #     self.assertEqual(self.info.mama_nombre, 'María')

    # def test_info_delete_view(self):
    #     response = self.client.post(reverse('info_delete', args=[self.info.id_tutor]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(InfoPadresTutoresLegales.objects.filter(id=self.info.id_tutor).exists())