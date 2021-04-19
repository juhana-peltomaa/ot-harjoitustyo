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

- käyttäjä voi luoda järjestelmään tilin:
  * uniikin käyttäjätunnuksen ja salasanan tallentaminen tietokantaan [x] 
  * salasanan ja käyttäjätunnuksen minimivaatimukset [ ] 
    ** käyttäjätunnuksen tulee olla 5-15 merkkiä [ ]
    ** salasanan tulee olla vähintään 5 merkkiä [ ]

- käyttäjä voi kirjautua järjestelmään kirjautumislomakkeella, jos:
  * lomakkeelle syötetty käyttäjätunnus sekä salasana löytyvät tietokannasta [x]
  * jos kirjautuminen epäonnistuu, järjestelmä ilmoittaa tästä käyttäjälle [x]

### Kirjautumisen jälkeen

- käyttäjä näkee omat kurssinsa [x]

- käyttäjä voi luoda uuden kurssin, josta voi lisätä
  * nimi ja opintopistemäärä [x]
  * arvosana ja suoritusstatus [ ]

- käyttäjä voi muokata kurssin yllä mainittuja tietoja [ ]
  
- käyttäjä voi poistaa olemassa olevia kursseja [ ]

- käyttäjä voi kirjautua ulos järjestelmästä [x]

## Jatkokehitysideoita

Sovellusta voidaan täydennetään mm. seuraavilla toiminnallisuuksilla

- kurssinäkymän järjestäminen esim. suoritusstatuksen tai arvosanan perusteella
- tietojen lisäämisen yksittäisiin kursseihin esim. päiväys, osa-suorituksia, lisätietoa
- kurssien erittely opinto-kokonaisuukisen mukaan esim. pakolliset, vapaa-valintaiset
- käyttäjän poistaminen
