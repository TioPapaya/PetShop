from django.urls import path 
from . import views

urlpatterns =[
    path('inicio', views.inicio, name='inicio'),
    path('tienda', views.productos, name='tienda'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('adopcion', views.adopcion, name='adopcion'),
    path('poner_adopcion', views.poner_adopcion,name='poner_adopcion'),
    path('mascotaDel/<pk>', views.mascotaDel, name='mascotaDel'),
]
