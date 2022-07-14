
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

    
    def resolver(self,cliente, evento):
        pass

class RazonAltaChequera(Razon):
    def __init__(self, datos):
        super().__init__(datos)
    
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, datos):
        super().__init__(datos)

class RazonCompraDolar(Razon):
    def __init__(self, datos):
        super().__init__(datos)

class RazonRetiroEfectivo(Razon):
    def __init__(self, datos):
        super().__init__(datos)
        
class RazonTransferenciaEnviada(Razon):
    def __init__(self, datos):
        super().__init__(datos)

class RazonTransferenciaRecibida(Razon):
    def __init__(self, datos):
        super().__init__(datos)