from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):

    class TipoUsuarioEnum(models.TextChoices):
        ADMINISTRADOR = 'Administrador', _('Administrador')
        CLIENTE = 'Cliente', _('Cliente')
        DELIVERY = 'Delivery', _('Delivery')

    nombre = models.CharField(max_length=255,blank=True,null=True)
    direcciones = models.JSONField(blank=True,null=True,default=[])
    telefono = models.CharField(max_length=10,blank=True,null=True)
    email = models.EmailField(max_length=255,blank=True,null=True)
    rol = models.CharField(max_length=15,choices=TipoUsuarioEnum.choices,default=TipoUsuarioEnum.CLIENTE)
    idUser = models.ForeignKey(User, null=False, on_delete=models.CASCADE)  # Relacion con la tabla usuario de la libreria de autenticacion

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)