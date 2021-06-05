from django.urls import path 
from .views import inicio,listadoProducto, crearProducto, modificarProducto, eliminarProducto

urlpatterns = [
    path('',inicio, name= "inicio"),
    path('inicio', inicio, name="inicio"),
    path('listadoProducto', listadoProducto, name="listadoProducto"),
    path('crearProducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    

    


]