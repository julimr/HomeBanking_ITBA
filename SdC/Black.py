from .Clientes import Clientes
from .Cuentas import Cuentas
from convertirSalidaTPS import *
dataDict = convertToDict('salidaTPS.json')

class Black(Clientes, Cuentas):
    def __init__(self):
        super().__init__(datos=dataDict)
        self.caracteristicas = Cuentas(100000, 500000, 0, 0, 10000)
        self.cuentas = self.caracteristicas.definirCajas(True, True, True)
        self.maximos = self.caracteristicas.definirMaximos(0,5,2)

    def puede_crear_chequera():
        return True

    def puede_crear_tarjeta_credito():
        return True

    def puede_comprar_dolar():
        return True

