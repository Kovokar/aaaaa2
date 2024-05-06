from django.contrib import admin
from django.urls import path, include
from .views import UsuariosListAndCreate,UsuariosDetailAtualizeAndDelete

urlpatterns = [
    path('users/', UsuariosListAndCreate.as_view()),
    path('users/<int:pk>/', UsuariosDetailAtualizeAndDelete.as_view()),
]
