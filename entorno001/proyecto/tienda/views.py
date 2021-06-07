from django.shortcuts import render, redirect
from .models import Producto, Usuario
from .forms import ProductoForm, UsuarioForm

# Create your views here.



def inicio (request):
    return render (request, 'Index.html')

def productos (request):
    return render (request, 'Productos.html')

def usuario (request):
    return render (request, 'Formulario.html')

def listadoProducto (request):
    listado = Producto.objects.all()

    contexto = {'listado' : listado, 'user' : ''}

    return render(request, 'ListadoProducto.html', contexto)

def crearProducto (request):
    contexto = {'formulario': ProductoForm}

    if request.method == 'POST':
        producto = ProductoForm(request.POST)
        producto.save()# insert
        contexto['mensaje'] = 'Datos guardados'
    return render(request, 'CrearProducto.html', contexto)

def usuario (request):
    contexto = {'form_usuario': UsuarioForm}

    if request.method == 'POST':
        usuario = UsuarioForm(request.POST)
        usuario.save()# insert
        contexto['mensaje'] = 'Datos guardados'
    return render(request, 'Formulario.html', contexto)

def modificarProducto(request, codigo_barra):

    producto = Producto.objects.get(codigo_barra = codigo_barra)

    contexto = {'formulario': ProductoForm(instance=producto) }

    if request.method == 'POST' :
        formulario = ProductoForm(data=request.POST, instance=producto)
        formulario.save()
        contexto = {'formulario' : ProductoForm(instance=Producto.objects.get(codigo_barra= codigo_barra)) }
        contexto['mensaje'] = 'Los datos fueron guardados'
        
    return render(request, 'ModificarProducto.html', contexto)


def eliminarProducto(request, codigo_barra ):
    producto = Producto.objects.get(codigo_barra = codigo_barra)
    producto.delete()
    return redirect(to = "listadoProducto")