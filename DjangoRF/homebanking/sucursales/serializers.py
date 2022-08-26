from dataclasses import field
from rest_framework import serializers,  permissions
from .models import Sucursal, Direccion, Prestamo, Cliente

class SucursalSerializer(serializers.ModelSerializer):
    direccion = serializers.SerializerMethodField()
    class Meta:
        model = Sucursal
        fields = ('branch_id', 'branch_name','branch_number', 'branch_address_id','direccion')
    def get_direccion(self, obj):
            customer_account_query = Direccion.objects.filter(direccion_id= obj.branch_address_id)
            serializer = DireccionSerializer(customer_account_query, many=True)
    
            return serializer.data


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('pais', 'provincia', 'ciudad', 'calle', 'numero')

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
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
            customer_account_query = Prestamo.objects.filter(customer_id= obj.customer_id)
            serializer = PrestamoSerializer(customer_account_query, many=True)
    
            return serializer.data