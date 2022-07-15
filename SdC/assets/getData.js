export {getDate, getType, getStatus, getAmount, getReason}

function getDate(data, i) {
    return data['transacciones'][i]['fecha'];
}

function getType(data, i) {
    return data['transacciones'][i]['tipo'];
}

function getStatus(data, i) {
    return data['transacciones'][i]['estado'];
}

function getAmount(data, i) {
    return data['transacciones'][i]['monto'];
}

function getReason(data, i) {
    return data['transacciones'][i]['razonRechazo'];
}