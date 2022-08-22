from dataclasses import field
from rest_framework import serializers
from .models import Sucursal, Direccion


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('branch_id', 'branch_name')

class DireccionSerializer(serializers.ModelSerializer):
    #Serializador anidado
    branch = SucursalSerializer()
    class Meta:
        model = Direccion
        fields = ('pais', 'provincia', 'ciudad', 'calle', 'numero', 'branch')
