counter = 1;
lista = document.getElementById('lista');

$(document).ready(function() {
    $('#the-href').on('click', function() {
        console.log('Clicked');
        $('#lista').append('<li class="list-item">Este es el item ' + counter + '</li>');
        counter++
    });
    $('#limpia').on('click', function() {
        console.log('A limpiaaaar....');
        counter = 1
        $('.list-item').remove()
    });
});