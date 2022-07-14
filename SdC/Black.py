from Clientes import Cliente
from Cuentas import Cuentas
from Exceptions import NoPuedeCrearExcedeElLimite 


class Black(Cliente):
    cupoDiario = 100000
    comisionTransferencias = 0
    montoMaximoTrasferenciasRecibidas = 0
    def __init__(self, datos):
        super().__init__(datos)
        self.caracteristicas = Cuentas(100000, 500000, 0, 0, 10000)
        self.cuentas = self.caracteristicas.definirCajas(True, True, True)
        self.maximos = self.caracteristicas.definirMaximos(0,5,2)

    def puede_crear_chequera(self):
        if (self.totalChequerasActualmente >= 2):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva chequera porque excede el límite (2 chequeras).')

    def puede_crear_tarjeta_credito(self):
        if (self.totalChequerasActualmente >= 5):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva tarjeta de crédito porque excede el límite (5 tarjetas).')

    def puede_comprar_dolar(self):
        pass
    
    def puede_recibir_transferencia(self, monto):
        pass