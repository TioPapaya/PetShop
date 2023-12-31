# Generated by Django 4.1.2 on 2023-06-18 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='PetShop')),
                ('peso', models.IntegerField()),
                ('raza', models.CharField(max_length=30)),
                ('esterilizado', models.BooleanField()),
                ('vacunas', models.BooleanField()),
                ('color', models.CharField(max_length=30)),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='PetShop.genero')),
            ],
        ),
    ]
