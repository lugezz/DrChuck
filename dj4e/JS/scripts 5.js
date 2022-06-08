counter = 1;
lista = document.getElementById('lista');

function add() {
    let x = document.createElement('li');
    x.className = "list-item";
    x.innerHTML = "Este es el item " + counter;
    lista.appendChild(x);
    counter++;
}

function limpiar() {
    counter = 1;
    listas = document.querySelectorAll('.list-item');
    listas.forEach(li => {
        li.remove();
    });
}