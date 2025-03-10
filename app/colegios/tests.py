from django.test import TestCase
from .models import Colegio
from django.urls import reverse

class ColegioModelTest(TestCase):

    def setUp(self):
        self.colegio = Colegio.objects.create(nombre_colegio="Colegio Nacional")

    def test_colegio_creation(self):
        self.assertEqual(self.colegio.nombre_colegio, "Colegio Nacional")

    # def test_colegio_str(self):
    #     self.assertEqual(str(self.colegio), "Colegio Nacional")

    # def test_colegio_creation_view(self):
    #     response = self.client.post(reverse('colegio_create'), {
    #         'nombre_colegio': 'Colegio Internacional'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(Colegio.objects.filter(nombre_colegio='Colegio Internacional').exists())

    # def test_colegio_list_view(self):
    #     response = self.client.get(reverse('colegio_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Colegio Nacional')

    # def test_colegio_detail_view(self):
    #     response = self.client.get(reverse('colegio_detail', args=[self.colegio.id_colegio]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Colegio Nacional')

    # def test_colegio_update_view(self):
    #     response = self.client.post(reverse('colegio_update', args=[self.colegio.id_colegio]), {
    #         'nombre_colegio': 'Colegio Nacional Actualizado'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.colegio.refresh_from_db()
    #     self.assertEqual(self.colegio.nombre_colegio, 'Colegio Nacional Actualizado')

    # def test_colegio_delete_view(self):
    #     response = self.client.post(reverse('colegio_delete', args=[self.colegio.id_colegio]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(Colegio.objects.filter(id=self.colegio.id_colegio).exists())