## Sovelluslogiikka


Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.


```mermaid
    classDiagram

        class Monopoly{lauta: Pelilauta
        noppa: Tuple[Noppa, Noppa]
        n = in range(2-8)
        pelaajat: Pelaaja*n} 

        Monopoly -- Pelilauta
        Pelilauta -- Ruudut
        Monopoly -- Noppa
        Pelilauta -- Pelinappula
        Monopoly -- Pelaaja
        Monopoly -- Pankki

        Monopoly --> Vankila: Monopoly tuntee sijainnin
        Monopoly --> Aloitusruutu: Monopoly tuntee sijainnin


        class Pelilauta{ruudut = [Ruudut]}

        class Ruudut

        class Pankki{id
        raha per pelaaja}
        
        Vankila --> Ruudut
        Aloitusruutu --> Ruudut
        Sattuma --> Ruudut
        Yhteismaa --> Ruudut
        Normaalit --> Ruudut
        Ruudut --> Paikka


        class Vankila{vieraile()
        jaa()}
        class Aloitusruutu{rahaatulee(200)}
        class Sattuma{sattumakortti}
        class Yhteismaa{yhteismaakortti}
        class Normaali{nimi: [kadunnimi]
        n: in range(1-4)
        talo: Talo*n
        omistaja: Player}
 
        class Noppa{silmäluku: int
        heitto()}

        class Pelaaja{id
        nappula: Pelinappula
        varat: int
        heita()
        siirto()
        maksa()
        }

        class Pelinappula{paikka: Paikka}
        Pelinappula --> Paikka

        class Talo{hinta: int}
        class Hotelli{hinta: int}
```
