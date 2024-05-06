from django.contrib import admin
from django.urls import path, include
from .views import ItensListAndCreate,ItensDetailAtualizeAndDelete

urlpatterns = [
    path('itens/', ItensListAndCreate.as_view()),
    path('itens/<int:pk>/', ItensDetailAtualizeAndDelete.as_view()),
]
