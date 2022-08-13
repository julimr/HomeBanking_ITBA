from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



from prestamos.models import Prestamo
from .forms import PrestamosForm

# Create your views here.
def index(request): 
    prestamos = Prestamo.objects.all().values()
    template = loader.get_template('prestamos/index.html')
    context = {
        'prestamos' : prestamos
    }
    return HttpResponse(template.render(context, request))

def prestamos(request):
    if request.method == "POST":
        forms = PrestamosForm(request.POST)
        #Una vez que este el login, hay que hacer esta verificacion:
        #El cliente debe poder elegir el tipo de préstamo y la fecha de inicio.
        # # El monto de pre aprobación depende del tipo de cliente 
        # con los siguientes límites: BLACK 500000$, GOLD 300000$ y CLASSIC 100000$
        if forms.is_valid():
            prestamo = forms.save(commit=False)
            # userLogID = request.user
            #cuentaUserLog = Cuenta.objects.filter(customer_id = userLogID).values()
            # if (cuentaUserLog.tipo_cuenta == 1 and prestamo.loan_total <= 100000 ):
            #     prestamo_aprobado(prestamo)
            # elif (cuentaUserLog.tipo_cuenta == 2 and prestamo.loan_total <= 300000):
            #     prestamo_aprobado(prestamo)
            # elif (cuentaUserLog.tipo_cuenta == 3 and prestamo.loan_total <= 500000):
            #     prestamo_aprobado(prestamo)
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