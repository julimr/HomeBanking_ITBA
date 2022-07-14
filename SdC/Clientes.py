
from Direccion import Direccion
from Razon import RazonAltaChequera, RazonAltaTarjetaCredito, RazonCompraDolar, RazonRetiroEfectivo, RazonTransferenciaEnviada, RazonTransferenciaRecibida
from Exceptions import NoPuedeRealizarTransferenciaNoHayDineroDisponible, NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo, NoPuedeRetirarExcedeDineroDisponible, NoPuedeRetirarExcedeMontoMaximo

class Cliente:
    totalTarjetasDeCreditoActualmente = 0
    totalChequerasActualmente = 0
    cupoDiario = 0
    comisionTransferencias = 0
    montoMaximoTrasferenciasRecibidas = 0

    def __init__(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['dni']
        self.direccion = Direccion(datos['direccion']['calle'],
                                    datos['direccion']['numero'],
                                    datos['direccion']['ciudad'],
                                    datos['direccion']['provincia'],
                                    datos['direccion']['pais'])
        self.transacciones = self.clasificar_transacciones(datos['transacciones'])

    def puede_crear_chequera(self):
        pass
    
    def puede_crear_tarjeta_credito(self):
        pass

    def puede_comprar_dolar(self):
        pass
    
    def puede_retirar(self, monto, cupoDiarioRestante, saldoEnCuenta):
        if (monto > saldoEnCuenta):
            raise NoPuedeRetirarExcedeDineroDisponible(f'No hay suficiente dinero disponible en la cuenta. Disponible: ${saldoEnCuenta}')
        elif (monto > self.cupoDiario):
            raise NoPuedeRetirarExcedeMontoMaximo(f'No puede retirar ${monto} porque excede el límite diario de ${self.cupoDiario}.')
        elif(monto > cupoDiarioRestante):
            raise NoPuedeRetirarExcedeMontoMaximo(f'No puede retirar ${monto} porque excede el cupo diario restante de ${cupoDiarioRestante}.')

    def puede_realizar_transferencia(self, monto, saldoEnCuenta):
        dineroARetirar = monto * ( 1 + self.comisionTransferencias)
        if ( dineroARetirar > saldoEnCuenta ):
            raise NoPuedeRealizarTransferenciaNoHayDineroDisponible(f'No puede realizar trasferencia porque no hay suficiente dinero en la cuenta. Disponible: ${saldoEnCuenta}. A retirar: ${dineroARetirar}')

    def puede_recibir_transferencia(self, monto):
        if ( monto > self.montoMaximoTrasferenciasRecibidas):
            raise NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo(f'No puede recibir la transferencia porque excede el monto máximo.')

    def cantTarjetasCredito(self):
        return self.totalTarjetasDeCreditoActualmente

    def cantChequeras(self):
        return self.totalChequerasActualmente
    
    def clasificar_transacciones(self,datosTransacciones):
        ''' Clasifica las transacciones dependiendo del tipo'''
        transacciones = []
        for transaccion in datosTransacciones:
            self.totalChequerasActualmente = transaccion['totalChequerasActualmente']
            self.totalTarjetasDeCreditoActualmente = transaccion['totalTarjetasDeCreditoActualmente']
            if(transaccion['tipo'] == "ALTA_CHEQUERA"):
                transacciones.append(RazonAltaChequera(transaccion))
            elif(transaccion['tipo'] == "ALTA_TARJETA_CREDITO"):
                transacciones.append(RazonAltaTarjetaCredito(transaccion))
            elif(transaccion['tipo'] == "COMPRA_DOLAR"):
                transacciones.append(RazonCompraDolar(transaccion))
            elif(transaccion['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO"):
                transacciones.append(RazonRetiroEfectivo(transaccion))
            elif(transaccion['tipo'] == "TRANSFERENCIA_ENVIADA"):
                transacciones.append(RazonTransferenciaEnviada(transaccion))
            elif(transaccion['tipo'] == "TRANSFERENCIA_RECIBIDA"):
               transacciones.append(RazonTransferenciaRecibida(transaccion))
            else:
                AssertionError("El tipo de transacción es inválido")
        return transacciones
    
    def resolver_transacciones(self):
        ''' Devuelve el reporte de las transacciones '''
        reporteFinalTransacciones = []
        for t in self.transacciones:
            reporteTransaccion = {}
            resultado = t.resolver(self)
            reporteTransaccion['fecha'] = t.fecha
            reporteTransaccion['tipo'] = t.tipo
            reporteTransaccion['estado'] = t.estado
            reporteTransaccion['monto'] = t.monto
            reporteTransaccion['razonRechazo'] = resultado
            reporteFinalTransacciones.append(reporteTransaccion)
        return reporteFinalTransacciones
    
    def reporte_cliente(self):
        reporteCliente = {}
        reporteTransacciones = self.resolver_transacciones()
        reporteCliente['nombre'] = self.nombre
        reporteCliente['numero'] = self.numero
        reporteCliente['dni'] = self.dni
        reporteCliente['direccion'] = { 'calle': self.direccion.calle, 'numero': self.direccion.numero,
                                        'ciudad': self.direccion.ciudad, 'provincia': self.direccion.provincia,
                                        'pais': self.direccion.pais}
        reporteCliente['transacciones'] = reporteTransacciones
        return reporteCliente