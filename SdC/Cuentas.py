class Cuentas:
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, monto, costo_transferencias, saldo_descubierto_disponible):

        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.monto = monto
        self.costo_transferencias = costo_transferencias
        self.saldo_descubierto_disponible = saldo_descubierto_disponible

    def definirCuentas(self, cajaAhorroPesos, cajaAhorroDolares, cuentaCorrientePesos):
        self.cajaAhorroPesos = cajaAhorroPesos
        self.cajaAhorroDolares = cajaAhorroDolares
        self.cuentaCorrientePesos = cuentaCorrientePesos