from Clientes import Cliente
from Cuentas import Cuentas
from Exceptions import NoPuedePorClienteClassic
from SdC.Cuentas import CuentaAhorroEnPesos
from Tarjetas import TarjetaDebito


class Classic(Cliente):
    cupoDiario = 10000
    comisionTransferencias = 0.01
    montoMaximoTrasferenciasRecibidas = 150000
    saldoDescubiertoDisponible = 0
    def __init__(self, datos):
        super().__init__(datos)
        cuentaAhorroPesos = CuentaAhorroEnPesos(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        self.cuentasBancarias['cuentaAhorroEnPesos'] = cuentaAhorroPesos

    def puede_crear_chequera(self):
        raise NoPuedePorClienteClassic('No puede dar de alta una chequera porque el Cliente Classic no lo tiene permitido.')

    def puede_crear_tarjeta_credito(self):
        raise NoPuedePorClienteClassic('No puede dar de alta una tarjeta de crédito porque el Cliente Classic no lo tiene permitido.')

    def puede_comprar_dolar(self):
        raise NoPuedePorClienteClassic('No puede comprar dólares porque el Cliente Classic no lo permite.')


