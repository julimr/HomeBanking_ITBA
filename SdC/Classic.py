from Clientes import Cliente
from Cuentas import Cuentas
from Exceptions import NoPuedePorClienteClassic


class Classic(Cliente):
    cupoDiario = 10000
    comisionTransferencias = 0.01
    montoMaximoTrasferenciasRecibidas = 150000
    def __init__(self, datos):
        super().__init__(datos)
        self.caracteristicas = Cuentas(10000, 150000, 0, 1, 0)
        self.cuentas = self.caracteristicas.definirCajas(True, False, False)
        self.maximos = self.caracteristicas.definirMaximos(1,0,0)

    def puede_crear_chequera(self):
        raise NoPuedePorClienteClassic('No puede dar de alta una chequera porque el Cliente Classic no lo tiene permitido.')

    def puede_crear_tarjeta_credito(self):
        raise NoPuedePorClienteClassic('No puede dar de alta una tarjeta de crédito porque el Cliente Classic no lo tiene permitido.')

    def puede_comprar_dolar(self):
        raise NoPuedePorClienteClassic('No puede comprar dólares porque el Cliente Classic no lo permite.')


