class Cuenta:
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):

        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.costo_transferencias = costo_transferencias
        self.saldo_descubierto_disponible = saldo_descubierto_disponible

class CuentaAhorroEnPesos(Cuenta):
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible)

class CuentaAhorroEnDolares(Cuenta):
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible)

class CuentaCorriente(Cuenta):
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible)