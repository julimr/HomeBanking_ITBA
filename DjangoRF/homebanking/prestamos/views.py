from datetime import datetime
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import TiposCliente
from prestamos.models import Prestamo, Cliente,  UserCliente, Cuenta
from .forms import PrestamosForm
from .serializers import PrestamoSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class PrestamosCliente(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request, pk):
        prestamosCliente = Prestamo.objects.filter(customer_id=pk)
        serializer = PrestamoSerializer(prestamosCliente, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            monto = serializer.validated_data.get('loan_total')
            id = serializer.validated_data.get('customer_id')
            actualizarBalanceCliente(id, monto)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EliminarPrestamo(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request, pk):
        prestamo = Prestamo.objects.filter(loan_id=pk)
        serializer = PrestamoSerializer(prestamo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if prestamo:
            serializer = PrestamoSerializer(prestamo)
            monto = serializer.data['loan_total']
            id = serializer.data['customer_id']
            restarBalanceCliente(id, monto)
            prestamo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

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
    montoFinal = montoPrestamo
    for x in cuentas:
        balanceAnterior = x.balance
        x.balance = int(balanceAnterior) + int(montoFinal)
        x.save()

def restarBalanceCliente(clienteID, montoPrestamo):
    cuentas = Cuenta.objects.filter(customer_id = clienteID)
    montoFinal = montoPrestamo
    for x in cuentas:
        balanceAnterior = x.balance
        x.balance = int(balanceAnterior) - int(montoFinal)
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