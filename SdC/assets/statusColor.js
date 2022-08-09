//Exportamos el procedimiento colorStatus
export {colorStatus}

let colorStatus = ()=>{
    //Seleccionamos todos los estados
    let transactionStatus = document.querySelectorAll('#status');
    //Por cada uno, comprobamos el estado y asignamos un color
    transactionStatus.forEach(element => {
        if (element.innerHTML=="ACEPTADA"){
            element.classList.add('accepted');
        } else {
            element.classList.add('rejected');
        }
    });
}