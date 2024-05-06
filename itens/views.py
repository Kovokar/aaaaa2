from django.shortcuts import render
from .models import Itens
from .serializers import ItensSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class ItensListAndCreate(APIView):
    def get(self, request):
        itens = Itens.objects.all()
        serializer = ItensSerializers(itens, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItensSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ItensDetailAtualizeAndDelete(APIView):
    def get_object(self, pk):
        try:
            return Itens.objects.get(pk=pk)
        except Itens.DoesNotExist:
            raise FileNotFoundError
        
    def get(self, request, pk):
        Itens = self.get_object(pk)
        serializer = ItensSerializers(Itens)
        return Response(serializer.data)
    
    def put(self, request, pk):
        Itens = self.get_object(pk)
        serializer = ItensSerializers(Itens, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Itens = self.get_object(pk)
        Itens.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



