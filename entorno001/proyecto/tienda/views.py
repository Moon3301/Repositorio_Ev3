from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def validar (request):
    return render (request, 'login.html')

def inicio (request):
    return render (request, 'index.html')

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

def listadoUsuario (request):
    listadoU = Usuario.objects.all()

    contexto = {'listadoU' : listadoU, 'user' : ''}

    return render(request, 'ListadoUsuario.html', contexto)

def modificarUsuario(request, rut):

    M_usuario = Usuario.objects.get(rut = rut)

    contexto = {'form_usuario': UsuarioForm(instance=M_usuario) }

    if request.method == 'POST' :
        M_usuario = UsuarioForm(data=request.POST, instance=M_usuario)
        M_usuario.save()
        contexto = {'form_usuario' : UsuarioForm(instance=Usuario.objects.get(rut = rut)) }
        contexto['mensaje'] = 'Los datos fueron guardados'
        
    return render(request, 'ModificarUsuario.html', contexto)


def eliminarUsuario(request, rut ):
    usuario = Usuario.objects.get(rut = rut)
    usuario.delete()
    return redirect(to = "listadoUsuario")


def ingresarProveedor (request):
    contexto = {'form_proveedor': ProveedorForm}

    if request.method == 'POST':
        proveedor = ProveedorForm(request.POST)
        proveedor.save()# insert
        contexto['mensaje'] = 'Datos guardados'
    return render(request, 'ingresarProveedor.html', contexto)

def modificarProveedor(request, rut):

    proveedor = Proveedor.objects.get(rut = rut)

    contexto = {'form_proveedor': ProveedorForm(instance=proveedor) }

    if request.method == 'POST' :
        proveedor = ProveedorForm(data=request.POST, instance=proveedor)
        proveedor.save()
        contexto = {'form_proveedor' : ProveedorForm(instance=Proveedor.objects.get(rut = rut)) }
        contexto['mensaje'] = 'Los datos fueron guardados'

    return render(request, 'modificarProveedor.html', contexto)

def listadoProveedor (request):
    listadoP = Proveedor.objects.all()

    contexto = {'listadoP' : listadoP, 'user' : ''}

    return render(request, 'listadoProveedor.html', contexto)


def eliminarProveedor(request, rut ):
    proveedor = Proveedor.objects.get(rut = rut)
    proveedor.delete()
    return redirect(to = "listadoProveedor")