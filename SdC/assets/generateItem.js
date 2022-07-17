//Importamos las funciones usadas para setear la data del cliente
import { getDate, getType, getStatus, getAmount, getReason } from "./getData.js";
//Exportamos la función generateItem
export {generateItem}

function generateItem(data, i) {
    /**
    * Devuelve un item de lista con la información del cliente
    * @param {object} //data
    * @param {int} //i
    * @return {Element} //li
    */
    //Creamos un li y le agregamos la clase transaction para darle formato
    let li = document.createElement('li');
    li.classList.add('transaction');

    //Template con el contenido del HTML
    li.innerHTML = 
    `
        <p class="data-item tr-item"><span id="changeFormat">Fecha:</span>${getDate(data, i)}</p>
        <p class="data-item tr-item"><span id="changeFormat">Tipo:</span>${getType(data, i)}</p>
        <p class="data-item tr-item"><span id="changeFormat">Estado:</span><span id="status">${getStatus(data, i)}</span></p>
        <p class="data-item tr-item"><span id="changeFormat">Monto:</span>${getAmount(data, i)}</p>
        <p class="data-item tr-item"><span id="changeFormat">Razón:</span>${getReason(data, i)}</p>   
    `
    return li;
}