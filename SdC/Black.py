from Clientes import Cliente
from Cuentas import Cuentas
from Exceptions import NoPuedeCrearExcedeElLimite, NoPuedeComprarDolaresExcedeDineroDisponible, NoPuedeComprarDolaresExcedeMontoMaximo 
from Cuentas import CuentaAhorroEnDolares, CuentaAhorroEnPesos, CuentaCorriente


class Black(Cliente):
    cupoDiario = 100000
    comisionTransferencias = 0
    montoMaximoTrasferenciasRecibidas = 0
    saldoDescubiertoDisponible = -10000
    def __init__(self, datos):
        super().__init__(datos)
        cuentaAhorroPesos = CuentaAhorroEnPesos(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        cuentaCorriente = CuentaCorriente(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        cuentaAhorroEnDolares = CuentaAhorroEnDolares(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        self.cuentasBancarias['cuentaAhorroEnPesos'] = cuentaAhorroPesos
        self.cuentasBancarias['cuentaCorriente'] = cuentaCorriente
        self.cuentasBancarias['cuentaAhorroEnDolares'] = cuentaAhorroEnDolares

    def puede_crear_chequera(self):
        if (self.totalChequerasActualmente >= 2):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva chequera porque excede el límite (2 chequeras).')

    def puede_crear_tarjeta_credito(self):
        if (self.totalTarjetasDeCreditoActualmente >= 5):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva tarjeta de crédito porque excede el límite (5 tarjetas).')

    def puede_comprar_dolar(self, monto, saldoEnCuenta, cupoDiarioRestante):
        if (monto > saldoEnCuenta):
            raise NoPuedeComprarDolaresExcedeDineroDisponible(f'No hay suficiente dinero disponible en la cuenta. Disponible: ${saldoEnCuenta}')
        elif (monto > self.cupoDiario):
            raise NoPuedeComprarDolaresExcedeMontoMaximo(f'No puede comprar US${monto} porque excede el límite diario de ${self.cupoDiario}.')
        elif(monto > cupoDiarioRestante):
            raise NoPuedeComprarDolaresExcedeMontoMaximo(f'No puede comprar US${monto} porque excede el cupo diario restante de ${cupoDiarioRestante}.')
    
    def puede_recibir_transferencia(self, monto):
        pass