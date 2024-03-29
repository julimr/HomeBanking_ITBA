const list = document.getElementById("list-group")
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
            li.classList.add("list-group-item");
            
            list.appendChild(li);
            agregarTituloDolar(li,e)
            
            const container = document.createElement('div')
            container.className = "container"
            li.appendChild(container)
            const containerDivisa = document.createElement('div')
            containerDivisa.className = "containerDivisa"
            container.appendChild(containerDivisa)

            if (e.casa.nombre == "Dolar Contado con Liqui" ||
                e.casa.nombre == "Dolar Bolsa"
            ){
                agregarReferencia(containerDivisa,e)
            }else if(e.casa.nombre == "Dolar turista"){
                agregarVenta(containerDivisa,e)
            }else{
                agregarCompra(containerDivisa,e)
                agregarVenta(containerDivisa,e)
            }
            agregarVariacion(container,e)
            agregarActualizacion(container)
            }
        })    
    )
function agregarReferencia(container,data){
    const ref = document.createElement('div');
    ref.innerText = `REFERENCIA`;
    ref.className = "referencia";
    container.appendChild(ref);
    if (data.casa.compra > data.casa.venta){
        agregarDivisa(ref,data.casa.compra)
    } else {
        agregarDivisa(ref,data.casa.venta)
    }
    
}
function agregarTituloDolar(container, data){
    const containerTitulo = document.createElement('div');
    containerTitulo.className = "containerTitulo"
    const titulo = document.createElement('div');
    const img = document.createElement('img');
    img.src = "dolar.png";
    img.className= "imgDolar"
    titulo.innerText = `${data.casa.nombre}`;
    titulo.className = "titulo";
    containerTitulo.appendChild(img);
    containerTitulo.appendChild(titulo);
    container.appendChild(containerTitulo)
}
function agregarCompra(container, data){
    const divCompra = document.createElement('div');
    divCompra.innerText = `COMPRA`;
    divCompra.className = "tituloCompra";
    container.appendChild(divCompra);
    agregarDivisa(divCompra,data.casa.compra)
}
function agregarDivisa(container,data){
    const divisa = document.createElement('p');
    divisa.className = "divisa"
    divisa.innerText = `$ ${data}`;
    container.appendChild(divisa);
}
function agregarVenta(container, data){
    const divVenta = document.createElement('div');
    divVenta.innerText = `VENTA`;
    divVenta.className = "tituloVenta";
    container.appendChild(divVenta);
    agregarDivisa(divVenta,data.casa.venta)
}
function agregarVariacion(container,data){
    const variacion = document.createElement('div');
    const indicador = document.createElement ('span');

    const containerVariacion = document.createElement('div');
    containerVariacion.classList.add ('displayVariacion');

    if (data.casa.variacion == undefined){
        variacion.innerText = `VARIACIÓN: 0,00 %`;
        establecerIndicador(indicador,0,containerVariacion);
        containerVariacion.append (variacion);
    } else{
        variacion.innerText = `VARIACIÓN: ${data.casa.variacion} %`;
        let valorVariacion = data.casa.variacion.replace(',', '.');
        establecerIndicador(indicador,valorVariacion,containerVariacion);
        containerVariacion.append (variacion);
    }
    
    variacion.className = "variacion";
    container.appendChild(containerVariacion);
}
function establecerIndicador (indicador,valor,container){
    if (parseFloat(valor) < 0) {
        console.log ("V");
        indicador.classList.toggle('indicador-negativo','indicador');
    } else {
        console.log ("F");
        indicador.classList.toggle('indicador','indicador-negativo');
    }

    container.appendChild (indicador);
}
function agregarActualizacion(container){
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

    actualizacion.className = "actualizacion"
    container.appendChild(actualizacion);
}