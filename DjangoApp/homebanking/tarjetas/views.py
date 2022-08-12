from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tarjetas.models import Tarjeta
# Create your views here.

def index(request):
  tarjetas = Tarjeta.objects.all().values()
  template = loader.get_template('tarjetas/index.html')
  context = {
    'tarjetas' : tarjetas
  }
  return HttpResponse(template.render(context, request))