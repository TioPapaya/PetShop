from django.shortcuts import render
from .models import mascota, tienda, fundacion
from .forms import adopcionForms
from django.shortcuts import redirect
# Create your views here.

def inicio(request):
    context={}
    return render(request,'PetShop/inicio.html')

def productos(request):
    tiendas = tienda.objects.all()
    data={
        'tiendas': tiendas
    }
    return render(request,'PetShop/tienda.html', data)

def nosotros(request):

    return render(request,'PetShop/nosotros.html')

def contacto(request):
    fundaciones = fundacion.objects.all()
    data={
        'fundaciones':fundaciones 
    }
    return render(request,'PetShop/contacto.html',data)

def adopcion(request):
    mascotas = mascota.objects.all()
    data={
        'mascotas': mascotas
    }
    return render(request,'PetShop/adopcion.html', data)

def poner_adopcion(request):
    data={
        'form': adopcionForms()
    }

    if request.method =='POST':
        formulario = adopcionForms( data= request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
        else:
            data['form']= formulario

    return render(request, 'PetShop/poner_adopcion.html', data)

def mascotaDel(request, pk):
    mascotas = mascota.objects.get(nombre=pk)
    mascotas.delete()
    return redirect(to='adopcion')
