class Direccion:
    """
    Sirve para organizar los datos de la dirección de cada Cliente
    """
    #Constructor de clase
    def __init__(self, calle, numero, ciudad, provincia, pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais