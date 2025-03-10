# Generated by Django 5.1.7 on 2025-03-10 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0001_initial'),
        ('colegios', '0001_initial'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id_inscripcion', models.AutoField(db_column='id_inscripcion', primary_key=True, serialize=False, verbose_name='ID de Inscripción')),
                ('fecha_inscripcion', models.DateTimeField(auto_now_add=True, db_column='fecha_inscripcion', verbose_name='Fecha de Inscripción')),
                ('fecha_baja', models.DateTimeField(blank=True, db_column='fecha_baja', null=True, verbose_name='Fecha de Baja')),
                ('id_alumno', models.ForeignKey(db_column='id_alumno', on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno', verbose_name='Alumno')),
                ('id_colegio', models.ForeignKey(blank=True, db_column='id_colegio', null=True, on_delete=django.db.models.deletion.CASCADE, to='colegios.colegio', verbose_name='Colegio')),
                ('id_curso', models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, to='cursos.curso', verbose_name='Curso')),
            ],
            options={
                'db_table': 'inscripciones',
            },
        ),
    ]
