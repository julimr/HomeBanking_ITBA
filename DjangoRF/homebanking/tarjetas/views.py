from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tarjetas.models import Tarjeta, UserCliente, Cliente
from django.contrib import messages
from tarjetas.serializers import ClienteSerializer
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
  tarjetas = Tarjeta.objects.all().values()
  userID = request.user.id
  if userID is not None:
    idCliente = obtenerClienteID(userID)
    tarjetasDelCliente = tarjetas.filter(customer_id = idCliente)
    context = { 'tarjetas' : tarjetasDelCliente, 'userID' : userID }
    if len(tarjetasDelCliente) == 0:
      messages.info(request, 'No tiene tarjetas a su nombre.')
  else: 
        context = { 'tarjetas' : tarjetas, 'userID' : userID }

  template = loader.get_template('tarjetas/index.html')
  return HttpResponse(template.render(context, request))


class TarjetasClienteDetail(APIView):
  renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
  def get(self, request, pk=None):
    if pk:
      cliente = Cliente.objects.filter(customer_id = pk)
      serializer = ClienteSerializer(cliente, context={'request':request}, many=True)
      if cliente:
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)

def obtenerClienteID(userID):
  userCliente = UserCliente.objects.filter(id_user = userID)
  for x in userCliente:
      idCliente = x.id_cliente
  return idCliente