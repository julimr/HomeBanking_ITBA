import csv
import pprint
from datetime import date

def ingresarTipoSalida():
    salida = (input("Ingrese la salida PANTALLA o CSV: ")).lower()
    while (salida !="pantalla" and salida != "csv"):
        print("Error en el tipo de salida, vuelva a ingresar")
        salida = (input("Ingrese la salida PANTALLA o CSV: ")).lower()
    return salida

def ingresarTipoCheque():
    tipoCheque = (input("Ingrese la salida EMITIDO o DEPOSITADO : ")).lower()
    while tipoCheque != "emitido" and tipoCheque != "depositado":
        print("Error en el tipo de cheque, vuelva a ingresar")
        tipoCheque = (input("Ingrese la salida EMITIDO o DEPOSITADO : ")).lower()
    return tipoCheque

def ingresarEstadoCheque():
    estadoCheque = (input("Ingrese el estado del cheque (PENDIENTE, APROBADO, RECHAZADO o vacío para ver todos): ")).lower()
    while estadoCheque != "pendiente" and estadoCheque != "aprobado" and estadoCheque != "rechazado" and estadoCheque != "":
        print("Error en el tipo de cheque, vuelva a ingresar")
        estadoCheque = (input("Ingrese el estado del cheque (PENDIENTE, APROBADO, RECHAZADO o vacío para ver todos): ")).lower()
    return estadoCheque

def abrirArchivo(nombreArchivo):
    lineas = []
    with open(nombreArchivo) as csvfile:
        archivo = csv.DictReader(csvfile)
        for linea in archivo:
            lineas.append(linea)
    return lineas
            
def filtrarDatos(archivo, dniCliente, tipoCheque, estadoCheque):
    filtradas = []
    for linea in archivo:
        if( coincideDNI(linea,dniCliente) and
            coincideTipoCheque(linea,tipoCheque) and
            coincideEstadoCheque(linea,estadoCheque)):
            filtradas.append(linea)
    return filtradas

def coincideDNI(linea,dniCliente):
    return linea['DNI'] == dniCliente

def coincideTipoCheque(linea,tipoCheque):
    return linea['Tipo'].lower() == tipoCheque

def coincideEstadoCheque(linea, estadoCheque):
    return linea['Estado'].lower() == estadoCheque or estadoCheque == ""

def realizarSalida(lineasFiltradas,salida,dniCliente):
    if(salida == "pantalla"):
        pprint.pprint(lineasFiltradas)
    else: 
        exportarCSV(dniCliente, lineasFiltradas)

def exportarCSV(dniCliente, lineasFiltradas):
    nombreArchivo= f"{dniCliente}_{date.today()}.csv"
    with open(nombreArchivo,'w', newline='') as csvfile:
        fielnames=["FechaOrigen","FechaPago","Valor","NumeroCuentaOrigen"]
        writer = csv.DictWriter(csvfile, fieldnames=fielnames)
        writer.writeheader()
        for linea in lineasFiltradas:
            writer.writerow({'FechaOrigen': linea['FechaOrigen'],
                             'FechaPago': linea['FechaPago'],
                             'Valor': linea['Valor'],
                             'NumeroCuentaOrigen': linea['NumeroCuentaOrigen']})
        print("Archivo Creado con éxito!")



nombreArchivo = input("Ingrese el nombre del archivo csv: ")
archivo_csv = abrirArchivo(nombreArchivo)

dniCliente = input("Ingrese el DNI del cliente: ")
tipoSalida = ingresarTipoSalida()
tipoCheque = ingresarTipoCheque()
estadoCheque = ingresarEstadoCheque()

lineasFiltradas = filtrarDatos(archivo_csv,dniCliente,tipoCheque,estadoCheque)

realizarSalida(lineasFiltradas,tipoSalida,dniCliente)
 


# FALTA:
# 2.f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)

# 3- Si para un DNI dado un número de cheque de una misma cuenta se repite se
# debe mostrar el error por pantalla, indicando que ese es el problema.
