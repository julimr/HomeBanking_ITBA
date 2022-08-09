#Importación de módulos
from Clientes import Cliente
from Exceptions import NoPuedePorClienteClassic
from Cuentas import CuentaAhorroEnPesos

class Classic(Cliente):
    """
    Hereda de la clase Cliente. Se redefinen los valores y métodos para
    determinar que y que no puede hacer un cliente Classic
    """
    cupoDiario = 10000
    comisionTransferencias = 0.01
    montoMaximoTrasferenciasRecibidas = 150000
    saldoDescubiertoDisponible = 0
    def __init__(self, datos):
        #Constructor de clase. Hereda de Cliente
        super().__init__(datos)
        #Se crean la cuenta correspondiente a un cliente Classic y la guardamos
        cuentaAhorroPesos = CuentaAhorroEnPesos(self.cupoDiario, self.montoMaximoTrasferenciasRecibidas, self.comisionTransferencias, self.saldoDescubiertoDisponible)
        self.cuentasBancarias['cuentaAhorroEnPesos'] = cuentaAhorroPesos

    def puede_crear_chequera(self):
        """
        Nos permite lanzar un error, ya que el cliente Classic no puede solicitar chequeras
        """
        raise NoPuedePorClienteClassic('No puede dar de alta una chequera porque el Cliente Classic no lo tiene permitido.')

    def puede_crear_tarjeta_credito(self):
        """
        Nos permite lanzar un error, ya que el cliente Classic no puede solicitar tarjetas
        """
        raise NoPuedePorClienteClassic('No puede dar de alta una tarjeta de crédito porque el Cliente Classic no lo tiene permitido.')

    def puede_comprar_dolar(self, monto, saldoEnCuenta, cupoDiarioRestante):
        """
        Nos permite lanzar un error, ya que el cliente Classic no puede comprar dólares
        """
        raise NoPuedePorClienteClassic('No puede comprar dólares porque el Cliente Classic no lo permite.')


