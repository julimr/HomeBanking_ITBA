import Clientes
import Cuentas

class Gold(Clientes, Cuentas):
    def __init__(self, nombre, apellido, numero, dni):
        super().__init__(nombre, apellido, numero, dni)
        self.caracteristicas = Cuentas(20000, 500000, 0, 0.5, 10000)
        self.cuentas=?

    def puede_crear_chequera():
        return True

    def puede_crear_tarjeta_credito():
        return True

    def puede_comprar_dolar():
        return True
