const list = document.getElementById("list-groupDolar")
fetch("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    .then((data) => data.json())
    .then((data) =>
        data.forEach((e) => {
            //console.log(e);
            if (e.casa.nombre != "Dolar Soja" &&
                e.casa.nombre != "Bitcoin" &&
                e.casa.nombre != "Argentina"
            ){
            const li = document.createElement("li");
            li.classList.add("list-group-itemDolar");
            
            list.appendChild(li);
            agregarTituloDolar(li,e)
            
            const containerDolar = document.createElement('div')
            containerDolar.className = "containerDolar"
            li.appendChild(containerDolar)
            const containerDolarDivisa = document.createElement('div')
            containerDolarDivisa.className = "containerDolarDivisa "
            containerDolar.appendChild(containerDolarDivisa)

            if (e.casa.nombre == "Dolar Contado con Liqui" ||
                e.casa.nombre == "Dolar Bolsa"
            ){
                agregarReferencia(containerDolarDivisa,e)
            }else if(e.casa.nombre == "Dolar turista"){
                agregarVenta(containerDolarDivisa,e)
            }else{
                agregarCompra(containerDolarDivisa,e)
                agregarVenta(containerDolarDivisa,e)
            }
            agregarVariacion(containerDolar,e)
            agregarActualizacion(containerDolar)
            }
        })    
    )
function agregarReferencia(containerDolar,data){
    const ref = document.createElement('div');
    ref.innerText = `REFERENCIA`;
    ref.className = "referencia";
    containerDolar.appendChild(ref);
    if (data.casa.compra > data.casa.venta){
        agregarDivisa(ref,data.casa.compra)
    } else {
        agregarDivisa(ref,data.casa.venta)
    }
    
}
function agregarTituloDolar(containerDolar, data){
    const containerDolarTitulo = document.createElement('div');
    containerDolarTitulo.className = "containerDolarTitulo borderDolarUp"
    const titulo = document.createElement('div');
    const img = document.createElement('img');
    img.src = "/Images/dolar.png";
    img.className= "imgDolar"
    titulo.innerText = `${data.casa.nombre}`;
    titulo.className = "titulo";
    containerDolarTitulo.appendChild(img);
    containerDolarTitulo.appendChild(titulo);
    containerDolar.appendChild(containerDolarTitulo)
}
function agregarCompra(containerDolar, data){
    const divCompra = document.createElement('div');
    divCompra.innerText = `COMPRA`;
    divCompra.className = "tituloCompra";
    containerDolar.appendChild(divCompra);
    agregarDivisa(divCompra,data.casa.compra)
}
function agregarDivisa(containerDolar,data){
    const divisa = document.createElement('p');
    divisa.className = "divisa"
    divisa.innerText = `$ ${data}`;
    containerDolar.appendChild(divisa);
}
function agregarVenta(containerDolar, data){
    const divVenta = document.createElement('div');
    divVenta.innerText = `VENTA`;
    divVenta.className = "tituloVenta";
    containerDolar.appendChild(divVenta);
    agregarDivisa(divVenta,data.casa.venta)
}
function agregarVariacion(containerDolar,data){
    const variacion = document.createElement('div');
    const indicador = document.createElement ('span');

    const containerDolarVariacion = document.createElement('div');
    containerDolarVariacion.classList.add ('displayVariacion');

    if (data.casa.variacion == undefined){
        variacion.innerText = `VARIACIÓN: 0,00 %`;
        establecerIndicador(indicador,0,containerDolarVariacion);
        containerDolarVariacion.append (variacion);
    } else{
        variacion.innerText = `VARIACIÓN: ${data.casa.variacion} %`;
        let valorVariacion = data.casa.variacion.replace(',', '.');
        establecerIndicador(indicador,valorVariacion,containerDolarVariacion);
        containerDolarVariacion.append (variacion);
    }
    
    variacion.className = "variacion";
    containerDolar.appendChild(containerDolarVariacion);
}
function establecerIndicador (indicador,valor,containerDolar){
    if (parseFloat(valor) < 0) {
        console.log ("V");
        indicador.classList.toggle('indicador-negativo','indicador');
    } else {
        console.log ("F");
        indicador.classList.toggle('indicador','indicador-negativo');
    }

    containerDolar.appendChild (indicador);
}
function agregarActualizacion(containerDolar){
    let fecha = new Date().toLocaleDateString();
    let hora = new Date().getHours();
    let minutos = new Date().getMinutes();

    const actualizacion = document.createElement('div');

    if (minutos < 10) {
        actualizacion.innerText = `ACTUALIZADO: ${fecha} ${hora}:0${minutos}`;
    }
    else {
        actualizacion.innerText = `ACTUALIZADO: ${fecha} ${hora}:${minutos}`;
    }

    actualizacion.className = "actualizacion borderDolarDown"
    containerDolar.appendChild(actualizacion);
}
