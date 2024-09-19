#creado por mi

from . import views
from django.urls import path

urlpatterns = [
    #urls a vistas en funciones simples
    path('', views.saludo, name="saludo"),
    path('prueba/1',  views.indexHardcodeado, name="hardcode"),
    path('prueba/2/<str:nombre>',  views.indexNombreUrl, name="nombreUrl"), #comodin
    path('prueba/3/', views.indexParametro, name="parametro"), #parametros
    #urls a clases en funciones simples
    path('prueba/index', views.Index.as_view(), name="crearMensajes"),
    path('prueba/saludar/<str:nombre>', views.SaludarComodin.as_view(), name="comodin"), #comodin
    path('prueba/saludar/', views.Saludar.as_view(), name="saludarParametros"), #parametros
    #A partir de aca, vistas para consultar al modelo. Se usan clases
    path('aplicacion/base', views.mostrarBase,name="mostrarBase"), #solo para probar, borrar este path despues
    path('aplicacion', views.mostrarBase,name="mostrarBase"),
    path('aplicacion/crearMensaje', views.crearMensaje,name="crearMensaje"),
]