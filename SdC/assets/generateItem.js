import { getDate, getType, getStatus, getAmount, getReason } from "./getData.js";
export {generateItem}

function generateItem(data, i) {
    let li = document.createElement('li');
    li.classList.add('transaction');
    li.innerHTML = 
    `
        <p class="data-item tr-item"><span id="changeFormat">Fecha:</span>${getDate(data, i)}</p>
        <p class="data-item tr-item"><span id="changeFormat">Tipo:</span>${getType(data, i)}</p>
        <p class="data-item tr-item"><span id="changeFormat">Estado:</span>${getStatus(data, i)}</p>
        <p class="data-item tr-item"><span id="changeFormat">Monto:</span>${getAmount(data, i)}</p>
        <p class="data-item tr-item"><span id="changeFormat">Razón:</span>${getReason(data, i)}</p>   
    `
    return li;
}