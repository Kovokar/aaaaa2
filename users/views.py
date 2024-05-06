from django.shortcuts import render
from .models import Usuarios
from .serializers import UsuariosSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class UsuariosListAndCreate(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializers(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuariosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UsuariosDetailAtualizeAndDelete(APIView):
    def get_object(self, pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            raise FileNotFoundError
        
    def get(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuariosSerializers(usuario)
        return Response(serializer.data)
    
    def put(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuariosSerializers(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



