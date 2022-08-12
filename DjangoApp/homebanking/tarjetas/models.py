from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    numero = models.TextField()
    CVV = models.TextField()
    fecha_otorgamiento = models.TextField()
    fecha_expiracion = models.TextField()
    tipo_tarjeta_id = models.IntegerField()
    marca_id = models.IntegerField()
    customer = models.ForeignKey("clientes.Cliente",  on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'tarjeta'
