#Importamos para poder trabajar con funciones de JSON
import json

def convertToDict(file):
    """
    Convierte a diccionario de Python un archivo del tipo JSON
    @param file -> json file
    return data -> dict
    """

    with open(file) as json_file:
        #Abrimos el archivo y lo convertimos a diccionario 
        data = json.load(json_file) 
    #Devolvemos dicho diccionario
    return data
