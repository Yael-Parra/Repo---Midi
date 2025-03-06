# Generated by Django 5.1.7 on 2025-03-06 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alumnos", "0002_alter_alumno_alumno_fecha_nacimiento"),
        ("colegios", "0001_initial"),
        ("cursos", "0002_alter_curso_id_colegio_alter_curso_nombre_curso"),
        ("inscripciones", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inscripcion",
            name="fecha_baja",
            field=models.DateTimeField(
                blank=True,
                db_column="fecha_baja",
                null=True,
                verbose_name="Fecha de Baja",
            ),
        ),
        migrations.AlterField(
            model_name="inscripcion",
            name="fecha_inscripcion",
            field=models.DateTimeField(
                auto_now_add=True,
                db_column="fecha_inscripcion",
                verbose_name="Fecha de Inscripción",
            ),
        ),
        migrations.AlterField(
            model_name="inscripcion",
            name="id_alumno",
            field=models.ForeignKey(
                db_column="id_alumno",
                on_delete=django.db.models.deletion.CASCADE,
                to="alumnos.alumno",
                verbose_name="Alumno",
            ),
        ),
        migrations.AlterField(
            model_name="inscripcion",
            name="id_colegio",
            field=models.ForeignKey(
                blank=True,
                db_column="id_colegio",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="colegios.colegio",
                verbose_name="Colegio",
            ),
        ),
        migrations.AlterField(
            model_name="inscripcion",
            name="id_curso",
            field=models.ForeignKey(
                db_column="id_curso",
                on_delete=django.db.models.deletion.CASCADE,
                to="cursos.curso",
                verbose_name="Curso",
            ),
        ),
        migrations.AlterField(
            model_name="inscripcion",
            name="id_inscripcion",
            field=models.AutoField(
                db_column="id_inscripcion",
                primary_key=True,
                serialize=False,
                verbose_name="ID de Inscripción",
            ),
        ),
    ]
