function PartyAnimal() {
    this.x = 0;
    this.party = function() {
        this.x = this.x + 1;
        console.log('So far ' + this.x);
    }
}

an = new PartyAnimal();
ab = new PartyAnimal();
an.party();
an.party();
an.party();
ab.party();
ab.party();
an.x += 2
console.log("AN es " + an.x + " y AB es " + ab.x)

function PartyAnimal2(nam) {
    this.x = 0;
    this.nam = nam
    console.log('Built ' + nam)
    this.party = function() {
        this.x = this.x + 1;
        console.log(`${nam} = ${this.x}`);
    }
}

s = new PartyAnimal2('Artime')
s.party()
s.party()
t = new PartyAnimal2('josefina')
t.party()
s.party()