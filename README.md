# Course Tracker App

Sovelluksen nykyinen versio mahdollistaa käyttäjän luoda uusi käyttäjä ja kirjautua sovellukseen. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Siirry hakemistoon CourseTrackerApp komennolla:

```cd CourseTrackerApp```

2. Asenna riippuvuudet komennolla:

```poetry install```

3. Käynnistä sovellus komennolla:

```poetry run invoke start```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Suorita ohjelma komennolla:

```poetry run invoke start```

### Testaus
Suorita testit komennolla:

```poetry run invoke test```

### Testikattavuus
Generoi testikattavuusraportti komennolla:

```poetry run invoke coverage-report```

Generoitu raportti löytyy _htmlcov_-hakemistosta
