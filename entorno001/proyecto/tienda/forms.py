from django import forms
from django.db import models
from .models import *


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = '__all__'