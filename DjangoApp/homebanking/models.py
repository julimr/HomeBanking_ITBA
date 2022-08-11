# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.AutoField(primary_key=True, blank=True, null=True)
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.IntegerField()
    new_type = models.IntegerField()
    user_action = models.TextField()
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.ForeignKey('TipoCuentas', models.DO_NOTHING, db_column='tipo_cuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True, blank=True, null=True)
    calle = models.TextField()
    numero = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('Empleado', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcasTarjeta(models.Model):
    marca_id = models.AutoField(primary_key=True, blank=True, null=True)
    marca = models.TextField()

    class Meta:
        managed = False
        db_table = 'marcas_tarjeta'


class Movimientos(models.Model):
    mov_id = models.AutoField(primary_key=True, blank=True, null=True)
    numero_cuenta = models.IntegerField()
    monto = models.IntegerField()
    tipo_operacion = models.TextField()
    hora = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    numero = models.TextField(primary_key=True, blank=True, null=True)
    cvv = models.TextField(db_column='CVV')  # Field name made lowercase.
    fecha_otorgamiento = models.TextField()
    fecha_expiracion = models.TextField()
    tipo_tarjeta = models.ForeignKey('TipoTarjetas', models.DO_NOTHING)
    marca = models.ForeignKey(MarcasTarjeta, models.DO_NOTHING)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoCuentas(models.Model):
    cuenta_id = models.AutoField(primary_key=True, blank=True, null=True)
    tipo_cuenta = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuentas'


class TipoTarjetas(models.Model):
    tipo_tarjeta_id = models.AutoField(primary_key=True, blank=True, null=True)
    tipo_tarjeta = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_tarjetas'


class TiposCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True, blank=True, null=True)
    tipo_cliente = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipos_cliente'
