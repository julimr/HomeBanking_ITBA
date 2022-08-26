from django.db import models

# Create your models here.
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

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey('TipoCuentas', models.DO_NOTHING, db_column='tipo_cuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'

class TipoCuentas(models.Model):
    cuenta_id = models.AutoField(primary_key=True, blank=True, null=False)
    tipo_cuenta = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuentas'

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True, blank=True)
    calle = models.TextField()
    numero = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    customer_id = models.IntegerField()
    employee_id = models.IntegerField()
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'direccion'
