from django.urls import path 
from . import views


urlpatterns =[
    path('inicioadmin', views.inicioadmin, name='inicioadmin'),
    path('refugio', views.refugio, name='refugio'),
    path('refugiodel/<pk>', views.refugiodel, name='refugiodel'),
    path('refugioedit/<pk>', views.refugioedit, name='refugioedit'),
    path('productoedit/<pk>', views.productoedit, name='productoedit'),
    path('productodel/<pk>', views.productodel, name='productodel'),
    path('tiendaforms', views.tiendaforms, name='tiendaforms'),
]