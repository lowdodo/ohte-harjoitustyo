## Sovelluslogiikka


Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.


```mermaid
    classDiagram

        class Monopoly{lauta: Pelilauta
        noppa: Tuple[Noppa, Noppa]} 

        Monopoly -- Pelilauta
        Pelilauta -- Ruudut
        Monopoly -- Noppa
        Pelilauta -- Pelinappula
        Monopoly -- Pelaaja
        Monopoly -- Pankki


        class Pelilauta{ruudut = [Ruudut]}

        class Ruudut

        class Pankki{id}
        
        Vankila --> Ruudut
        Aloitusruutu --> Ruudut
        Sattuma --> Ruudut
        Yhteismaa --> Ruudut
        Normaalit --> Ruudut
        class Vankila{vieraile()
        jaa()}
        class Aloitusruutu{rahaatulee(200)}
        class Sattuma{sattumakortti}
        class Yhteismaa{yhteismaakortti}
        class Normaalit{kadunnimet}

        class Noppa{silmäluku: int
        heitto()}

        class Pelaaja{id
        maara: int}

        class Pelinappula

        class Talo{hinta: int}
        class Hotelli{hinta: int}
```
