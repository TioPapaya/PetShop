from dataclasses import fields
from django import forms
from .models import mascota


class adopcionForms(forms.ModelForm):
    class Meta:
        model  = mascota
        fields = "nombre","edad","id_genero","imagen","peso","raza","esterilizado","vacunas","color"



