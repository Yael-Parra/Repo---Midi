from django.test import TestCase
from .models import InfoPadresTutoresLegales
from app.alumnos.models import Alumno

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

