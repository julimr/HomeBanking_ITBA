import Clientes
import Cuentas

class Classic(Clientes, Cuentas):
    def __init__(self, nombre, apellido, numero, dni):
        super().__init__(nombre, apellido, numero, dni)
        self.caracteristicas = Cuentas(10000, 150000, 0, 1, 0)
        self.cuentas = ?

    def puede_crear_chequera():
        return True

    def puede_crear_tarjeta_credito():
        return False

    def puede_comprar_dolar():
        return False

    #Hay que definir los metodos para crear tarjetas y eso, y comprobar que no se pasen de su limite. Lo mismo en los tres tipos de cuenta
