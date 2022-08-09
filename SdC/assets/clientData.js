//Exportamos la función setClientData
export {setClientData}

function setClientData(data, i, name, number, dni, address) {
    /**
    * Seteamos los datos personales de cada cliente
    * @param {object} //data
    * @param {number} //i
    * @param {NodeListOf} //name
    * @param {NodeListOf} //number
    * @param {NodeListOf} //dni
    * @param {NodeListOf} //address
    */
    name[i].textContent = `${data['nombre']}`;
    number[i].textContent = data['numero'];
    dni[i].textContent = data['dni'];
    address[i].textContent = `${data['direccion']['calle']} ${data['direccion']['numero']}, ${data['direccion']['ciudad']}
`
}