
from Exceptions import NoPuedeCrearExcedeElLimite, NoPuedePorClienteClassic, NoPuedeRealizarTransferenciaNoHayDineroDisponible, NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo, NoPuedeRetirarExcedeDineroDisponible, NoPuedeRetirarExcedeMontoMaximo, NoPuedeComprarDolaresExcedeDineroDisponible, NoPuedeComprarDolaresExcedeMontoMaximo


class Razon:
    def __init__(self, datos):
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
    def __init__(self, datos):
        super().__init__(datos)
    
    def resolver(self, cliente):
        if (self.estado == 'RECHAZADA'):
            try:
                cliente.puede_crear_chequera()
            except NoPuedePorClienteClassic as e:
                return e.mensaje
            except NoPuedeCrearExcedeElLimite as e:
                return e.mensaje
        else: 
            return ''
    
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, datos):
        super().__init__(datos)
    
    def resolver(self, cliente):
        if (self.estado == 'RECHAZADA'):
            try:
                cliente.puede_crear_tarjeta_credito()
            except NoPuedePorClienteClassic as e:
                return e.mensaje
            except NoPuedeCrearExcedeElLimite as e:
                return e.mensaje
        else: 
            return ''

class RazonCompraDolar(Razon):
    def __init__(self, datos):
        super().__init__(datos)
    
    def resolver(self, cliente):
        if (self.estado == 'RECHAZADA'):
            try:
                cliente.puede_comprar_dolar(self.monto, self.saldoEnCuenta, self.cupoDiarioRestante)
            except NoPuedePorClienteClassic as e:
                return e.mensaje
            except NoPuedeComprarDolaresExcedeMontoMaximo as e:
                return e.mensaje
            except NoPuedeComprarDolaresExcedeDineroDisponible as e:
               return e.mensaje 
        else: 
            return ''

class RazonRetiroEfectivo(Razon):
    def __init__(self, datos):
        super().__init__(datos)
    
    def resolver(self, cliente):
        if (self.estado == 'RECHAZADA'):
            try:
                cliente.puede_retirar(self.monto,self.cupoDiarioRestante, self.saldoEnCuenta)
            except NoPuedeRetirarExcedeDineroDisponible as e:
                return e.mensaje
            except NoPuedeRetirarExcedeMontoMaximo as e:
                return e.mensaje
        else: 
            return ''
        
class RazonTransferenciaEnviada(Razon):
    def __init__(self, datos):
        super().__init__(datos)
    
    def resolver(self, cliente):
        if (self.estado == 'RECHAZADA'):
            try:
                cliente.puede_realizar_transferencia(self.monto, self.saldoEnCuenta)
            except NoPuedeRealizarTransferenciaNoHayDineroDisponible as e:
                return e.mensaje
        else: 
            return ''

class RazonTransferenciaRecibida(Razon):
    def __init__(self, datos):
        super().__init__(datos)
    
    def resolver(self, cliente):
        if (self.estado == 'RECHAZADA'):
            try:
                cliente.puede_recibir_transferencia(self.monto)
            except NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo as e:
                return e.mensaje
        else: 
            return ''