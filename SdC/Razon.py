
class Razon:
    def __init__(self,estado,tipo,cuentaNumero,
    CupoDiarioRestante,monto,fecha, numero,saldoEnCuenta,
    totalTarjetasDeCreditoActualmente,totalChequerasActualmente):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.CupoDiarioRestante = CupoDiarioRestante
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.saldoEnCuenta = saldoEnCuenta
        self.totalTarjetasDeCreditoActualmente = totalTarjetasDeCreditoActualmente
        self.totalChequerasActualmente = totalChequerasActualmente

    
    def resolver(self,cliente,monto):
         pass

class RazonAltaChequera(Razon):
    def __init__(self, estado, cuentaNumero, CupoDiarioRestante, monto,
    fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        super().__init__(estado, cuentaNumero, CupoDiarioRestante, monto, fecha, numero,
        saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente)
        self.tipo = "ALTA_CHEQUERA"
    
    def resolver(self, cliente, monto):
        cliente.nueva_chequera()
    
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, estado, cuentaNumero, CupoDiarioRestante, monto,
    fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        super().__init__(estado, cuentaNumero, CupoDiarioRestante, monto, fecha, numero,
        saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente)
        self.tipo = "ALTA_TARJETA_CREDITO"
    
    def resolver(self, cliente, monto):
        cliente.cantTarjetasCredito += 1

class RazonCompraDolar(Razon):
    def __init__(self, estado, cuentaNumero, CupoDiarioRestante, monto,
    fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        super().__init__(estado, cuentaNumero, CupoDiarioRestante, monto, fecha, numero,
        saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente)
        self.tipo = "COMPRAR_DOLAR"

class RazonRetiroEfectivo(Razon):
    def __init__(self, estado, cuentaNumero, CupoDiarioRestante, monto,
    fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        super().__init__(estado, cuentaNumero, CupoDiarioRestante, monto, fecha, numero,
        saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente)
        self.tipo = "RETIRO_EFECTIVO_CAJERO_AUTOMATICO"
    
    def resolver(self, cliente, monto):
        cliente.retirar_efectivo(monto)
        
class RazonTransferenciaEnviada(Razon):
    def __init__(self, estado, cuentaNumero, CupoDiarioRestante, monto,
    fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        super().__init__(estado, cuentaNumero, CupoDiarioRestante, monto, fecha, numero,
        saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente)
        self.tipo = "TRANSFERENCIA_ENVIADA"

class RazonTransferenciaRecibida(Razon):
    def __init__(self, estado, cuentaNumero, CupoDiarioRestante, monto,
    fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        super().__init__(estado, cuentaNumero, CupoDiarioRestante, monto, fecha, numero,
        saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente)
        self.tipo = "TRANSFERENCIA_RECIBIDA"