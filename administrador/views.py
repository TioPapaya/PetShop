from django.shortcuts import render
from PetShop.models import fundacion, tienda
from django.shortcuts import redirect
from .forms import fundacionFrom, tiendaForm
from django.contrib.auth.decorators import login_required


@login_required
def inicioadmin(request):
    request.session["usuario"]="joalmontes"
    usuario=request.session["usuario"]

    tiendas = tienda.objects.all()
    fundaciones = fundacion.objects.all()
    data = {
        'tiendas': tiendas,
        'fundaciones': fundaciones,
        'usuario':usuario
    }
    return render(request, 'administrador/inicioadmin.html', data)

def refugioedit(request, pk):
    editarRefugio = fundacion.objects.get(nombre_fundacion=pk)
    data={
        'form': fundacionFrom(instance=editarRefugio)
    }
    if request.method =='POST':
        formulario = fundacionFrom( data= request.POST, files=request.FILES, instance=editarRefugio)
        if formulario.is_valid:
            formulario.save()
            return redirect(to='inicioadmin')
        else:
            data['form']= formulario
    return render(request,'administrador/fundacionform.html',data)


def refugiodel(request, pk):
    borrarfundacio = fundacion.objects.get(nombre_fundacion=pk)
    borrarfundacio.delete()
    return redirect(to='inicioadmin')


def refugio(request):
    data={
        'form': fundacionFrom()
    }
    if request.method =='POST':
        formulario = fundacionFrom( data= request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
        else:
            data['form']= formulario
    return render(request,'administrador/fundacionform.html',data)

def productoedit(request, pk):
    editarproducto = tienda.objects.get(nombre=pk)
    data={
        'form': tiendaForm(instance=editarproducto)
    }
    if request.method =='POST':
        formulario = tiendaForm( data= request.POST, files=request.FILES, instance=editarproducto)
        if formulario.is_valid:
            formulario.save()
            return redirect(to='inicioadmin')
        else:
            data['form']= formulario
    return render(request,'administrador/fundacionform.html',data)

def productodel(request, pk):
    borrartienda = tienda.objects.get(nombre=pk)
    borrartienda.delete()
    return redirect(to='inicioadmin')

def tiendaforms(request):
    data={
        'form': tiendaForm()
    }
    if request.method =='POST':
        formulario = tiendaForm( data= request.POST, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
        else:
            data['form']= formulario
    return render(request,'administrador/tiendaforms.html',data) 
