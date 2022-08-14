from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cuentas.models import Cuenta, UserCliente
from django.contrib import messages
# Create your views here.

def index(request):
  cuentas = Cuenta.objects.all().values()
  userID = request.user.id
  if userID is not None:
    idCliente = obtenerClienteID(userID)
    cuentasDelCliente = cuentas.filter(customer_id = idCliente)
    context = { 'cuentas' : cuentasDelCliente }
    if len(cuentasDelCliente) == 0:
      messages.info(request, 'No tiene cuentas a su nombre.')
  else: 
        context = { 'cuentas' : cuentas }
  template = loader.get_template('cuentas/index.html')
  return HttpResponse(template.render(context, request))

def obtenerClienteID(userID):
  userCliente = UserCliente.objects.filter(id_user = userID)
  for x in userCliente:
      idCliente = x.id_cliente
  return idCliente