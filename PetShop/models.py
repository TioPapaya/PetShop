from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True) 
    genero    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class mascota(models.Model):
    nombre            = models.CharField(max_length = 30)
    edad              = models.IntegerField()
    id_genero         = models.ForeignKey('genero',on_delete=models.CASCADE,db_column='idGenero')
    imagen            = models.ImageField(upload_to='PetShop', null=True)
    peso              = models.IntegerField()
    raza              = models.CharField(max_length = 30)
    esterilizado      = models.BooleanField()
    vacunas           = models.BooleanField()
    color             = models.CharField(max_length = 30)
    
    def __str__(self):
        return str(self.nombre)

class tienda(models.Model):
    nombre      = models.CharField(max_length = 30)
    precio      = models.IntegerField()
    imagen      = models.ImageField(upload_to='PetShop', null=True)
    
    def __str__(self):
        return str(self.nombre)

class fundacion(models.Model):
    nombre_fundacion   = models.CharField(max_length=30)
    direcion           = models.CharField(max_length=50)
    nro_telefono       = models.IntegerField()
    corre              = models.EmailField()
    
    def __str__(self):
        return str(self.nombre_fundacion)
    
