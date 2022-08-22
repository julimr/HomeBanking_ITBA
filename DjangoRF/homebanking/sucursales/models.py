from django.db import models

# Create your models here.
class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'
    
class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True, blank=True, null=False)
    calle = models.TextField()
    numero = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'