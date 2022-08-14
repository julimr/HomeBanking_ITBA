from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tarjetas.models import Tarjeta, UserCliente
from django.contrib import messages
# Create your views here.

def index(request):
  tarjetas = Tarjeta.objects.all().values()
  userID = request.user.id
  if userID is not None:
    idCliente = obtenerClienteID(userID)
    tarjetasDelCliente = tarjetas.filter(customer_id = idCliente)
    context = { 'tarjetas' : tarjetasDelCliente }
    if len(tarjetasDelCliente) == 0:
      messages.info(request, 'No tiene tarjetas a su nombre.')
  else: 
        context = { 'tarjetas' : tarjetas }

  template = loader.get_template('tarjetas/index.html')
  return HttpResponse(template.render(context, request))


def obtenerClienteID(userID):
  userCliente = UserCliente.objects.filter(id_user = userID)
  for x in userCliente:
      idCliente = x.id_cliente
  return idCliente