from Direccion import Direccion
from convertirSalidaTPS import *

dataDict = convertToDict('salidaTPS.json')

class Clientes:

    def __init__(self, datos=dataDict):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['DNI']
        self.direccion = Direccion(datos['direccion']['calle'],
                                    datos['direccion']['numero'],
                                    datos['direccion']['ciudad'],
                                    datos['direccion']['provincia'],
                                    datos['direccion']['pais'])
        self.tipo = datos["tipo"]

    def puede_crear_chequera():
        return None
    
    def puede_crear_tarjeta_credito():
        return None

    def puede_comprar_dolar():
        return None
    
    def cantTarjetasCredito(self, datos):
        return datos['transacciones']['totalTarjetasDeCreditoActualmente']

    def cantChequeras(self, datos):
        return datos['transacciones']['totalChequerasActualmente']
