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

#MOSTRAR EL HOME
def mostrarHome(request):
    return render(request, 'home.html')

#CREAR MENSAJE
class CrearMensaje(View):
    def get(self, request):
        return render(request, 'crearMensaje.html')
    def post(self, request):
        texto = request.POST.get('texto')
        emisor = request.POST.get('emisor')
        receptor = request.POST.get('receptor')
        nuevoMensaje = Mensaje(texto=texto, emisor=emisor ,receptor=receptor)
        nuevoMensaje.save()
        return redirect('mostrarHome')

#RECIBIDOS
def accionVerMensajesRecibidos(request):
    receptor = request.GET.get('receptor')
    if receptor:
        contexto = {
            'titulo': 'Mensajes recibidos por '+receptor+': ',
            'mensajes':Mensaje.objects.filter(receptor=receptor),
        }
    else:
        contexto = {
            'titulo': 'No hay mensajes buscados aun. Empieze una busqueda.',
            'mensajes': None,
        }
    return render(request, 'verRecibidos.html', contexto)

#ENVIADOS
def accionVerMensajesEnviados(request):
    emisor = request.GET.get('emisor')
    if emisor:
        contexto = {
            'titulo': 'Mensajes enviados por '+emisor+': ',
            'mensajes':Mensaje.objects.filter(emisor=emisor),
        }
    else:
        contexto = {
            'titulo': 'No hay mensajes buscados aun. Empieze una busqueda.',
            'mensajes': None,
        }
    return render(request, 'verEnviados.html', contexto)

#ELIMINAR MENSAJE
def mostrarEliminarMensaje(request):
    return render(request, 'eliminarMensaje.html')

