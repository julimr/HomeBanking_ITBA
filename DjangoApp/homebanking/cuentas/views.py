from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cuentas.models import Cuenta
# Create your views here.

def index(request):
  cuentas = Cuenta.objects.all().values()
  template = loader.get_template('cuentas/index.html')
  context = {
    'cuentas' : cuentas
  }
  return HttpResponse(template.render(context, request))