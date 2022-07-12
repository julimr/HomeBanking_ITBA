'''
Código de Rogelio

class Cliente:
    def _init_(self, nombre, apelldo, numero, dni, crearChequera, crearTarjetaC, comprarDolar):
        self.nombre = nombre
        self.apellido = apelldo
        self.numero = numero
        self.dni = dni
        self.cuenta = Cuenta(crearChequera, crearTarjetaC, comprarDolar)


class Cuenta:
    def _init_(self, crearChequera, crearTarjetaC, comprarDolar):
        self.crearChequera = crearChequera
        self.crearTarjetaC = crearTarjetaC
        self.comprarDolar = comprarDolar

class Classic (Cuenta):   

    def _init_(self, crearChequera, crearTarjetaC, comprarDolar):
       super()._init_(crearChequera, crearTarjetaC, comprarDolar) 

class Gold (Cuenta):   

    def _init_(self, crearChequera, crearTarjetaC, comprarDolar):
        super()._init_(crearChequera, crearTarjetaC, comprarDolar) 

class Black (Cuenta):   

    def _init_(self, crearChequera, crearTarjetaC, comprarDolar):
        super()._init_(crearChequera, crearTarjetaC, comprarDolar)

'''