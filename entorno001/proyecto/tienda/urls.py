from django.urls import path 
from .views import inicio

urlpatterns = [
    path('',inicio, name= "inicio"),
    path('inicio', inicio, name="inicio"),
    

]