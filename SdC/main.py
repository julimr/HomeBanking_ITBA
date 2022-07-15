from Black import Black
from Classic import Classic
from Gold import Gold
from convertirSalidaTPS import convertToDict
from content import content

import json

dataClassic = convertToDict('ejemplos_json/eventos_classic.json')
dataGold = convertToDict('ejemplos_json/eventos_gold.json')
dataBlack = convertToDict('ejemplos_json/eventos_black.json')

clienteClassic = Classic(dataClassic)
clienteGold = Gold(dataGold)
clienteBlack = Black(dataBlack)

transaccionesClassic = dataClassic['transacciones']
transaccionesGold = dataGold['transacciones']
transaccionesBlack = dataBlack['transacciones']

clienteClassic.clasificar_transacciones(transaccionesClassic)
clienteGold.clasificar_transacciones(transaccionesGold)
clienteBlack.clasificar_transacciones(transaccionesBlack)

reporteClassic = clienteClassic.reporte_cliente()
reporteGold = clienteGold.reporte_cliente()
reporteBlack = clienteBlack.reporte_cliente()

reporte = [reporteClassic, reporteGold, reporteBlack]

with open("data.json", "w") as f:
    json.dump(reporte, f, indent=4)

import webbrowser

file = open('index.html', 'w')
file.write(content)
file.close()

webbrowser.open_new_tab('index.html')