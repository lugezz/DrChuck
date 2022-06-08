/* Si hiciera como un switch */
function cambia() {
    let resp
    let obj = document.getElementById('stuff2')
    if (obj.innerHTML == 'Back') {
        resp = 'Forth'
    } else {
        resp = 'Back'
    }

    obj.innerHTML = resp
}

function elije(resp) {
    let obj = document.getElementById('stuff2')

    obj.innerHTML = resp
}