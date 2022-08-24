from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from principal.models import Cliente, UserCliente
from principal.models import Cliente, Cuenta, Prestamo
from principal.serializers import DatosSerializer

# Create your views here.
class DatosCliente(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        userID = request.user.id
        idCliente = obtenerClienteId(userID)
        cliente = Cliente.objects.filter(customer_id=idCliente).first()
        serializer = DatosSerializer(cliente, context={'request':request})
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

def index(request):
  template = loader.get_template('principal/index.html')
  userID = request.user.id
  if userID is not None:
        idCliente = obtenerClienteId(userID)
        nombreCliente = obtenerNombreCliente(idCliente)
  else: 
    nombreCliente = 'Anónimo'
  context = {'nombreCliente': nombreCliente }
  return HttpResponse(template.render(context, request))

def obtenerClienteId(userID):
    userCliente = UserCliente.objects.filter(id_user = userID)
    for x in userCliente:
        idCliente = x.id_cliente
    return idCliente

def obtenerNombreCliente(idCliente):
  cliente = Cliente.objects.filter(customer_id = idCliente)
  for x in cliente:
        nombreCliente = x.customer_name
  return nombreCliente