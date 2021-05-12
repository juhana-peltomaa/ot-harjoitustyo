# Course Tracker App

Sovelluksen käyttäjän on mahdollista luoda uusi käyttäjä ja kirjautua sovellukseen. Kirjautunut käyttäjä voi hallinnoida kurssejaan muun muassa lisäämällä uusia tai muokkaamalla olemassa olevia kursseja. Sovellus näyttää käyttäjälle myös statistiikkaa suoritetusta kursseista kuten kurssien lukumäärän, opintopisteiden yhteismäärän sekä painotetun keskiarvon. 

Käyttäjän on myös mahdollista poistaa yksittäisiä tai kaikki tallentamansa kurssit. 

Sovellusta voi käyttää useampi käyttäjä, jolloin he näkevät ainoastaan omat kurssinsa. Käyttäjä voi myös halutessaan poistaa kaikki tietonsa sovelluksesta.

# Huomio Python-versiosta

Sovellus on testattu Python-versiolla ```3.6.0```. Erityisesti, jos käytössä on vanhempi versio voi sovelluksen käytössä esiintyä ongelmia. 

## Releases
[Loppupalautus](https://github.com/juhana-peltomaa/ot-harjoitustyo/releases/tag/viikko7)

[Viikko 6 release](https://github.com/juhana-peltomaa/ot-harjoitustyo/releases/tag/viikko6)

[Viikko 5 release](https://github.com/juhana-peltomaa/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

[Käyttöohje](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/dokumentaatio/testaus.md)

## Asennus

1. Siirry hakemistoon CourseTrackerApp komennolla:

```cd CourseTrackerApp```

2. Asenna riippuvuudet komennolla:

```poetry install``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry install```

3. Alusta tietokanta sovelluksen käyttöä varten:

```poetry run invoke build``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke build```

4. Käynnistä sovellus komennolla:

```poetry run invoke start``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke start```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Alusta tietokanta sovelluksen käyttöä varten:

```poetry run invoke build``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke build```

Suorita ohjelma komennolla:

```poetry run invoke start``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke start```

### Testaus
Suorita testit komennolla:

```poetry run invoke test``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke test```

### Testikattavuus
Generoi testikattavuusraportti komennolla:

```poetry run invoke coverage-report``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke coverage-report```

Generoitu raportti löytyy _htmlcov_-hakemistosta.

### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:
```poetry run invoke lint``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke lint```
