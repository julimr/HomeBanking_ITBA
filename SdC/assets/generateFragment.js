//Importamos la función para generar el li
import { generateItem } from "./generateItem.js";
//Exportamos la función generateFragment
export {generateFragment}

function generateFragment(fragment, length, data) {
    /**
    * Devuelve un fragmento con cada item de la lista de transacciones
    * @param {DocumentFragment} //fragment
    * @param {number} //length
    * @param {object} //data
    * @return {DocumentFragment} //fragment
    */

    for (let i=0; i<length; i++){
        fragment.appendChild(generateItem(data, i));
    }

    return fragment
    
}
