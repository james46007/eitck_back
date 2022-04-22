from django.utils.translation import gettext_lazy as _

from django.db import models
from django.utils import timezone
from usuario.models import Usuario

def upload_path(instance, filname):
    return '/'.join(['Bakery/imgCajas', str(timezone.localtime(timezone.now())) + "_" + filname])

# Create your models here.
class Pedido(models.Model):

    class TipoPago(models.TextChoices):
        EFECTIVO = 'Efectivo', _('Efectivo')
        TARGETA = 'Targeta', _('Targeta')


    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)  # Relacion usuario
    tipoPago = models.CharField(
        max_length=8,
        choices=TipoPago.choices,
        default=TipoPago.EFECTIVO,
    )
    total = models.FloatField(null=False)
    nombre = models.CharField(max_length=150,blank=False,null=False)
    direccion = models.CharField(max_length=150,blank=False,null=False)
    telefono = models.CharField(max_length=150,blank=False,null=False)

    cajas = models.JSONField(default=[])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)


class Caja(models.Model):
    nombre = models.CharField(max_length=150,null=True)
    precio = models.FloatField(null=False)
    cantidad = models.SmallIntegerField(null=False)
    descripcion = models.TextField(null=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
    

class Imagen(models.Model):
    imagen=models.ImageField(blank=False,null=False,upload_to=upload_path)
    caja = models.ForeignKey(Caja, related_name='imagenes', blank=False, null=True, on_delete=models.CASCADE)  # Relacion caja

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)


