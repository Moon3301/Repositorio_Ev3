from django import contrib
from django import urls
from django.contrib import auth
from django.urls import path 
from django.contrib import admin
from django.contrib.auth import login,logout
from django.urls.conf import include
from .views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required



urlpatterns = [

    path('',validar, name= "validar"),
    path('inicio', inicio, name="inicio"),
    path('listadoProducto', listadoProducto, name="listadoProducto"),
    path('crearProducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<codigo_barra>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<codigo_barra>', eliminarProducto, name="eliminarProducto"),
    path('usuario', usuario, name="usuario"),
    path('productos', productos,name="productos"),
    path('listadoUsuario', listadoUsuario, name="listadoUsuario"),
    path('modificarUsuario/<rut>', modificarUsuario, name="modificarUsuario"),
    path('eliminarUsuario/<rut>', eliminarUsuario, name="eliminarUsuario"),
    
]