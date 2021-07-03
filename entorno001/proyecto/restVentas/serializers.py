from rest_framework import serializers
from tienda.models import *

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProveedorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
