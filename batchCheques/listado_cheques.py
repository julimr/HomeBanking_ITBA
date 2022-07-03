#Permite trabajar con datos tabulares en formato CSV
import csv
#Permite «imprimir de forma bonita» estructuras de datos
import pprint
#Permiten trabajar con marcas de tiempo y fecha
from datetime import date
from datetime import datetime
import datetime
import time

#Permite manipular ciertas funciones del entorno de ejecución
import sys

def ingresarTipoSalida():
    """
    Description
    -----------
    Permite al usuario elegir el tipo de salida para visualizar los datos

    Returns
    -------
    salida :type string
        Devuelve un string con lo ingresado
    """

    salida = (input('-> Ingrese la salida (PANTALLA o CSV): ')).lower()

    #Solicitamos hasta que se ingrese una opción válida
    while (salida != "pantalla" and salida != "csv"):
        print('\n|X| Error en el tipo de salida, vuelva a ingresarlo |X|\n')
        salida = (input('-> Ingrese la salida (PANTALLA o CSV): ')).lower()
    return salida


def ingresarTipoCheque():

    """
    Description
    -----------
    Permite al usuario ingresar el tipo de cheque

    Returns
    -------
    tipoCheque :type string
        Devuelve un string con lo ingresado
    """

    tipoCheque = (input('-> Ingrese la salida (EMITIDO o DEPOSITADO): ')).lower()

    #Solicitamos hasta que se ingrese una opción válida
    while tipoCheque != "emitido" and tipoCheque != "depositado":
        print('\n|X| Error en el tipo de cheque, vuelva a ingresarlo |X|\n')
        tipoCheque = (input('-> Ingrese la salida EMITIDO o DEPOSITADO: ')).lower()
    return tipoCheque


def ingresarEstadoCheque():

    """
    Description
    -----------
    Permite al usuario ingresar el estado del cheque

    Returns
    -------
    estadoCheque :type string
        Devuelve un string con lo ingresado
    """

    estadoCheque = (
        input('-> Ingrese el estado del cheque (PENDIENTE, APROBADO, RECHAZADO o vacío para ver todos): ')).lower()

    #Solicitamos hasta que se ingrese una opción válida
    while estadoCheque != "pendiente" and estadoCheque != "aprobado" and estadoCheque != "rechazado" and estadoCheque != "":
        print('\n|X| Error en el estado de cheque, vuelva a ingresarlo |X|\n')
        estadoCheque = (
            input('-> Ingrese el estado del cheque (PENDIENTE, APROBADO, RECHAZADO o vacío para ver todos): ')).lower()
    return estadoCheque

def filtrarPorFecha():
    filtrar = input('\n⏸¿Desea filtrar por rango de fecha (Si/No)?: ').lower()
    if(filtrar == 'si'):
        rangoFecha = [
            input('\n->Ingrese la fecha mínima de emisión(dd-mm-yyyy): '),
            input('->Ingrese la fecha máxima de emisión (dd-mm-yyyy): ')
        ]
    else:
        rangoFecha = []

    return rangoFecha

def abrirArchivo(nombreArchivo):
    """
    Description
    -----------
    Abre el archivo solicitado

    Parameters
    ----------
    parametro_1 :type string
        Nombre del archivo ingresado por el usuario

    Returns
    -------
    lineas :type list
        Devuelve una lista con los datos del archivo
    """

    lineas = []
    #Intentamos abrir el archivo con ese nombre
    try:
        with open(nombreArchivo) as csvfile:
            archivo = csv.DictReader(csvfile)
            for linea in archivo:
                lineas.append(linea)
        return lineas

    #Si no se puede, notificamos el error
    except FileNotFoundError:
        sys.exit('\n|X| El archivo al que intenta acceder no fue encontrado |X|')

def filtrarDatos(archivo, dniCliente, tipoCheque, estadoCheque, rango):

    """
    Description
    -----------
    Filtra los datos segun ciertos criterios

    Parameters
    ----------
    parametro_1 :type list
        Lista con los datos del archivo
    parametro_2 :type string
        String con numero de DNI
    parametro_3 :type string
        String con tipo de cheque
    parametro_4 :type string
        String con estado del cheque
    parametro_5 :type list
        Lista con los rangos de fecha

    Returns
    -------
    filtradas :type list
        Datos que coinciden con los filtros aplicados
    """

    filtradas = []
    cheques = []
    for linea in archivo:
        #Guardamos todos los numeros de cheques
        obtenerNroCheque(linea, cheques)
    for linea in archivo:
        #Preguntamos si esa linea de datos coincide con todos los filtros
        if (coincideDNI(linea, dniCliente) and
                coincideTipoCheque(linea, tipoCheque) and
                coincideEstadoCheque(linea, estadoCheque) and coincideRangoFecha(linea,rango)):
             #Si se encontró dos veces un numero de cheque en distintas cuentas, notificamos el error   
            if(cheques.count(linea['NroCheque']) > 1):
                sys.exit('\n|X| El número de cheque se encuentra repetido en otra cuenta |X|')
            estampaOrigen = int(linea['FechaOrigen'])
            estampaPago = int(linea['FechaPago'])
            stampToDate(linea,estampaOrigen,estampaPago)
            #Guardamos los datos coincidentes
            filtradas.append(linea)

    return filtradas

def obtenerNroCheque(linea, cheques):
    """
    Description
    -----------
    Guarda los numeros de cheques de todas las cuentas

    Parameters
    ----------
    parametro_1 :type dict
        Linea de datos del archivo
    parametro_2 :type list
        Lista donde se guardaran los números de cheques

    Returns
    -------
    cheques :type list
        Números de cheques
    """

    cheques.append(linea['NroCheque'])
    return cheques

def stampToDate(linea, estampaOrigen, estampaPago):
    """
    Description
    -----------
    Permite convertir una estampa temporal a fecha

    Parameters
    ----------
    parametro_1 :type dict
        Linea de datos del archivo
    parametro_2 :type int
        Estampa de fecha de origen
    parametro_3 :type int
        Estampa de fecha de pago

    Returns
    -------
    linea :type dict
        Devuelve los datos originales, pero con las fechas convertidas a date
    """
    fechas = []

    fechaOrigen = datetime.datetime.fromtimestamp(estampaOrigen).strftime('%d-%m-%y')
    fechas.append(fechaOrigen)
    fechaPago = datetime.datetime.fromtimestamp(estampaPago).strftime('%d-%m-%y')
    fechas.append(fechaPago)

    #Convertimos las estampas a date y las formateamos
    linea['FechaOrigen'] = fechas[0]
    linea['FechaPago'] = fechas[1]

    return linea

def dateToStamp(fechas):
    """
    Description
    -----------
    Permite convertir una fecha a estampa temporal

    Parameters
    ----------
    parametro_1 :type list
        Lista con las fechas a convertir

    Returns
    -------
    rangoEstampas :type list
        Devuelve una lista con las estampas temporales
    """

    # Convertimos a estampa temporal si la lista contiene algo

    if(fechas!=[]):

        fechaMinima = fechas[0]
        fechaMaxima = fechas[1]

        rangoEstampas = [
            time.mktime(datetime.datetime.strptime(fechaMinima,
                                                   "%d-%m-%Y").timetuple()),
            time.mktime(datetime.datetime.strptime(fechaMaxima,
                                                   "%d-%m-%Y").timetuple())
        ]

     # Si no, colocamos dos ceros indicando que no se ha decidido filtrar por fecha   
    else:
        rangoEstampas = [0,0]

    return rangoEstampas

def coincideRangoFecha(linea, fechas):

    """
    Description
    -----------
    Determina si las fechas se encuentran en el rango solicitado

    Parameters
    ----------
    parametro_1 :type dict
        Linea de datos del archivo
    parametro_2 :type list
        Lista con los rangos de fecha

    Returns
    -------
    :type bool
        Devuelve True si la fecha se encuentra en el rango especificado
    """

    rango = dateToStamp(fechas)

    #Si se encuentra en el rango o si no se filtra por fecha
    return ( (int(linea['FechaOrigen']) >= rango[0] and int(linea['FechaOrigen']) <= rango[1]) or rango == [0,0] )

def coincideDNI(linea, dniCliente):
    """
    Description
    -----------
    Determina si el DNI coincide

    Parameters
    ----------
    parametro_1 :type dict
        Linea de datos del archivo
    parametro_2 :type string
        Dni del cliente

    Returns
    -------
    :type bool
        Devuelve True si el DNI coincide
    """
    
    return linea['DNI'] == dniCliente


def coincideTipoCheque(linea, tipoCheque):

    """
    Description
    -----------
    Determina si el tipo de cheque coincide

    Parameters
    ----------
    parametro_1 :type dict
        Linea de datos del archivo
    parametro_2 :type string
        Tipo de cheque

    Returns
    -------
    :type bool
        Devuelve True si el tipo de cheque coincide
    """
    return linea['Tipo'].lower() == tipoCheque


def coincideEstadoCheque(linea, estadoCheque):

    """
    Description
    -----------
    Determina si el estado del cheque coincide

    Parameters
    ----------
    parametro_1 :type dict
        Linea de datos del archivo
    parametro_2 :type string
        Estado del cheque

    Returns
    -------
    :type bool
        Devuelve True si el estado del cheque coincide o es vacío para ver todos
    """

    return linea['Estado'].lower() == estadoCheque or estadoCheque == ""

def realizarSalida(lineasFiltradas, salida, dniCliente):
    """
    Description
    -----------
    Permite realizar la salida en funcion de lo seleccionado

    Parameters
    ----------
    parametro_1 :type list
        Lista con los datos coincidentes
    parametro_2 :type string
        Tipo de salida elegido por el usuario
    parametro_3 :type string
        DNI del cliente buscado

    Result
    -------
    :type string
        Muestra los resultados obtenidos en consola o en un nuevo archivo
    """
    if (salida == "pantalla"):
        print('\n---RESULTADOS OBTENIDOS---')
        print(f'\t☑ {len(lineasFiltradas)} coincidencias\n')
        pprint.pprint(lineasFiltradas)
    else:
        exportarCSV(dniCliente, lineasFiltradas)


def exportarCSV(dniCliente, lineasFiltradas):
    """
    Description
    -----------
    Permite exportar los datos en un nuevo archivo CSV

    Parameters
    ----------
    parametro_1 :type string
        DNI del cliente
    parametro_2 :type list
        Lista con los datos filtrados

    Result
    -------
    :type file
        Crea un nuevo archivo CSV
    """

    nombreArchivo = f"{dniCliente}_{date.today()}.csv"
    with open(nombreArchivo, 'w', newline='') as csvfile:
        fielnames = ["FechaOrigen", "FechaPago", "Valor", "NumeroCuentaOrigen"]
        writer = csv.DictWriter(csvfile, fieldnames=fielnames)
        writer.writeheader()
        for linea in lineasFiltradas:
            writer.writerow({'FechaOrigen': linea['FechaOrigen'],
                             'FechaPago': linea['FechaPago'],
                             'Valor': linea['Valor'],
                             'NumeroCuentaOrigen': linea['NumeroCuentaOrigen']})
        print("Archivo Creado con éxito!")

def ingresarDatos():

    """
    Description
    -----------
    Permite al usuario ingresar todos los datos

    Parameters
    ----------

    Result
    -------
    :type string
        Muestra las solicitudes de datos en consola
    """

    print('===SISTEMA PROCESAMIENTO BATCH DE CHEQUES===\n')

    nombreArchivo = input('-> Ingrese el nombre del archivo csv: ')
    archivo_csv = abrirArchivo(nombreArchivo)

    dniCliente = input('-> Ingrese el DNI del cliente: ')
    tipoSalida = ingresarTipoSalida()
    tipoCheque = ingresarTipoCheque()
    estadoCheque = ingresarEstadoCheque()

    rangoFecha = filtrarPorFecha()

    lineasFiltradas = filtrarDatos(archivo_csv, dniCliente, tipoCheque, estadoCheque, rangoFecha)

    realizarSalida(lineasFiltradas, tipoSalida, dniCliente)

ingresarDatos()
