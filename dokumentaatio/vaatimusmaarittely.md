# Ohjelmistotekniika
## OTaTama
# Task manager


#käyttäjä
Käyttäjä voi luoda tunnuksen ja kirjautua käyttäjälleen

## sovelluksen tarkoitus
OTaTama on täydellinen ohjelmisto ihmiselle, jolla liikaa, mistä valita. Käyttäjä syöttää työtehtävänsä OTaTaman listalle prioriteettiarvoineen, jonka jälkeen OTaTama antaa käyttäjälle työtehtävän, jonka se toteutaa. Näin käyttäjä säästyy valinnanvaikeudelta. Loppukohteena tarkoitus olisi antaa käyttäjälle myös mahdollisuus saada viikkosuunnitelma tehtävistä, ja antaa käyttäjälle mahdollisuus vaikuttaa suunnitelmaan halutessaan. 

## suunnitellut toiminnallisuudet

# perusversion toiminnallisuus
## kirjautuessa
- käyttäjä voi luoda tunnuksen
   - käyttäjänimi on oltava uniikki ja vähintään 4 merkkiä
   - salasanan on oltava vähintään 4 merkkiä

- käyttäjä kirjautuu
   - jos käyttäjää ei ole olemassa, se ehdottaa sen luomista
   - jos salasana on väärin, siitä ilmoitetaan

## kirjauduttua
- käyttäjä lisää ja poistaa listalle työtehtävän
- käyttäjä näkee listan työtehtävistään
- käyttäjä voi kutsua itselleen seuraavan työtehtävän
   - listalta tulee randomilla työtehtävä
   - työtehtävän voi joko merkata tehdyksi, jolloin se katoaa listalta, tai sen voi hylätä, jolloin työtehtävä palaa listalle, eikä sama tehtävä voi olla heti seuraava valinta, ellei se ole ainoa listalla.
- käyttäjä voi kirjautua ulos 
# jatkokehitysideat
- käyttäjä voi asetaa työtehtäville prioriteettiarvoja, joiden perusteella niiden todennäköisyys valikoitua määrittyy
- työtehtäviä voi merkata osittain tehdyksi, jolloin ne palaavat listalle, mutta niissä on merkki puoliksi tehdyistä. Tällöin seuraava valinta ei voi olla äskeinen tehtävä.

