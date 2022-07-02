#Falta documentar
import csv
import pprint
from datetime import date
from datetime import datetime
import datetime
import time
import sys

def ingresarTipoSalida():
    salida = (input('▶ Ingrese la salida (PANTALLA o CSV): ')).lower()
    while (salida != "pantalla" and salida != "csv"):
        print('\n❌ Error en el tipo de salida, vuelva a ingresarlo ❌\n')
        salida = (input('▶ Ingrese la salida (PANTALLA o CSV): ')).lower()
    return salida


def ingresarTipoCheque():
    tipoCheque = (input('▶ Ingrese la salida (EMITIDO o DEPOSITADO): ')).lower()
    while tipoCheque != "emitido" and tipoCheque != "depositado":
        print('\n❌ Error en el tipo de cheque, vuelva a ingresarlo ❌\n')
        tipoCheque = (input('▶ Ingrese la salida EMITIDO o DEPOSITADO: ')).lower()
    return tipoCheque


def ingresarEstadoCheque():
    estadoCheque = (
        input('▶ Ingrese el estado del cheque (PENDIENTE, APROBADO, RECHAZADO o vacío para ver todos): ')).lower()
    while estadoCheque != "pendiente" and estadoCheque != "aprobado" and estadoCheque != "rechazado" and estadoCheque != "":
        print('\n❌ Error en el estado de cheque, vuelva a ingresarlo ❌\n')
        estadoCheque = (
            input('▶ Ingrese el estado del cheque (PENDIENTE, APROBADO, RECHAZADO o vacío para ver todos): ')).lower()
    return estadoCheque


def abrirArchivo(nombreArchivo):
    lineas = []
    try:
        with open(nombreArchivo) as csvfile:
            archivo = csv.DictReader(csvfile)
            for linea in archivo:
                lineas.append(linea)
        return lineas

    except FileNotFoundError:
        sys.exit('\n❌ El archivo al que intenta acceder no fue encontrado ❌')

def filtrarDatos(archivo, dniCliente, tipoCheque, estadoCheque, rango):
    filtradas = []
    cheques = []
    for linea in archivo:
        verificarNroCheque(linea, cheques)
    for linea in archivo:
        if (coincideDNI(linea, dniCliente) and
                coincideTipoCheque(linea, tipoCheque) and
                coincideEstadoCheque(linea, estadoCheque) and coincideRangoFecha(linea,rango)):
            if(cheques.count(linea['NroCheque']) > 1):
                sys.exit('\n❌ El número de cheque se encuentra repetido en otra cuenta ❌')
            estampaOrigen = int(linea['FechaOrigen'])
            estampaPago = int(linea['FechaPago'])
            stampToDate(linea,estampaOrigen,estampaPago)
            filtradas.append(linea)
    return filtradas

def verificarNroCheque(linea, cheques):
    cheques.append(linea['NroCheque'])
    return cheques

def stampToDate(linea, estampaOrigen, estampaPago):
    fechas = []

    fechaOrigen = datetime.datetime.fromtimestamp(estampaOrigen).strftime('%d-%m-%y')
    fechas.append(fechaOrigen)
    fechaPago = datetime.datetime.fromtimestamp(estampaPago).strftime('%d-%m-%y')
    fechas.append(fechaPago)

    linea['FechaOrigen'] = fechas[0]
    linea['FechaPago'] = fechas[1]

    return linea

def dateToStamp(fechas):

    if(fechas!=[]):

        fechaMinima = fechas[0]
        fechaMaxima = fechas[1]

        rangoEstampas = [
            time.mktime(datetime.datetime.strptime(fechaMinima,
                                                   "%d-%m-%Y").timetuple()),
            time.mktime(datetime.datetime.strptime(fechaMaxima,
                                                   "%d-%m-%Y").timetuple())
        ]
    else:
        rangoEstampas = [0,0]

    return rangoEstampas

def coincideRangoFecha(linea, fechas):
    rango = dateToStamp(fechas)
    return ( (int(linea['FechaOrigen']) >= rango[0] and int(linea['FechaOrigen']) <= rango[1]) or rango == [0,0] )

def coincideDNI(linea, dniCliente):
    return linea['DNI'] == dniCliente


def coincideTipoCheque(linea, tipoCheque):
    return linea['Tipo'].lower() == tipoCheque


def coincideEstadoCheque(linea, estadoCheque):
    return linea['Estado'].lower() == estadoCheque or estadoCheque == ""

def realizarSalida(lineasFiltradas, salida, dniCliente):
    if (salida == "pantalla"):
        print('\n---RESULTADOS OBTENIDOS---')
        print(f'\t☑ {len(lineasFiltradas)} coincidencias\n')
        pprint.pprint(lineasFiltradas)
    else:
        exportarCSV(dniCliente, lineasFiltradas)


def exportarCSV(dniCliente, lineasFiltradas):
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

    print('===SISTEMA PROCESAMIENTO BATCH DE CHEQUES===\n')

    nombreArchivo = input('▶ Ingrese el nombre del archivo csv: ')
    archivo_csv = abrirArchivo(nombreArchivo)

    dniCliente = input('▶ Ingrese el DNI del cliente: ')
    tipoSalida = ingresarTipoSalida()
    tipoCheque = ingresarTipoCheque()
    estadoCheque = ingresarEstadoCheque()

    filtrar = input('\n⏸¿Desea filtrar por rango de fecha (Si/No)?: ').lower()
    if(filtrar == 'si'):
        rangoFecha = [
            input('\n▶Ingrese la fecha mínima de emisión(dd-mm-yyyy): '),
            input('▶Ingrese la fecha máxima de emisión (dd-mm-yyyy): ')
        ]
    else:
        rangoFecha = []

    lineasFiltradas = filtrarDatos(archivo_csv, dniCliente, tipoCheque, estadoCheque, rangoFecha)

    realizarSalida(lineasFiltradas, tipoSalida, dniCliente)

ingresarDatos()
