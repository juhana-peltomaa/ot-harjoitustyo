# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus mahdollistaa käyttäjän kirjata tietoja käymistään yliopistokursseista ja siten seurata omaa kurssitilannetaan. Käyttäjän on mahdollista kirjata sovellukseen
kurssin nimi, opintopisteet, arvosanan sekä suoritusstatuksen. Sovellukseen on mahdollista rekisteröidä oma käyttäjä, jolloin jokaisen käyttäjä näkee uniikin tilanteensa. Käyttäjä voi myös halutessaan poistaa kaikki tietonsa sovelluksesta. 

## Käyttäjät

Sovelluksella on ainoastaan yksi käyttäjärooli ns. _normaali käyttäjä_.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- käyttäjä voi luoda järjestelmään tilin:
  - [x] uniikin käyttäjätunnuksen ja salasanan tallentaminen tietokantaan 
  - [x] käyttäjätunnuksen tulee olla vähintään 4 merkkiä
  - [x] salasanan tulee olla vähintään 4 merkkiä

- käyttäjä voi kirjautua järjestelmään kirjautumislomakkeella, jos:
  - [x] lomakkeelle syötetty käyttäjätunnus sekä salasana löytyvät tietokannasta 
  - [x] jos kirjautuminen epäonnistuu, järjestelmä ilmoittaa tästä käyttäjälle 

### Kirjautumisen jälkeen

- [x] kirjautunut käyttäjä näkee ainoastaan omat kurssinsa 

- kirjautunut käyttäjä näkee statistiikkaa suoritetuista kursseista (eli kursseista, joiden status == _Completed_):
  - [x] suoritettujen kurssien määrän
  - [x] suoritettujen opintopisteiden määrän
  - [x] suoritettujen kurssien painotetun keskiarvon 

- kirjautunut voi luoda uuden kurssin lisäämällä:
  - [x] nimen ja opintopistemäärän (minimivaatimus uuden kurssin lisäämiselle)
  - [x] arvosanan ja suoritusstatuksen 
  - [x] kurssiin liittyvän URL-osoitteen 

- [x] käyttäjä voi muokata kurssin yllä mainittuja tietoja 

- [x] käyttäjä voi avata selaimessa lisäämänsä URL-osoitteet tuplaklikkaamalla niitä taulukosta
  
- [x] käyttäjä voi poistaa olemassa olevia kursseja 

- [x] käyttäjä voi kirjautua ulos järjestelmästä 

- [x] käyttäjä voi poistaa kaikki tietonsa (käyttäjän poistaminen)

## Jatkokehitysideoita

Sovellusta voidaan täydennetään mm. seuraavilla toiminnallisuuksilla

- kurssinäkymän järjestäminen esim. suoritusstatuksen tai arvosanan perusteella
- tietojen lisäämisen yksittäisiin kursseihin esim. päiväys, osa-suorituksia, lisätietoa
- kurssien erittely opinto-kokonaisuukisen mukaan esim. pakolliset, vapaa-valintaiset
