from django.urls import path 
from .views import inicio,listadoProducto, crearProducto, modificarProducto, eliminarProducto, productos, usuario

urlpatterns = [
    path('',inicio, name= "inicio"),
    path('inicio', inicio, name="inicio"),
    path('listadoProducto', listadoProducto, name="listadoProducto"),
    path('crearProducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<codigo_barra>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<codigo_barra>', eliminarProducto, name="eliminarProducto"),
    path('usuario', usuario, name="usuario"),
    path('productos', productos,name="productos"),
    




]