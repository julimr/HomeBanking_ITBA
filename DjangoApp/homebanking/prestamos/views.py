from datetime import datetime
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import TiposCliente
from prestamos.models import Prestamo, Cliente,  UserCliente, Cuenta
from .forms import PrestamosForm

# Create your views here.
def index(request): 
    prestamos = Prestamo.objects.all().values()
    userID = request.user.id
    if userID is not None:
        idCliente = obtenerClienteId(userID)
        prestamosDelCliente = prestamos.filter(customer_id = idCliente)
        context = { 'prestamos' : prestamosDelCliente , 'userID' : userID }
        if len(prestamosDelCliente) == 0:
            messages.info(request, 'No tiene préstamos.')
    else: 
        context = { 'prestamos' : prestamos, 'userID' : userID }
    template = loader.get_template('prestamos/index.html')
    return HttpResponse(template.render(context, request))

def prestamos(request):
    if request.method == "POST":
        forms = PrestamosForm(request.POST)
        montoPrestamo = request.POST['loan_total']
        userID = request.user.id
        clienteID = obtenerClienteId(userID)
        tipoClienteID = obtenerTipoClienteID(clienteID)
        if forms.is_valid():
            prestamo = forms.save(commit=False)
            if (tipoClienteID == 1 and prestamo.loan_total <= 100000 ):
                prestamo_aprobado(prestamo, clienteID,montoPrestamo)
                return HttpResponseRedirect(reverse('prestamos'))
            elif (tipoClienteID == 2 and prestamo.loan_total <= 300000):
                prestamo_aprobado(prestamo, clienteID, montoPrestamo)
                return HttpResponseRedirect(reverse('prestamos'))
            elif (tipoClienteID == 3 and prestamo.loan_total <= 500000):
                prestamo_aprobado(prestamo, clienteID, montoPrestamo)
                return HttpResponseRedirect(reverse('prestamos'))
            else :
                tipoCliente = obtenerTipoCliente(tipoClienteID)
                messages.error(request, "No cumple con los requisitos para pedir un préstamo de ese monto.")
                messages.error(request, f"Usted es cliente {tipoCliente}")
                if (tipoClienteID == 1): messages.error(request, "Puede pedir hasta $100.000")
                if (tipoClienteID == 2): messages.error(request, "Puede pedir hasta $300.000")
                if (tipoClienteID == 3): messages.error(request, "Puede pedir hasta $500.000")
    else:
        forms = PrestamosForm()
    return render(request, "Prestamos/prestamos.html", {"forms": forms})

def prestamo_aprobado(prestamo, clienteID, montoPrestamo):
    prestamo.customer_id = clienteID
    prestamo.loan_date = datetime.now().date()
    prestamo.save()
    actualizarBalanceCliente(clienteID, montoPrestamo)
   
def actualizarBalanceCliente(clienteID, montoPrestamo):
    cuentas = Cuenta.objects.filter(customer_id = clienteID)
    #Aca le agregue 2 ceros ya que los ultimos 2 numeros en la bd corresponden a los decimales
    montoFinal = montoPrestamo + '00' 
    for x in cuentas:
        balanceAnterior = x.balance
        x.balance = balanceAnterior - int(montoFinal)
        x.save()

def obtenerClienteId(userID):
    userCliente = UserCliente.objects.filter(id_user = userID)
    for x in userCliente:
        idCliente = x.id_cliente
    return idCliente

def obtenerTipoClienteID(clienteID):
    cliente = Cliente.objects.filter(customer_id = clienteID)
    for x in cliente:
        tipo_cliente_id = x.tipo_cliente
    return tipo_cliente_id

def obtenerTipoCliente(tipo_cliente_id):
    tipoCliente = TiposCliente.objects.filter(tipo_cliente_id = tipo_cliente_id)
    for x in tipoCliente:
        tipo_cliente = x.tipo_cliente
    return tipo_cliente