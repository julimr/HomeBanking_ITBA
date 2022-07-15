export {setClientData}

function setClientData(data, i, name, number, dni, address) {
    name[i].textContent = `${data['nombre']}`;
    number[i].textContent = data['numero'];
    dni[i].textContent = data['dni'];
    address[i].textContent = `${data['direccion']['calle']} ${data['direccion']['numero']}, ${data['direccion']['ciudad']}
`
}