# Generated by Django 5.1.7 on 2025-03-06 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info_padres_tutores_legales", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="infopadrestutoreslegales",
            name="direccion",
            field=models.CharField(max_length=100, null=True, verbose_name="Dirección"),
        ),
    ]
