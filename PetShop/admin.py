from django.contrib import admin
from .models import Genero, mascota, tienda, fundacion

# Register your models here.
admin.site.register(Genero)
admin.site.register(mascota)
admin.site.register(tienda)
admin.site.register(fundacion)

