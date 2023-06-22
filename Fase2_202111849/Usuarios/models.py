from django.db import models
from colorama import Fore as fo

# Create your models here.
class Usuario(models.Model):
    rol = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=15)
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)