import jsonData from "../data.json" assert { type: "json" }
import { generateItem } from "./generateItem.js";
import { generateFragment } from "./generateFragment.js";
import { setClientData } from "./clientData.js";

const list = document.querySelectorAll('.transactions__list');

const dataClassic = jsonData[0];
const dataGold = jsonData[1];
const dataBlack = jsonData[2];

const name = document.querySelectorAll('.name');
const number = document.querySelectorAll('.number');
const dni = document.querySelectorAll('.dni');
const address = document.querySelectorAll('.address');

setClientData(dataClassic, 0, name, number, dni, address);
setClientData(dataGold, 1, name, number, dni, address);
setClientData(dataBlack, 2, name, number, dni, address);

let lenClassic = dataClassic['transacciones'].length;
let lenGold = dataGold['transacciones'].length;
let lenBlack = dataBlack['transacciones'].length;

let classicFragment = document.createDocumentFragment();
let goldFragment = document.createDocumentFragment();
let blackFragment = document.createDocumentFragment();

list[0].appendChild(generateFragment(classicFragment, lenClassic, dataClassic));
list[1].appendChild(generateFragment(goldFragment, lenGold, dataGold));
list[2].appendChild(generateFragment(blackFragment, lenBlack, dataBlack));

