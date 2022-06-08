function product(a, b) {
    return a * b;
}

obj = document.getElementById('DeJS')
txt = 'El resultado es ' + product(22, 33)
obj.innerHTML = txt

lista = ['Juan', 'Pedro', 'Emma']
diccio = { Juan: 10, Pedro: 20, Emma: 90 }

console.log('Lista números')
for (let i = 0; i < 20; i++) {
    console.log('20 veces ' + i + ' es ' + product(20, i));
}

console.log('Lista array')
for (const i in lista) {
    console.log(i)
}

console.log('Lista array')
for (const c in diccio) {
    console.log(c + ": " + diccio[c])
}