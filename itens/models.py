from django.db import models
from users.models import Base


class Itens(Base):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    




# Create your models here.
