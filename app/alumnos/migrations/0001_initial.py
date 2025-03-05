# Generated by Django 5.1.6 on 2025-03-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alumno",
            fields=[
                ("id_alumno", models.AutoField(primary_key=True, serialize=False)),
                (
                    "alumno_nombre",
                    models.CharField(max_length=50, verbose_name="Nombre del Alumno"),
                ),
                (
                    "alumno_apellidos",
                    models.CharField(
                        max_length=50, verbose_name="Apellidos del Alumno"
                    ),
                ),
                (
                    "alumno_fecha_nacimiento",
                    models.DateField(verbose_name="Fecha de Nacimiento"),
                ),
            ],
            options={
                "db_table": "alumnos",
            },
        ),
    ]
