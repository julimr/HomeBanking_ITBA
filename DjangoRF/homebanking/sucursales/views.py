from django.shortcuts import render
from sucursales.models import Direccion
from sucursales.serializers import DireccionSerializer
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



