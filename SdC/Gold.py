from Clientes import Cliente
from Cuentas import Cuentas
from Exceptions import NoPuedeCrearExcedeElLimite, NoPuedeRetirarExcedeMontoMaximo
from SdC.Cuentas import CuentaAhorroEnDolares, CuentaCorriente


class Gold(Cliente):
    cupoDiario = 20000
    comisionTransferencias = 0.005
    montoMaximoTrasferenciasRecibidas = 500000
    saldoDescubiertoDisponible = -10000
    def __init__(self, datos):
        super().__init__(datos)
        self.caracteristicas = Cuentas(20000, 500000, 0, 0.5, 10000)
        self.cuentas = self.caracteristicas.definirCajas(False, True, True)
        self.maximos = self.caracteristicas.definirMaximos(1,1,1)
        cuentaCorriente = CuentaCorriente(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        cuentaAhorroEnDolares = CuentaAhorroEnDolares(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        self.cuentasBancarias['cuentaCorriente'] = cuentaCorriente
        self.cuentasBancarias['cuentaAhorroEnDolares'] = cuentaAhorroEnDolares

    def puede_crear_chequera(self):
        if (self.totalChequerasActualmente >= 1):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva chequera porque excede el límite (1 chequera).')

    def puede_crear_tarjeta_credito(self):
        if (self.totalTarjetasDeCreditoActualmente >= 1):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva tarjeta de crédito porque excede el límite (1 tarjeta de crédito).')

    def puede_comprar_dolar(self):
        return True
    