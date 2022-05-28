let nombre = document.querySelector ('.inputNombre');
let gasto = document.querySelector ('.inputGasto')

let botonEnviar = document.querySelector ('.botoncito')
let gastoTotal = 0;
let contadorPersonas = 0;

botonEnviar.addEventListener ('click', function(){

    contadorPersonas ++;

    let valorNombre = nombre.value;
    let valorGasto = gasto.value;

    agregarPersona (valorNombre, valorGasto);

    gastoTotal += parseFloat (valorGasto);
    actualizarGastoTotal (gastoTotal);

    gastoIndividual (contadorPersonas, gastoTotal);

    nombre.value = '';
    gasto.value = '';

    console.log (gastoTotal);

})

function agregarPersona (nombre, gasto) {
    
    let fila = document.createElement ('span');
    fila.textContent = `${nombre}: $${gasto}`;
    var sectionPersonas = document.getElementById ('secPersonas');
    sectionPersonas.appendChild (fila);
    fila.classList.add ('formatoLinea');

}

function actualizarGastoTotal (gasto) {

    let gastado = document.getElementById ('gastado');
    gastado.textContent = `Total: $${gasto}`;

}

function gastoIndividual (personas, total) {
    let individual = document.getElementById ('individual');
    individual.textContent = `Cada uno debe pagar: $${(total/personas).toFixed(2)}`;
}