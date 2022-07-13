class Razon:
    def __init__(self, type):
        self.type = type
    
    def resolver(self,cliente,evento):
         pass

class RazonAltaChequera(Razon):
    def __init__(self, type):
        super().__init__(type)
    
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, type):
        super().__init__(type)

class RazonCompraDolar(Razon):
    def __init__(self, type):
        super().__init__(type)

class RazonRetiroEfectivo(Razon):
    def __init__(self, type):
        super().__init__(type)

class RazonTransferenciaEnviada(Razon):
    def __init__(self, type):
        super().__init__(type)

class RazonTransferenciaRecibida(Razon):
    def __init__(self, type):
        super().__init__(type)