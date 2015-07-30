from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=250)


class Juguete(models.Model):
    valorUnitario = models.DecimalField(default=0)
    valorAdicional = models.DecimalField(default=0)
    codigo = models.IntegerField()
    edadRecomenda = models.IntegerField()
    numeroProveedor = models.IntegerField()
    cantidad = models.IntegerField()
