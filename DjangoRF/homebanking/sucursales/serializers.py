from dataclasses import field
from rest_framework import serializers
from .models import Sucursal, Direccion, Prestamo, Cliente

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        #Acá se podría incluir el branch_number tambien
        fields = ('branch_id', 'branch_name')


class DireccionSerializer(serializers.ModelSerializer):
    #Serializador anidado
    branch = SucursalSerializer()
    class Meta:
        model = Direccion
        fields = ('pais', 'provincia', 'ciudad', 'calle', 'numero', 'branch')

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('loan_id', 'loan_total')
    

class ClienteSerializer(serializers.ModelSerializer):
    prestamos = serializers.SerializerMethodField()
    class Meta:
        model = Cliente
        fields = ('customer_id', 'branch_id', 'prestamos')
    def get_prestamos(self, obj):
            customer_account_query = Prestamo.objects.filter(customer_id= obj.customer_id)
            serializer = PrestamoSerializer(customer_account_query, many=True)
    
            return serializer.data