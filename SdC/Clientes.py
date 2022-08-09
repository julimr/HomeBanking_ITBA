#Importación de modulos

from Direccion import Direccion
from Razon import RazonAltaChequera, RazonAltaTarjetaCredito, RazonCompraDolar, RazonRetiroEfectivo, RazonTransferenciaEnviada, RazonTransferenciaRecibida
from Exceptions import NoPuedeRealizarTransferenciaNoHayDineroDisponible, NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo, NoPuedeRetirarExcedeDineroDisponible, NoPuedeRetirarExcedeMontoMaximo
from Tarjetas import TarjetaDebito

class Cliente:
    """
    Clase Padre. Se definen las claves principales de cada cliente.
    Se inicializan en 0 las variables de cada uno. En las clases
    que hereden de esta (Classic, Gold y Black), se redefiniran ciertos métodos.
    """
    totalTarjetasDeCreditoActualmente = 0
    totalChequerasActualmente = 0
    cupoDiario = 0
    comisionTransferencias = 0
    montoMaximoTrasferenciasRecibidas = 0
    tarjetas = []
    cuentasBancarias = {}
    def __init__(self, datos):
        #Constructor de clase
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
        self.tarjetas.append(TarjetaDebito(self))
        
    #Métodos definidos para la clase
    def puede_crear_chequera(self):
        """
        Devuelve True o False cuando es llamado desde una clase hija
        """
        pass
    
    def puede_crear_tarjeta_credito(self):
        """
        Devuelve True o False cuando es llamado desde una clase hija
        """
        pass

    def puede_comprar_dolar(self):
        """
        Devuelve True o False cuando es llamado desde una clase hija
        """
        pass
    
    def puede_retirar(self, monto, cupoDiarioRestante, saldoEnCuenta):
        """
        Determina si el cliente puede retirar efectivo
        @param -> monto -> monto a retirar
        @param -> cupoDiarioRestante -> dinero restante que puede retirar en el dia
        @param -> saldoEnCuenta -> Saldo actual en la cuenta
        """
        #Si lo que desea retirar excede el saldo o el cupo diario, lanzamos un error
        if (monto > saldoEnCuenta):
            raise NoPuedeRetirarExcedeDineroDisponible(f'No hay suficiente dinero disponible en la cuenta. Disponible: ${saldoEnCuenta}')
        elif (monto > self.cupoDiario):
            raise NoPuedeRetirarExcedeMontoMaximo(f'No puede retirar ${monto} porque excede el límite diario de ${self.cupoDiario}.')
        elif(monto > cupoDiarioRestante):
            raise NoPuedeRetirarExcedeMontoMaximo(f'No puede retirar ${monto} porque excede el cupo diario restante de ${cupoDiarioRestante}.')

    def puede_realizar_transferencia(self, monto, saldoEnCuenta):
        """
        Determina si el cliente puede realizar la transferencia
        @param -> monto -> monto a retirar
        @param -> saldoEnCuenta -> saldo disponible en cuenta
        """
        #Al dinero a retirar, le agregamos la comision correspondiente a la clase
        dineroARetirar = monto * ( 1 + self.comisionTransferencias)
        #Comprobamos si tiene dinero en la cuenta o lanzamos un error
        if ( dineroARetirar > saldoEnCuenta ):
            raise NoPuedeRealizarTransferenciaNoHayDineroDisponible(f'No puede realizar trasferencia porque no hay suficiente dinero en la cuenta. Disponible: ${saldoEnCuenta}. A retirar: ${round(dineroARetirar,2)}')

    def puede_recibir_transferencia(self, monto):
        """
        Determina si el cliente puede recibir una transferencia
        @param -> monto -> monto recibido
        """
        #Comprobamos si lo recibido no excede el monto máximo
        if ( monto > self.montoMaximoTrasferenciasRecibidas):
            raise NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo(f'No puede recibir la transferencia porque excede el monto máximo.')
   
    def clasificar_transacciones(self,datosTransacciones):
        ''' 
        Clasifica las transacciones dependiendo del tipo
        @return -> lista con las transacciones clasificadas
        '''
        transacciones = []
        for transaccion in datosTransacciones:
            self.totalChequerasActualmente = transaccion['totalChequerasActualmente']
            self.totalTarjetasDeCreditoActualmente = transaccion['totalTarjetasDeCreditoActualmente']
            #Según el tipo, llamamos a los diferentes hijos de la clase Razon
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
        ''' 
        Devuelve el reporte de las transacciones 
        return -> lista con el motivo de rechazo de la transacción
        '''
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
        ''' 
        Permite obtener el reporte completo del cliente
        return -> Diccionario con los datos del cliente y transacciones
        '''
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