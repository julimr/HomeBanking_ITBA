function logIn() {
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value

    if (username == 'itbankgroup' && password == 'itbank123') {
        // alert("Usuario y contraseñas validos");
        window.location.href ='https://julimr.github.io/HomeBanking_ITBA/HomeBanking.html';
        // document.location.assing('login-page.html'); este código nos permite hacerlo de forma local

    } else {
        alert('Usuario y/o contraseña incorrectos');
        console.log('Usuario y/o contraseña incorrectos');
        console.log(username + password);
    }
}