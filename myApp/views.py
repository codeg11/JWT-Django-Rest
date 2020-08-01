from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer,ProductSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, )) #aca se ponen los permisos pero ya por medio de la arroba
def hello_world(request):
    print(" el nombre ",request.user)
    serializer_class = UserSerializer(request.user)
    user = serializer_class.data
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!","user":user})

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, ) #allow any es para permitir que cualquier persona tenga acceso a esta visto ya sea por post o get
  
"""
para ponerlo en el frontend en los headers de las peticiones es de la siguiente manera
key 
Authorization
value
JWT 'aca va la token'
"""

class Product(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, ) #para saber si esta autenticado

