from Clientes import Clientes
from Cuentas import Cuentas
from convertirSalidaTPS import *

class Gold(Clientes):
    def __init__(self, datos):
        super().__init__(datos)
        self.caracteristicas = Cuentas(20000, 500000, 0, 0.5, 10000)
        self.cuentas = self.caracteristicas.definirCajas(False, True, True)
        self.maximos = self.caracteristicas.definirMaximos(1,1,1)

    def puede_crear_chequera():
        return True

    def puede_crear_tarjeta_credito():
        return True

    def puede_comprar_dolar():
        return True
