from django.urls import path 
from .views import *

urlpatterns = [
    path('listarProducto',listarProducto, name= "listarProducto"),
    path('gestionarProducto/<codigo_barra>', gestionarProducto, name="gestionarProducto"),

    path('listarCategoria',listarUsuario, name="listarCategoria"),
    path('gestionarUsuario/<rut>,',gestionarUsuario, name="gestionarUsuario"),

    path('login', login , name="login")

    

]