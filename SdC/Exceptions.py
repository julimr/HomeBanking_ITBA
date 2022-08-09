"""
En este archivo, guardamos las clases utilizadas como excepciones.
Cada uno permitira ejecutar un mensaje, depediendo del tipo de error.
Todas heredan de la clase Exception.
"""

class NoPuedePorClienteClassic(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoPuedeCrearExcedeElLimite(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoPuedeRetirarExcedeMontoMaximo(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoPuedeRetirarExcedeDineroDisponible(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoPuedeRealizarTransferenciaNoHayDineroDisponible(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoPuedeRecibirTransferenciaPorqueExcedeMontoMaximo(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoPuedeComprarDolaresExcedeMontoMaximo(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class NoPuedeComprarDolaresExcedeDineroDisponible(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje