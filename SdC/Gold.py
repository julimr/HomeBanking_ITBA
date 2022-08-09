#Importación de módulos
from Clientes import Cliente
from Exceptions import NoPuedeCrearExcedeElLimite, NoPuedeComprarDolaresExcedeDineroDisponible, NoPuedeComprarDolaresExcedeMontoMaximo
from Cuentas import CuentaAhorroEnDolares, CuentaCorriente

class Gold(Cliente):
    """
    Hereda de la clase Cliente. Se redefinen los valores y métodos para
    determinar que y que no puede hacer un cliente Gold
    """
    cupoDiario = 20000
    comisionTransferencias = 0.005
    montoMaximoTrasferenciasRecibidas = 500000
    saldoDescubiertoDisponible = -10000
    def __init__(self, datos):
        #Constructor de clase. Hereda de cliente
        super().__init__(datos)
        #Se crean las cuentas correspondientes a un cliente Gold y las guardamos
        cuentaCorriente = CuentaCorriente(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        cuentaAhorroEnDolares = CuentaAhorroEnDolares(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        self.cuentasBancarias['cuentaCorriente'] = cuentaCorriente
        self.cuentasBancarias['cuentaAhorroEnDolares'] = cuentaAhorroEnDolares

    def puede_crear_chequera(self):
        """
        Permite determinar si el cliente puede obtener una nueva chequera.
        """
        #Si es mayor o igual a 1, lanzamos un error.
        if (self.totalChequerasActualmente >= 1):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva chequera porque excede el límite (1 chequera).')

    def puede_crear_tarjeta_credito(self):
        """
        Permite determinar si el cliente puede obtener una nueva tarjeta de crédito.
        """
        #Si es mayor o igual a 1, lanzamos un error.
        if (self.totalTarjetasDeCreditoActualmente >= 1):
            raise NoPuedeCrearExcedeElLimite('No puede dar de alta una nueva tarjeta de crédito porque excede el límite (1 tarjeta de crédito).')

    def puede_comprar_dolar(self, monto, saldoEnCuenta, cupoDiarioRestante):
        """
        Permite determinar si el cliente puede comprar dólares.
        """
        #Si el monto es mayor al saldo o el límite diario restante, lanzamos un error.
        if (monto > saldoEnCuenta):
            raise NoPuedeComprarDolaresExcedeDineroDisponible(f'No hay suficiente dinero disponible en la cuenta. Disponible: ${saldoEnCuenta}')
        elif (monto > self.cupoDiario):
            raise NoPuedeComprarDolaresExcedeMontoMaximo(f'No puede comprar US${monto} porque excede el límite diario de ${self.cupoDiario}.')
        elif(monto > cupoDiarioRestante):
            raise NoPuedeComprarDolaresExcedeMontoMaximo(f'No puede comprar US${monto} porque excede el cupo diario restante de ${cupoDiarioRestante}.')
    