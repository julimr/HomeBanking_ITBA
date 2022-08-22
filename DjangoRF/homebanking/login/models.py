from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    email = models.EmailField(max_length = 50)

class Login(models.Model):
    username = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length = 50)

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

class UserCliente(models.Model):
    id_user = models.IntegerField()
    id_cliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_cliente'