#Importación de módulos
from convertirSalidaTPS import convertToDict
from Classic import Classic
from Gold import Gold
from Black import Black
from content import content

#Nos permite trabajar con archivos JSON
import json

#Nos permite visualizar documentos en la web (no es usado por lo explicado al final)
import webbrowser

#Convertimos a diccionario los datos correspondientes a cada cliente
dataClassic = convertToDict('ejemplos_json/eventos_classic.json')
dataGold = convertToDict('ejemplos_json/eventos_gold.json')
dataBlack = convertToDict('ejemplos_json/eventos_black.json')

#Creamos tres clientes, uno de cada uno. Le asignamos los datos anteriores
clienteClassic = Classic(dataClassic)
clienteGold = Gold(dataGold)
clienteBlack = Black(dataBlack)

#Para cada uno, obtenemos sus transacciones
transaccionesClassic = dataClassic['transacciones']
transaccionesGold = dataGold['transacciones']
transaccionesBlack = dataBlack['transacciones']

#Clasificamos las transacciones
clienteClassic.clasificar_transacciones(transaccionesClassic)
clienteGold.clasificar_transacciones(transaccionesGold)
clienteBlack.clasificar_transacciones(transaccionesBlack)

#Generamos el reporte de cada cliente
reporteClassic = clienteClassic.reporte_cliente()
reporteGold = clienteGold.reporte_cliente()
reporteBlack = clienteBlack.reporte_cliente()

#El reporte final será una lista con el reporte de cada cliente
reporte = [reporteClassic, reporteGold, reporteBlack]

#Convertimos el reporte a un archivo del tipo JSON para trabajarlo con JS
with open("data.json", "w") as f:
    #indent=4 es para darle un formato más legible 
    json.dump(reporte, f, indent=4)

#Abrimos el archivo index.html (o lo creamos) en modo escritura
file = open('index.html', 'w')
#Escribimos el contenido del template HTML en el
file.write(content)
#Cerramos el archivo
file.close()

# webbrowser.open_new_tab('index.html')

'''
La linea de arriba abre una nueva pestaña que no va a funcionar, porque al usar JS se necesita un servidor.
Entonces, hay que abrir el archivo index que genera con live server.
'''