class Cuentas:
    """
    Establece los límites y valores que aplican a las cuentas
    """
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):

        self.limite_extraccion_diario = limite_extraccion_diario
        self.limite_transferencia_recibida = limite_transferencia_recibida
        self.costo_transferencias = costo_transferencias
        self.saldo_descubierto_disponible = saldo_descubierto_disponible

class CuentaAhorroEnPesos(Cuentas):
    #Hereda de la clase Cuentas
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible)

class CuentaAhorroEnDolares(Cuentas):
    #Hereda de la clase Cuentas
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible)

class CuentaCorriente(Cuentas):
    #Hereda de la clase Cuentas
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        super().__init__(limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible)