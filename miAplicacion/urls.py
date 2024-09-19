#creado por mi

from . import views
from django.urls import path

urlpatterns = [
    #urls a vistas en funciones simples
    path('', views.saludo, name="saludo"),
    path('base/1',  views.indexHardcodeado, name="hardcode"),
    path('base/2/<str:nombre>',  views.indexNombreUrl, name="nombreUrl"),
    path('base/3/', views.indexParametro, name="parametro"),
    #A partir de aca, vistas para consultar al modelo. Se usan clases

]