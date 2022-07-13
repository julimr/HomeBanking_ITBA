from datetime import datetime
from Direccion import Direccion
from SdC.Razon import RazonAltaChequera, RazonAltaTarjetaCredito, RazonRetiroEfectivo

class Clientes:
    transacciones = []
    saldoEnCuenta = 0
    cantTarjetasCredito = 0
    cantChequeras = 0
    cupoDiarioRestante = 0
    def __init__(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['DNI']
        self.direccion = Direccion(datos['direccion']['calle'],
                                    datos['direccion']['numero'],
                                    datos['direccion']['ciudad'],
                                    datos['direccion']['provincia'],
                                    datos['direccion']['pais'])

    def puede_crear_chequera():
        return None
    
    def puede_crear_tarjeta_credito():
        return None

    def puede_comprar_dolar():
        return None
    
    def puede_retirar(monto):
        return True

    def retirar_efectivo(self,monto):
        self.saldoEnCuenta -= monto
    
    def nueva_chequera(self):
        self.cantChequeras += 1

    def cantTarjetasCredito(datos):
        return datos['transacciones']['totalTarjetasDeCreditoActualmente']

    def cantChequeras(datos):
        return datos['transacciones']['totalChequerasActualmente']
    
    def cantidad_transacciones(self):
        return len(self.transacciones)

    def RETIRO_EFECTIVO_CAJERO_AUTOMATICO(self,monto,cuentaNumero):
        if (self.puede_retirar(monto)):
            retiroEfvo = RazonRetiroEfectivo("APROBADO", cuentaNumero, self.cupoDiarioRestante , monto,datetime.now,
            self.cantidad_transacciones() +1, self.saldoEnCuenta, self.cantTarjetasCredito(), self.cantChequeras() )
            retiroEfvo.resolver(self, monto)
        else:
            retiroEfvo= RazonRetiroEfectivo("RECHAZADO", cuentaNumero, self.cupoDiarioRestante , monto,datetime.now,
            self.cantidad_transacciones() +1, self.saldoEnCuenta, self.cantTarjetasCredito(), self.cantChequeras() )

        self.transacciones.append(retiroEfvo)

    def ALTA_TARJETA_CREDITO(self, monto, cuentaNumero):
        if (self.puede_crear_tarjeta_credito()):
            nuevaTarjeta = RazonAltaTarjetaCredito("APROBADO", cuentaNumero, self.cupoDiarioRestante , monto,datetime.now,
            self.cantidad_transacciones() +1, self.saldoEnCuenta, self.cantTarjetasCredito(), self.cantChequeras() )
            nuevaTarjeta.resolver(self,monto)
        else:
            nuevaTarjeta = RazonAltaTarjetaCredito("RECHAZADO", cuentaNumero, self.cupoDiarioRestante , monto,datetime.now,
            self.cantidad_transacciones() +1, self.saldoEnCuenta, self.cantTarjetasCredito(), self.cantChequeras() )
    
        self.transacciones.append(nuevaTarjeta)

    def ALTA_CHEQUERA(self,monto,cuentaNumero):
        if (self.puede_crear_chequera()):
            altaChequera = RazonAltaChequera("APROBADO", cuentaNumero, self.cupoDiarioRestante , monto,datetime.now,
            self.cantidad_transacciones() +1, self.saldoEnCuenta, self.cantTarjetasCredito(), self.cantChequeras() )
            altaChequera.resolver(self,monto)
        else:
            altaChequera = RazonAltaTarjetaCredito("RECHAZADO", cuentaNumero, self.cupoDiarioRestante , monto,datetime.now,
            self.cantidad_transacciones() +1, self.saldoEnCuenta, self.cantTarjetasCredito(), self.cantChequeras() )
        self.transacciones.append(altaChequera)