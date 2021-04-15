# Course Tracker App

Sovelluksen nykyinen versio mahdollistaa käyttäjän luoda uusi käyttäjä ja kirjautua sovellukseen. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Siirry hakemistoon CourseTrackerApp komennolla:

```cd CourseTrackerApp```

2. Asenna riippuvuudet komennolla:

```poetry install``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry install```

3. Käynnistä sovellus komennolla:

```poetry run invoke start``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke start```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Suorita ohjelma komennolla:

```poetry run invoke start``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke start```

### Testaus
Suorita testit komennolla:

```poetry run invoke test``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke test```

### Testikattavuus
Generoi testikattavuusraportti komennolla:

```poetry run invoke coverage-report``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke coverage-report```

Generoitu raportti löytyy _htmlcov_-hakemistosta
