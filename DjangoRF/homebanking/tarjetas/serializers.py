from dataclasses import field
from rest_framework import serializers
from .models import Tarjeta, Cliente
from rest_framework import status, permissions


class ClienteSerializer(serializers.ModelSerializer):
    tarjetas = serializers.SerializerMethodField()
    class Meta:
        model = Cliente
        #Acá se podría incluir el branch_number tambien
        fields = ('customer_id', 'customer_name', 'tarjetas')
    def get_tarjetas(self, obj):
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
            customer_account_query = Tarjeta.objects.filter(customer_id= obj.customer_id)
            serializer = TarjetaSerializer(customer_account_query, many=True)
    
            return serializer.data

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ('tarjeta_id','numero', 'cvv','fecha_otorgamiento')