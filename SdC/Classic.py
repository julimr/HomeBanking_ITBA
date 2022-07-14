from Clientes import Cliente
from Cuentas import Cuentas
from convertirSalidaTPS import *

class Classic(Cliente):
    def __init__(self, datos):
        super().__init__(datos)
        self.caracteristicas = Cuentas(10000, 150000, 0, 1, 0)
        self.cuentas = self.caracteristicas.definirCajas(True, False, False)
        self.maximos = self.caracteristicas.definirMaximos(1,0,0)

    def puede_crear_chequera():
        return True

    def puede_crear_tarjeta_credito():
        return False

    def puede_comprar_dolar():
        return False

