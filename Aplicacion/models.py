from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .enumeraciones import *

class Tecnico(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre
    
class Sucursal(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre

class Mantencion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    motivo = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    valor = models.IntegerField(null=False)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT, null=False)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, null=False)
    imagen = models.ImageField(upload_to="Aplicacion/media/productos", null=True)
    estado =models.CharField(max_length=50, choices= sorted(ESTADO, key=lambda x: x[1]),default="Mantencion solicitada")

    def __str__(self):
        return f"Nombre:{self.usuario} Motivo: {self.motivo} Tecnico: {self.tecnico} Valor: {self.valor}"
