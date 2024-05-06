from .models import Usuarios
from rest_framework import serializers


class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = [
            'id',
            'nome',
            'email'
        ]

