from django.db import models

# Create your models here.


class Base(models.Model): 
    criacao = models.DateTimeField(auto_now_add= True) 
    atualizacao = models.DateTimeField(auto_now= True) 
    ativo = models.BooleanField(default=True) 

    class Meta: 
        abstract = True


class Usuarios(Base):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)


