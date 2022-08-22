from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from clientes.models import Cliente
# Create your views here.

def index(request):
  clientes = Cliente.objects.all().values()
  template = loader.get_template('clientes/index.html')
  context = {
    'clientes' : clientes
  }
  return HttpResponse(template.render(context, request))