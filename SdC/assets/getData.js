//Exportamos todas las funciones del archivo
export {getDate, getType, getStatus, getAmount, getReason}

function getDate(data, i) {
    /**
    * Devuelve la fecha de la transacción
    * @param {object} //data
    * @param {number} //i
    * @return {string}
    */

    return data['transacciones'][i]['fecha'];
}

function getType(data, i) {
    /**
    * Devuelve el tipo de transacción
    * @param {object} //data
    * @param {number} //i
    * @return {string}
    */
    return data['transacciones'][i]['tipo'];
}

function getStatus(data, i) {
    /**
    * Devuelve el estado de la transacción
    * @param {object} //data
    * @param {number} //i
    * @return {string}
    */
    return data['transacciones'][i]['estado'];
}

function getAmount(data, i) {
    /**
    * Devuelve el monto la transacción
    * @param {object} //data
    * @param {number} //i
    * @return {string}
    */
    return data['transacciones'][i]['monto'];
}

function getReason(data, i) {
    /**
    * Devuelve el motivo de rechazo de la transacción
    * @param {object} //data
    * @param {number} //i
    * @return {string}
    */
    return data['transacciones'][i]['razonRechazo'];
}