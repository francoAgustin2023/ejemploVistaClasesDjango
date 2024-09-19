from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Mensaje

#Funciones

def saludo(request): #respuesta HTTP 
    return HttpResponse("Hola mundo!")

def indexHardcodeado(request): #devuelve un saludo con el nombre hardcodeado
    nombre = "joaquin"
    elemento = {
        'nombre': nombre
    }
    return render(request, 'prueba.html', elemento)

def indexNombreUrl(request, nombre): #devuelve un saludo con el nombre
    return render(request, 'prueba.html', {'nombre':nombre})

def indexParametro(request): #obtiene valores de parametros en la url
    nombre = request.GET.get('nombre','desconocido')
    return render(request, 'prueba.html', {'nombre':nombre})

#Clases

class Index(View):
    def get(self, request):
        return HttpResponse("aca hay que seguir!")
    
class Saludar(View):
    def get(self, request):
        nombre = request.GET.get('nombre','desconocido')
        return render(request, 'prueba.html', {'nombre':nombre})
    
class SaludarComodin(View):
    def get(self, request, nombre):
        return render(request, 'prueba.html', {'nombre':nombre})
    
#A partir de aca se empieza a interactuar con el modelo (se usan funciones y clases)

def mostrarBase(request): #borrar despues y dejar solo el mostrar home
    return render(request, 'base.html')

def mostrarHome(request):
    return render(request, 'home.html')

def crearMensaje(request):
    if request.method == 'GET':
        return render(request, 'crearMensaje.html')
    else:
        texto = request.POST['texto']
        emisor = request.POST['emisor']
        receptor = request.POST['receptor']
        Mensaje.objects.create(texto=texto, emisor=emisor, receptor=receptor)
        return redirect('base')