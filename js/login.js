const ingresar = document.querySelector ('.formulario__datos-final-boton');
const usuario = document.querySelector ('.formulario__datos-usuario');
const email = document.querySelector ('.formulario__datos-email');

const contraseña = document.querySelector ('#txtPassword');
const imgContraseña = document.getElementById ('imgContrasena');
const icono = document.querySelector ('.icon');
let oculto = true;

const usuario1 = {
    nombre : 'itbankgroup',
    email : 'itbank@gmail.com',
    contraseña : 'itbank123'
}

const mensajeError = document.getElementById ('mensaje_error');
let intentos = 3;

imgContraseña.addEventListener ('click', function(){
    if (oculto) {
        contraseña.setAttribute ('type', 'text');
        icono.setAttribute ('src', 'https://cdn3.iconfinder.com/data/icons/show-and-hide-password/100/show_hide_password-10-256.png');
        oculto = false;
    } else {
        contraseña.setAttribute ('type', 'password');
        icono.setAttribute ('src', 'https://cdn3.iconfinder.com/data/icons/show-and-hide-password/100/show_hide_password-09-256.png');
        oculto = true;
    }
})

ingresar.addEventListener ('click', function(){

    let usuarioIngresado = usuario.value;
    let emailIngresado = email.value;
    let contraseñaIngresada = contraseña.value;

    let validacion = comprobarDatos (usuarioIngresado, emailIngresado, contraseñaIngresada);
    let noVacio = comprobarVacio (usuarioIngresado, emailIngresado, contraseñaIngresada);

    if (noVacio) {

        if (validacion) {
            mensajeError.classList.toggle('con_error', 'sin_error');
            ingresar.classList.remove ('deshabilitar');
            window.location.href ='https://julimr.github.io/HomeBanking_ITBA/HomeBanking.html';
            
        } else {
            mensajeError.classList.toggle('con_error', 'sin_error');
            mensajeError.innerHTML = 'Los datos ingresados son incorrectos';
            intentos--;
            /*Evitar fuerza bruta*/
            if (intentos == 0) {
                mensajeError.innerHTML = 'Acceso bloqueado';
                ingresar.classList.add ('deshabilitar');
            }
        }

    } else {
        mensajeError.classList.toggle('con_error', 'sin_error');
        mensajeError.innerHTML = 'No puede haber campos vacios';
    }

    limpiarEntrada (usuario, email, contraseña);

});

function comprobarDatos (usuario, email, contraseña) {
    return ( (usuario == usuario1.nombre) && 
        (email == usuario1.email) && 
        (contraseña == usuario1.contraseña) );
}

function comprobarVacio (usuario, email, contraseña) {
    return ( (usuario != '') && 
        (email != '') && 
        (contraseña != '') );
}

function limpiarEntrada (usuario, email, contraseña) {
    usuario.value = '';
    email.value = '';
    contraseña.value = '';
}