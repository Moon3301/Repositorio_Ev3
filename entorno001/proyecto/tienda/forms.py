from django import forms
from django.db import models
from .models import Producto, Usuario


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'