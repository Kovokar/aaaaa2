from .models import Itens
from rest_framework import serializers


class ItensSerializers(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = [
            'id',
            'nome',
            'preco',
        ]