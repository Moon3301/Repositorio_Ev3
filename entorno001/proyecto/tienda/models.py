from django.db import models
from django.db.models.base import Model

list_pais = [
    (1,'Argentina'),(2,'Bolivia'),(3,'Brasil'),(4,'Chile'),(5,'Colombia'),
    (6,'Costa Rica'),(7,'Cuba'),(8,'Ecuador'),(9,'El salvador'),(10,'Guatemala'),
    (11,'Honduras'),(12,'Mexico'),(13,'Nicaragua'),(14,'Panama'),(15,'Paraguay'),
    (16,'Peru'),(17,'Puerto Rico'),(18,'Republica Dominicana'),(19,'Uruguay'),(20,'Venezuela'),
    (21,'Seleccione')
]

list_nivel = [
        (1,'Seleccione'),(2,'Doctor'),(3,'Magister'),(4,'Profesional'),(5,'Educacion Media'),
        (6,'Educacion Basica'),(7,'Otra')
]
 

# Create your models here.

class Usuario(models.Model):

   
    rut = models.CharField(primary_key= True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    fecha_nac = models.CharField(max_length=50)
    telefono = models.IntegerField()
    pais = models.IntegerField(
        null=False, blank = False,
        choices=list_pais,
        default = 21
    )
    nivel_educacional = models.IntegerField(
        null=False, blank=False,
        choices=list_nivel,
        default=1

    )

    def __str__(self):
        return self.nombre


             
class Producto(models.Model):
    
    codigo_barra = models.IntegerField(primary_key= True)
    descripcion = models.CharField(max_length=50)
    precio_costo = models.IntegerField()
    precio_venta = models.IntegerField()
    marca = models.CharField(max_length=50)
    activo = models.BooleanField()
    


    

    def __str__(self):
        return self.descripcion
# Create your models here.
