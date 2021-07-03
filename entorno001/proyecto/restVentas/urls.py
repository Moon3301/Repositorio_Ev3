from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('listarProducto',listarProducto, name= "listarProducto"),
    path('gestionarProducto/<codigo_barra>', gestionarProducto, name="gestionarProducto"),

    path('listarUsuario',listarUsuario, name="listarUsuario"),
    path('gestionarUsuario/<rut>,',gestionarUsuario, name="gestionarUsuario"),

    path('listarProveedor',listarProveedor, name="listarProveedor"),
    path('gestionarProveedor/<rut>,',gestionarProveedor, name="gestionarProveedor"),


    path('login',login, name="login"),

    
  
   
    
   

    

]