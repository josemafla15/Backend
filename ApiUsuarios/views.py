import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from ApiUsuarios.models import Usuario
from .serializer import usuario_serializer
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
#Clase publicacion view
class UsuariosView(APIView):
    def get(self, request, *args, **kwargs):
            lista_usuarios=Usuario.objects.all()
            serializer_usuarios=usuario_serializer(lista_usuarios, many=True)
            return Response(serializer_usuarios.data,status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'contraseña': request.data.get('contraseña'),
            'fechaNacimiento': request.data.get('fechaNacimiento'),
            'email': request.data.get('email'),
            'paisOrigen': request.data.get('paisOrigen')       
        }

        serializador = usuario_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(
                {"message": "Usuario creado correctamente", "data": serializador.data},
                status=status.HTTP_201_CREATED
            )
    
        return Response(
            {"message": "El usuario no se pudo crear", "errors": serializador.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pkid):
    # Intenta actualizar el usuario y guarda la cantidad de registros afectados
        registros_actualizados = Usuario.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            contraseña=request.data.get('contraseña'),
            fechaNacimiento=request.data.get('fechaNacimiento'),
            email=request.data.get('email'),
            paisOrigen=request.data.get('paisOrigen')
        )

    # Si se actualizó al menos un registro, devuelve un mensaje de éxito
        if registros_actualizados > 0:
            return Response(
                {"message": "Usuario actualizado correctamente"},
                status=status.HTTP_200_OK
        )
        else:
            return Response(
                {"message": "El usuario no se pudo actualizar"},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request, pkid, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(id=pkid)
            usuario.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
          
class UsuarioQueryApiView(APIView):
    def get(self, request, pkid, *args, **kargs):
        miUsuario=Usuario.objects.filter(id=pkid).first()
        serializer_usuario = usuario_serializer(miUsuario)
        return Response(serializer_usuario.data, status=status.HTTP_200_OK)

