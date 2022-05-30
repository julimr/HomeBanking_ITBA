let nombre = document.querySelector ('.inputNombre');
let gasto = document.querySelector ('.inputGasto')

let botonEnviar = document.querySelector ('.botoncito')
let gastoTotal = 0;
let contadorPersonas = 0;

let error = document.createElement ('span');
let sectionErrores = document.getElementById ('errores');
let calculos = document.querySelector ('.calculos');

botonEnviar.addEventListener ('click', function(){

    if (validarNombre (nombre.value)) {

        if (gasto.value < 0 || !(gasto.value > 0 )) {
            gasto.value = 0;
        }
        
        calculos.classList.remove ('invisible');
        calculos.classList.remove ('desvanecer');
        nombre.classList.remove ('incorrecto');
        error.classList.remove ('advertencia');
        sectionErrores.classList.add ('sacarAdvertencia');
        contadorPersonas ++;

        let valorNombre = nombre.value;
        let valorGasto = gasto.value;

        agregarPersona (valorNombre, valorGasto);

        gastoTotal += parseFloat (valorGasto);
        actualizarGastoTotal (gastoTotal);

        gastoIndividual (contadorPersonas, gastoTotal);

        nombre.value = '';
        gasto.value = '';
    }

    else {
        
        error.textContent = "Solo letras y espacios";
        sectionErrores.classList.remove ('sacarAdvertencia');
        sectionErrores.appendChild (error);
        error.classList.add ('advertencia');

        nombre.classList.add ('incorrecto');
    }

})

function agregarPersona (nombre, gasto) {
    
    let fila = document.createElement ('span');
    fila.setAttribute("id","persona");
    fila.textContent = `${nombre}: $${parseFloat(gasto).toFixed(2)}`;

    fila.addEventListener ("dblclick", function (event) {

        let gastoPersona = parseFloat(gasto).toFixed(2);

        gastoTotal -= gastoPersona;
        contadorPersonas-=1;
        actualizarGastoTotal (gastoTotal);
        
        if (gastoTotal == 0) {

            calculos.classList.add ('desvanecer');
            setTimeout (function () {

                calculos.classList.add ('invisible');
    
            }, 500) ;
        }
        else {
            calculos.classList.remove ('invisible');
            calculos.classList.remove ('desvanecer');
            gastoIndividual (contadorPersonas, gastoTotal);
        }

        fila.classList.add("desvanecer");
        setTimeout (function () {

            fila.remove();

        }, 500) ;

});


    var sectionPersonas = document.getElementById ('secPersonas');
    sectionPersonas.appendChild (fila);
    fila.classList.add ('formatoLinea');

}

function actualizarGastoTotal (gasto) {

    let gastado = document.getElementById ('gastado');
    gastado.textContent = `Total: $${parseFloat(gasto).toFixed(2)}`;

}

function gastoIndividual (personas, total) {
    let individual = document.getElementById ('individual');
    individual.textContent = `Cada uno debe pagar: $${(total/personas).toFixed(2)}`;
}

function validarNombre(nombre) {
    const permitido = new RegExp("^[a-zA-Z ]+$");
    return permitido.test(nombre);
  }
