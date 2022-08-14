from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from principal.models import Cliente, UserCliente

# Create your views here.
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