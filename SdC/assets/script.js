//Importación para trabajar con archivos JSON
import jsonData from "../data.json" assert { type: "json" }
//Importación para generar fragmentos con las transacciones (una lista)
import { generateFragment } from "./generateFragment.js";
//Importación para setear los datos del cliente
import { setClientData } from "./clientData.js";
//Importación para poder colocar un color a cada estado de la operación
import { colorStatus } from "./statusColor.js";

//Buscamos las listas en el HTML
const list = document.querySelectorAll('.transactions__list');

//A cada cliente, le corresponden objetos diferentes de la lista de datos
const dataClassic = jsonData[0];
const dataGold = jsonData[1];
const dataBlack = jsonData[2];

//Buscamos los campos para luego colocarles los datos correspondiente
const name = document.querySelectorAll('.name');
const number = document.querySelectorAll('.number');
const dni = document.querySelectorAll('.dni');
const address = document.querySelectorAll('.address');

//Llamamos a la función setClientData y pasamos los datos
setClientData(dataClassic, 0, name, number, dni, address);
setClientData(dataGold, 1, name, number, dni, address);
setClientData(dataBlack, 2, name, number, dni, address);

//Obtenemos cuantas transacciones realizó cada cliente
let lenClassic = dataClassic['transacciones'].length;
let lenGold = dataGold['transacciones'].length;
let lenBlack = dataBlack['transacciones'].length;

//Generamos tres fragmentos de código donde se insertarán las transacciones
let classicFragment = document.createDocumentFragment();
let goldFragment = document.createDocumentFragment();
let blackFragment = document.createDocumentFragment();

//A cada lista le agregamos su contenido correspondiente
list[0].appendChild(generateFragment(classicFragment, lenClassic, dataClassic));
list[1].appendChild(generateFragment(goldFragment, lenGold, dataGold));
list[2].appendChild(generateFragment(blackFragment, lenBlack, dataBlack));

//Establecemos el color del estado de cada operación
colorStatus();