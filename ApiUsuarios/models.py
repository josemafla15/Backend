from django.db import models

# Create your models here.
#Clase publicacion para feed de publicaciones
class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    contraseña=models.CharField(max_length=30)
    fechaNacimiento=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    paisOrigen=models.CharField(max_length=30)

