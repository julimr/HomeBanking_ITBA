from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from prestamos.models import Prestamo, Cliente
from .forms import PrestamosForm

# Create your views here.
def index(request): 
    prestamos = Prestamo.objects.all().values()
    userLogID = request.user.id
    if userLogID is not None:
        prestamosDelCliente = prestamos.filter(customer_id = userLogID)
        context = { 'prestamos' : prestamosDelCliente }
    else: 
        context = { 'prestamos' : prestamos }
    template = loader.get_template('prestamos/index.html')
    return HttpResponse(template.render(context, request))

def prestamos(request):
    if request.method == "POST":
        forms = PrestamosForm(request.POST)
        #Una vez que este el login, hay que hacer esta verificacion:
        if forms.is_valid():
            prestamo = forms.save(commit=False)
            # userLogID = request.user.id
            # cuentaUserLog = Cliente.objects.filter(customer_id = userLogID)
            # if (cuentaUserLog.tipo_cliente_id == 1 and prestamo.loan_total <= 100000 ):
            #     prestamo_aprobado(prestamo)
            # elif (cuentaUserLog.tipo_cliente_id == 2 and prestamo.loan_total <= 300000):
            #      prestamo_aprobado(prestamo)
            # elif (cuentaUserLog.tipo_cliente_id == 3 and prestamo.loan_total <= 500000):
            #     prestamo_aprobado(prestamo)
            # prestamo.customer_id = userLogID
            prestamo.customer_id = 12
            prestamo.loan_date = datetime.now().date()
            
            prestamo.save()
            return HttpResponseRedirect(reverse('prestamos'))
    else:
        forms = PrestamosForm()
    return render(request, "Prestamos/prestamos.html", {"forms": forms})

def prestamo_aprobado(prestamo):
    prestamo.customer_id = 12 
    prestamo.loan_date = datetime.now().date()
    prestamo.save()
    return HttpResponseRedirect(reverse('prestamos'))