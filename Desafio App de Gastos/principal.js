let nombre = document.querySelector ('.inputNombre');
let gasto = document.querySelector ('.inputGasto')
let individual = document.getElementById ('individual');

let botonEnviar = document.querySelector ('.botoncito')
let gastoTotal = 0;
let contadorPersonas = 0;

let error = document.createElement ('span');
let error2 = document.createElement ('span');
let sectionErrores = document.getElementById ('errores');
let calculos = document.querySelector ('.calculos');

botonEnviar.addEventListener ('click', function(){

    if (validarNombre (nombre.value)) {

        //Negativo o no numérico
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
        
        if (nombre.value==""){

            error.textContent = "";
            error2.textContent = "El nombre no puede estar vacío";
            sectionErrores.classList.remove ('sacarAdvertencia');
            sectionErrores.appendChild (error2);
            error2.classList.add ('advertencia');
            
        }

        else {
            error2.textContent="";
            error.textContent = "Solo letras y espacios";
            sectionErrores.classList.remove ('sacarAdvertencia');
            sectionErrores.appendChild (error);
            error.classList.add ('advertencia');
        }
        
        nombre.classList.add ('incorrecto');
    }

})

function agregarPersona (nombre, gasto) {
    
    let image = document.createElement('img')
    image.className = 'icon-delete'
    image.src  = './delete-red.png'

    let fila = document.createElement ('span');
    fila.setAttribute("id","persona");
    fila.textContent = `${nombre}: $${parseFloat(gasto)}`;
    fila.appendChild(image);
    

    image.addEventListener ("click", function (event) {

        let gastoPersona = parseFloat(gasto).toFixed(2);
        image.remove();
        gastoTotal -= gastoPersona;
        contadorPersonas-=1;
        actualizarGastoTotal (gastoTotal);
        
        if (gastoTotal == 0) {

            individual.textContent = `Cada uno debe pagar: $0.00`;
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

    individual.textContent = `Cada uno debe pagar: $${(total/personas).toFixed(2)}`;

}

function validarNombre(nombre) {
    const permitido = new RegExp("^[a-zA-Z ]+$");
    return permitido.test(nombre);
  }
