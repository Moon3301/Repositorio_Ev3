from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def inicio (request):
    return render (request, 'Index.html')

def listadoProducto (request):
    listado = Producto.objects.all()

    contexto = {'listado' : listado, 'user' : 'alguien'}

    return render(request, 'ListadoProducto.html', contexto)

def crearProducto (request):
    contexto = {'formulario': ProductoForm}

    if request.method == 'POST':
        producto = ProductoForm(request.POST)
        producto.save()# insert
        contexto['mensaje'] = 'Datos guardados'
    return render(request, 'RegistroProducto.html', contexto)

def modificarProducto(request, id):

    producto = Producto.objects.get(id = id)

    contexto = {'formulario': ProductoForm(instance=producto) }

    if request.method == 'POST' :
        formulario = ProductoForm(data=request.POST, instance=producto)
        formulario.save()
        contexto = {'formulario' : ProductoForm(instance=Producto.objects.get(id = id)) }
        contexto['mensaje'] = 'Los datos fueron guardados'
        
    return render(request, 'modificarProducto.html', contexto)


def eliminarProducto(request, id ):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect(to = "listadoProducto")