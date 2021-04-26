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
  - [x] uniikin käyttäjätunnuksen ja salasanan tallentaminen tietokantaan 
  - [ ] käyttäjätunnuksen tulee olla 5-15 merkkiä
  - [ ] salasanan tulee olla vähintään 5 merkkiä 

- käyttäjä voi kirjautua järjestelmään kirjautumislomakkeella, jos:
  - [x] lomakkeelle syötetty käyttäjätunnus sekä salasana löytyvät tietokannasta 
  - [x] jos kirjautuminen epäonnistuu, järjestelmä ilmoittaa tästä käyttäjälle 

### Kirjautumisen jälkeen

- [x] kirjautunut käyttäjä näkee ainoastaan omat kurssinsa 

- kirjautunut voi luoda uuden kurssin lisäämällä:
  - [x] nimen ja opintopistemäärän 
  - [x] arvosanan ja suoritusstatuksen 

- [x] käyttäjä voi muokata kurssin yllä mainittuja tietoja 
  
- [x] käyttäjä voi poistaa olemassa olevia kursseja 

- [x] käyttäjä voi kirjautua ulos järjestelmästä 

## Jatkokehitysideoita

Sovellusta voidaan täydennetään mm. seuraavilla toiminnallisuuksilla

- kurssinäkymän järjestäminen esim. suoritusstatuksen tai arvosanan perusteella
- tietojen lisäämisen yksittäisiin kursseihin esim. päiväys, osa-suorituksia, lisätietoa
- kurssien erittely opinto-kokonaisuukisen mukaan esim. pakolliset, vapaa-valintaiset
- käyttäjän poistaminen
