from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True, blank=True)
    numero = models.TextField()
    cvv = models.TextField(db_column='CVV')  # Field name made lowercase.
    fecha_otorgamiento = models.TextField()
    fecha_expiracion = models.FloatField()
    tipo_tarjeta_id = models.IntegerField()
    marca_id = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'

class UserCliente(models.Model):
    id_user = models.IntegerField()
    id_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_cliente'

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'