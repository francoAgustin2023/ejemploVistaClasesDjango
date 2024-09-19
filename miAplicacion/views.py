from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def saludo(request): #respuesta HTTP 
    return HttpResponse("Hola mundo!")

def indexHardcodeado(request): #devuelve un saludo con el nombre hardcodeado
    nombre = "joaquin"
    elemento = {
        'nombre': nombre
    }
    return render(request, 'base.html', elemento)

def indexNombreUrl(request, nombre): #devuelve un saludo con el nombre
    return render(request, 'base.html', {'nombre':nombre})

def indexParametro(request): #obtiene valores de parametros en la url
    nombre = request.GET.get('nombre','desconocido')
    return render(request, 'base.html', {'nombre':nombre})

#A partir de aca se empieza a interactuar con el modelo
class CrearMensaje(View):
    def get(self, request):
        