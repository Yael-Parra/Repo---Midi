# Generated by Django 5.1.7 on 2025-03-10 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPadresTutoresLegales',
            fields=[
                ('id_tutor', models.AutoField(db_column='id_tutor', primary_key=True, serialize=False)),
                ('mama_nombre', models.CharField(db_column='mama_nombre', max_length=50, verbose_name='Nombre de la Madre')),
                ('mama_apellido', models.CharField(db_column='mama_apellido', max_length=50, verbose_name='Apellido de la Madre')),
                ('mama_cedula', models.CharField(db_column='mama_cedula', max_length=20, verbose_name='Cédula de la Madre')),
                ('mama_telefono', models.CharField(db_column='mama_telefono', max_length=20, verbose_name='Teléfono de la Madre')),
                ('mama_email', models.EmailField(db_column='mama_email', max_length=50, verbose_name='Email de la Madre')),
                ('mama_empresa', models.CharField(db_column='mama_empresa', max_length=100, verbose_name='Empresa de la Madre')),
                ('papa_nombre', models.CharField(db_column='papa_nombre', max_length=50, verbose_name='Nombre del Padre')),
                ('papa_apellido', models.CharField(db_column='papa_apellido', max_length=50, verbose_name='Apellido del Padre')),
                ('papa_cedula', models.CharField(db_column='papa_cedula', max_length=20, verbose_name='Cédula del Padre')),
                ('papa_telefono', models.CharField(db_column='papa_telefono', max_length=20, verbose_name='Teléfono del Padre')),
                ('papa_email', models.EmailField(db_column='papa_email', max_length=50, verbose_name='Email del Padre')),
                ('papa_empresa', models.CharField(db_column='papa_empresa', max_length=100, verbose_name='Empresa del Padre')),
                ('direccion', models.CharField(db_column='direccion', max_length=100, null=True, verbose_name='Dirección')),
                ('id_alumno', models.ForeignKey(db_column='id_alumno', on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno', verbose_name='Alumno')),
            ],
            options={
                'db_table': 'info_padres_tutores_legales',
            },
        ),
    ]
