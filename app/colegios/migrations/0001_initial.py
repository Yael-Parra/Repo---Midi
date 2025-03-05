# Generated by Django 5.1.6 on 2025-03-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Colegio",
            fields=[
                ("id_colegio", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nombre_colegio",
                    models.CharField(max_length=100, verbose_name="Nombre del Colegio"),
                ),
            ],
            options={
                "db_table": "colegios",
            },
        ),
    ]
