from ApiUsuarios.models import Usuario
from rest_framework import serializers

#Serializer publicacion para feed de publicaciones
class usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=[
            'id',
            'nombre',
            'contraseña',
            'fechaNacimiento',
            'email',
            'paisOrigen'
        ]