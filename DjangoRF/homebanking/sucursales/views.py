from django.shortcuts import render
from sucursales.models import Direccion, Sucursal, Cliente
from sucursales.serializers import DireccionSerializer, SucursalSerializer, ClienteSerializer
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SucursalesList(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = "sucursales/index.html"
    def get(self, request):
        direccion = Direccion.objects.filter(branch__lte = 100)
        dir_serializer = DireccionSerializer(direccion, many=True)
        #return render(request, 'sucursales/index.html', {'direcciones' : dir_serializer.data})
        return Response({'direcciones' : dir_serializer.data})

class SucursalDetail(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    def get(self, request, pk=None):
        if pk:
            clientes = Cliente.objects.filter(branch_id = pk)
            serializer = ClienteSerializer(clientes, context={'request':request}, many=True)
            if clientes:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)
