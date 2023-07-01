from dataclasses import fields
from django import forms
from PetShop.models import fundacion,tienda


class fundacionFrom(forms.ModelForm):
    class Meta:
        model  = fundacion
        fields =  "nombre_fundacion","direcion","nro_telefono","corre"

class tiendaForm(forms.ModelForm):
    class Meta:
        model  = tienda 
        fields = "nombre","precio","imagen"
