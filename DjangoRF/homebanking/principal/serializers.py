from rest_framework import serializers,permissions
from .models import Cliente, Direccion, Prestamo, Cuenta

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('tipo_cuenta', 'balance')

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('loan_type', 'loan_total')

class DatosSerializer(serializers.ModelSerializer):
    cuenta = serializers.SerializerMethodField()
    prestamos = serializers.SerializerMethodField()
    class Meta:
        model = Cliente
        fields = ('customer_id', 'customer_name', 'customer_surname', 'cuenta', 'prestamos')

    def get_cuenta(self, obj):
            customer_account_query = Cuenta.objects.filter(customer_id=obj.customer_id)
            serializer = CuentaSerializer(customer_account_query, many=True)
    
            return serializer.data

    def get_prestamos(self, obj):
            customer_account_query = Prestamo.objects.filter(customer_id=obj.customer_id)
            serializer = PrestamoSerializer(customer_account_query, many=True)
    
            return serializer.data

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('direccion_id', 'calle','numero','ciudad','provincia','pais')
