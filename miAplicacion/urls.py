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
    path('aplicacion/', views.mostrarHome,name="mostrarHome"),
    path('aplicacion/crearMensaje', views.CrearMensaje.as_view(),name="CrearMensaje"),
    path('aplicacion/verEnviados', views.accionVerMensajesEnviados,name="accionVerMensajesEnviados"),
    path('aplicacion/verRecibidos', views.accionVerMensajesRecibidos,name="accionVerMensajesRecibidos"),
    path('aplicacion/eliminarMensaje', views.mostrarEliminarMensaje,name="mostrarEliminarMensaje"),
]