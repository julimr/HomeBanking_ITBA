import { getDate, getType, getStatus, getAmount, getReason } from "./getData.js";
import { generateItem } from "./generateItem.js";

export {generateFragment}

function generateFragment(fragment, length, data) {

    for (let i=0; i<length; i++){
        fragment.appendChild(generateItem(data, i));
    }

    return fragment
    
}
