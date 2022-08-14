from django.db import models

# Create your models here.
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("clientes.Cliente",  on_delete=models.CASCADE)
    balance = models.TextField()  
    iban = models.TextField() 
    tipo_cuenta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'

class UserCliente(models.Model):
    id_user = models.IntegerField()
    id_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_cliente'