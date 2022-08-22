from django.shortcuts import render
from sucursales.models import Sucursal, Direccion
from sucursales.serializers import SucursalSerializer, DireccionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SucursalesList(APIView):
    def get(self, request):
        direccion = Direccion.objects.filter(branch__lte = 100)
        dir_serializer = DireccionSerializer(direccion, many=True)
        print(dir_serializer.data)
        return render(request, 'sucursales/index.html', {'direcciones' : dir_serializer.data})


