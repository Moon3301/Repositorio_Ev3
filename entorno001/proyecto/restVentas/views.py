from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.authtoken.models import Token

from .serializers import ProductoSerializers, UsuarioSerializers
from tienda.models import Producto, Usuario

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def listarProducto(request):

    if request.method == 'GET':
        listado = Producto.objects.all()
        Serializer = ProductoSerializers(listado, many=True)
        return Response(Serializer.data)

    elif request.method == 'POST':
        Serializer = ProductoSerializers(data= request.data)

        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status= status.HTTP_201_CREATED)
        return Response(Serializer.errors, status= status.HTTP_400_BAD_REQUEST)        

@csrf_exempt
@api_view(['GET', 'DELETE' ,'PUT'])
def gestionarProducto(request, codigo_barra):

    try:
        objeto = Producto.objects.get(codigo_barra = codigo_barra)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = ProductoSerializers(objeto)
        return Response(Serializer.data)
    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        Serializer = ProductoSerializers(objeto, data = request.data)

        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)

        return Response(Serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes(IsAuthenticated,)
def listarUsuario(request):

    if request.method == 'GET':
        listado = Usuario.objects.all()
        Serializer = UsuarioSerializers(listado, many=True)
        return Response(Serializer.data)

    elif request.method == 'POST':
        Serializer = UsuarioSerializers(data= request.data)

        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status= status.HTTP_201_CREATED)
        return Response(Serializer.errors, status= status.HTTP_400_BAD_REQUEST)  

@csrf_exempt
@api_view(['GET', 'DELETE' ,'PUT'])
@permission_classes(IsAuthenticated,)
def gestionarUsuario(request, rut):

    try:
        objeto = Usuario.objects.get(rut = rut)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = UsuarioSerializers(objeto)
        return Response(Serializer.data)
    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        Serializer = UsuarioSerializers(objeto, data = request.data)

        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)

        return Response(Serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST = ["username"]
        password = request.POST =["password"]

        try:
            usuario = User.objects.get(username = username)

        except User.DoesNotExist:
            return Response("Usuario no existe")

        claveValida = check_password(password, usuario.password)

        if not claveValida:
            return Response("La clave no es valida")

        token, created = Token.objects.get_or_create(user = usuario)

        return Response(token.key)