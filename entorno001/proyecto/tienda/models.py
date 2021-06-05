from django.db import models
from django.db.models.base import Model

# Create your models here.

class Usuario(models.Model):
    rut = models.IntegerField(primary_key= True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_nac = models.CharField(max_length=50)
    telefono = models.IntegerField()
    pais = models.CharField(max_length=50)
    nivel_educacional = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    
    codigo_barra = models.IntegerField(primary_key= True)
    descripcion = models.CharField(max_length=50)
    precio_costo = models.IntegerField()
    precio_venta = models.IntegerField()
    marca = models.CharField(max_length=50)
    activo = models.BooleanField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


    

    def __str__(self):
        return self.descripcion
# Create your models here.
