# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus mahdollistaa käyttäjän kirjata tietoja käymistään yliopistokursseista ja siten seurata omaa kurssitilannetaan. Käyttäjän on mahdollista kirjata sovellukseen
kurssin nimi, opintopisteet, arvosanan sekä suoritusstatuksen. Sovellukseen on mahdollista rekisteröidä oma käyttäjä, jolloin jokaisen käyttäjä näkee uniikin tilanteensa.

## Käyttäjät

Sovelluksella on ainoastaan yksi käyttäjärooli ns. _normaali käyttäjä_.

## Käyttöliittymäluonnos

_TBA_

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- käyttäjä voi luoda järjestelmään tilin, jolle asetetaan
  - käyttäjätunnus: täytyy olla uniikki, pituudeltaan vähintään 3 ja enintään 10 merkkiä
  - salasana: täytyy olla 5-15 merkkiä 

- käyttäjä voi kirjautua järjestelmään kirjautumislomakkeella, jos:
  - lomakkeelle syötetty käyttäjätunnus sekä salasana löytyvät tietokannasta
  - jos kirjautuminen epäonnistuu, järjestelmä ilmoittaa tästä käyttäjälle

### Kirjautumisen jälkeen

- käyttäjä näkee omat kurssinsa

- käyttäjä voi luoda uuden kurssin:
  - kurssista lisätään nimi, opintopistemäärä, arvosana ja suoritusstatus

- käyttäjä voi muokata kurssin yllä mainittuja tietoja
  
- käyttäjä voi poistaa olemassa olevia kursseja

- käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Sovellusta voidaan täydennetään mm. seuraavilla toiminnallisuuksilla

- kurssinäkymän järjestäminen esim. suoritusstatuksen tai arvosanan perusteella
- tietojen lisäämisen yksittäisiin kursseihin esim. päiväys, osa-suorituksia, lisätietoa
- kurssien erittely opinto-kokonaisuukisen mukaan esim. pakolliset, vapaa-valintaiset
- käyttäjän poistaminen
