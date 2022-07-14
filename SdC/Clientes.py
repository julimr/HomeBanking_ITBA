
from Direccion import Direccion
from Razon import RazonAltaChequera, RazonAltaTarjetaCredito, RazonCompraDolar, RazonRetiroEfectivo, RazonTransferenciaEnviada, RazonTransferenciaRecibida

class Cliente:
    def __init__(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['dni']
        self.direccion = Direccion(datos['direccion']['calle'],
                                    datos['direccion']['numero'],
                                    datos['direccion']['ciudad'],
                                    datos['direccion']['provincia'],
                                    datos['direccion']['pais'])
        self.transacciones = self.clasificar_transacciones(datos['transacciones'])

    def puede_crear_chequera():
        return None
    
    def puede_crear_tarjeta_credito():
        return None

    def puede_comprar_dolar():
        return None
    
    def puede_retirar(monto):
        return True

    def cantTarjetasCredito(datos):
        return datos['transacciones']['totalTarjetasDeCreditoActualmente']

    def cantChequeras(datos):
        return datos['transacciones']['totalChequerasActualmente']
    
    def clasificar_transacciones(self,datosTransacciones):
        transacciones = []
        for transaccion in datosTransacciones:
            if(transaccion['tipo'] == "ALTA_CHEQUERA"):
                transacciones.append(RazonAltaChequera(transaccion))
            elif(transaccion['tipo'] == "ALTA_TARJETA_CREDITO"):
                transacciones.append(RazonAltaTarjetaCredito(transaccion))
            elif(transaccion['tipo'] == "COMPRA_DOLAR"):
                transacciones.append(RazonCompraDolar(transaccion))
            elif(transaccion['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO"):
                transacciones.append(RazonRetiroEfectivo(transaccion))
            elif(transaccion['tipo'] == "TRANSFERENCIA_ENVIADA"):
                transacciones.append(RazonTransferenciaEnviada(transaccion))
            elif(transaccion['tipo'] == "TRANSFERENCIA_RECIBIDA"):
               transacciones.append(RazonTransferenciaRecibida(transaccion))
            else:
                AssertionError("El tipo de transacción es inválido")
        return transacciones
    
