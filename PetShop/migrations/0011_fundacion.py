# Generated by Django 4.1.2 on 2023-06-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetShop', '0010_solicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='fundacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fundacion', models.CharField(max_length=30)),
                ('direcion', models.CharField(max_length=50)),
                ('nro_telefono', models.IntegerField()),
                ('corre', models.EmailField(max_length=254)),
            ],
        ),
    ]
