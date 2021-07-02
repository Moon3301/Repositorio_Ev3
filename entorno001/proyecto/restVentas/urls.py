from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('listarProducto',listarProducto, name= "listarProducto"),
    path('gestionarProducto/<codigo_barra>', gestionarProducto, name="gestionarProducto"),

    path('listarCategoria',listarUsuario, name="listarCategoria"),
    path('gestionarUsuario/<rut>,',gestionarUsuario, name="gestionarUsuario"),

  
   
    
   

    

]