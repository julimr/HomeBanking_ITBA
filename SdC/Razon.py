#Importamos todas las clases de Exceptions
from Exceptions import NoPuedeCrearExcedeElLimite, NoPuedePorClienteClassic, NoPuedeRealizarTransferenciaNoHayDineroDisponible, NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo, NoPuedeRetirarExcedeDineroDisponible, NoPuedeRetirarExcedeMontoMaximo, NoPuedeComprarDolaresExcedeDineroDisponible, NoPuedeComprarDolaresExcedeMontoMaximo

class Razon:
    """
    Obtiene todos los datos correspondientes a la lista de transacciones del cliente
    """
    def __init__(self, datos):
        """
        Constructor de clase Razón
        @param datos -> diccionario con los datos de transacciones
        """
        self.estado = datos['estado']
        self.tipo = datos['tipo']
        self.cuentaNumero = datos['cuentaNumero']
        self.cupoDiarioRestante = datos['cupoDiarioRestante']
        self.monto = datos['monto']
        self.fecha = datos['fecha']
        self.numero = datos['numero']
        self.saldoEnCuenta = datos['saldoEnCuenta']
        self.totalTarjetasDeCreditoActualmente = datos['totalTarjetasDeCreditoActualmente']
        self.totalChequerasActualmente = datos['totalChequerasActualmente']

    
    def resolver(self,cliente):
        pass

class RazonAltaChequera(Razon):
    """
    Nos permite resolver cuando el cliente pide crear una nueva chequera
    """
    def __init__(self, datos):
        """
        Constructor de la clase. Hereda de Razón. 
        """
        super().__init__(datos)
    
    def resolver(self, cliente):
        """
        Determina si el cliente puede crear una chequera
        """
        #Preguntamos si la operación fue rechazada
        if (self.estado == 'RECHAZADA'):
            try:
                #Determinamos si puede crear una chequera
                cliente.puede_crear_chequera()
                #Si no puede, vemos si es porque es un cliente Classic
            except NoPuedePorClienteClassic as e:
                return e.mensaje
                #O si no puede por exceder el limite de chequeras
            except NoPuedeCrearExcedeElLimite as e:
                return e.mensaje
        #En caso de que la operacion es aceptada, devolvemos vacío
        else: 
            return ''
    
class RazonAltaTarjetaCredito(Razon):
    """
    Nos permite resolver cuando el cliente pide crear una nueva tarjeta de crédito
    """
    def __init__(self, datos):
        """
        Constructor de la clase. Hereda de Razón. 
        """
        super().__init__(datos)
    
    def resolver(self, cliente):
        """
        Determina si el cliente puede crear una tarjeta de crédito
        """
        #Preguntamos si la operación fue rechazada
        if (self.estado == 'RECHAZADA'):
            try:
                #Determinamos si puede crear una tarjeta
                cliente.puede_crear_tarjeta_credito()
                #Si no puede, vemos si es porque es un cliente Classic
            except NoPuedePorClienteClassic as e:
                return e.mensaje
                #O si no puede por exceder el limite de tarjetas
            except NoPuedeCrearExcedeElLimite as e:
                return e.mensaje
        #En caso de que la operacion es aceptada, devolvemos vacío
        else: 
            return ''

class RazonCompraDolar(Razon):
    """
    Nos permite resolver cuando el cliente pide comprar dólares
    """
    def __init__(self, datos):
        """
        Constructor de la clase. Hereda de Razón. 
        """
        super().__init__(datos)
    
    def resolver(self, cliente):
        """
        Determina si el cliente puede comprar dolares
        """
        #Preguntamos si la operación fue rechazada
        if (self.estado == 'RECHAZADA'):
            try:
                #Pasamos los datos y comprobamos si puede
                cliente.puede_comprar_dolar(self.monto, self.saldoEnCuenta, self.cupoDiarioRestante)
                #Si es classic, no podrá
            except NoPuedePorClienteClassic as e:
                return e.mensaje
                #Si excede el monto máximo o excede su dinero disponible, tampoco
            except NoPuedeComprarDolaresExcedeMontoMaximo as e:
                return e.mensaje
            except NoPuedeComprarDolaresExcedeDineroDisponible as e:
               return e.mensaje 
        #En caso de que la operacion es aceptada, devolvemos vacío
        else: 
            return ''

class RazonRetiroEfectivo(Razon):
    """
    Nos permite resolver cuando el cliente pide retirar efectivo
    """
    def __init__(self, datos):
        """
        Constructor de la clase. Hereda de Razón. 
        """
        super().__init__(datos)
    
    def resolver(self, cliente):
        """
        Determina si el cliente puede retirar efectivo
        """
        #Preguntamos si la operación fue rechazada
        if (self.estado == 'RECHAZADA'):
            try:
                #Comprobamos si puede retirar con el dinero disponible
                cliente.puede_retirar(self.monto,self.cupoDiarioRestante, self.saldoEnCuenta)
                #Si no puede, es por exceder lo disponible o por exceder el monto máximo diario
            except NoPuedeRetirarExcedeDineroDisponible as e:
                return e.mensaje
            except NoPuedeRetirarExcedeMontoMaximo as e:
                return e.mensaje
        #En caso de que la operacion es aceptada, devolvemos vacío
        else: 
            return ''
        
class RazonTransferenciaEnviada(Razon):
    """
    Nos permite resolver cuando el cliente realiza transferencias
    """
    def __init__(self, datos):
        """
        Constructor de la clase. Hereda de Razón. 
        """
        super().__init__(datos)
    
    def resolver(self, cliente):
        """
        Determina si el cliente puede realizar la transferencia
        """
        #Preguntamos si la operación fue rechazada
        if (self.estado == 'RECHAZADA'):
            try:
                #Si no puede realizarla, es por exceder el dinero disponible
                cliente.puede_realizar_transferencia(self.monto, self.saldoEnCuenta)
            except NoPuedeRealizarTransferenciaNoHayDineroDisponible as e:
                return e.mensaje
        #En caso de que la operacion es aceptada, devolvemos vacío
        else: 
            return ''

class RazonTransferenciaRecibida(Razon):
    """
    Nos permite resolver cuando el cliente recibe una transferencia
    """
    def __init__(self, datos):
        super().__init__(datos)
    
    def resolver(self, cliente):
        """
        Determina si el cliente puede recibir el monto de la transferencia
        """
        #Preguntamos si la operación fue rechazada
        if (self.estado == 'RECHAZADA'):
            try:
                #Si no puede, es porque excede lo máximo que puede recibir sin aviso
                cliente.puede_recibir_transferencia(self.monto)
            except NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo as e:
                return e.mensaje
        #En caso de que la operacion es aceptada, devolvemos vacío
        else: 
            return ''