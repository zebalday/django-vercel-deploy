// RANDOM USER INFO FETCH
function fetchRandomUser() {
    var imagen = document.getElementById("imagen");
    var nombre = document.getElementById("nombre");
    var pais = document.getElementById("pais");
    var mail = document.getElementById("email");

    $.ajax({
        url: 'https://randomuser.me/api/',
        dataType: 'json',
        success: function(data) {
          console.log(data.results[0]);
          imagen.src = data.results[0].picture.medium;
          nombre.innerHTML = data.results[0].name.first + data.results[0].name.last;
          pais.innerHTML = data.results[0].location.country;
          mail.innerHTML = data.results[0].email;
        }
    });
}

// CHUCK NORRIS INFO FETCH
function fetchChuckFact() {
    var icon = document.getElementById("icon");
    var fact = document.getElementById("fact");

    $.ajax({
        url: 'https://api.chucknorris.io/jokes/random',
        dataType: 'json',
        success: function(data) {
          console.log(data);
          icon.src = data.icon_url;
          fact.innerHTML = data.value;
        }
    });
}


