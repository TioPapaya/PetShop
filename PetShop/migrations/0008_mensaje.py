# Generated by Django 4.1.2 on 2023-06-29 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetShop', '0007_delete_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='mensaje',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_persona', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('nro_telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('nombre_mascota', models.CharField(max_length=30)),
                ('motivo', models.CharField(max_length=100)),
            ],
        ),
    ]
