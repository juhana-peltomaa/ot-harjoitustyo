# Course Tracker App

### Dokumentaatio

[Vaatimusmäärittely](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

### Asennus

1. Asenna riippuvuudet komennolla:

```python poetry install```

2. Alusta suoritusympäristö komennolla:

```python poetry run invoke build```

3. Käynnistä sovellus komennolla:

```python poetry sun invoke start```

### Komentorivitoiminnot

#### Ohjelman suorittaminen

Suorita ohjelma komennolla:

```python poetry run invoke start```

#### Testaus
Suorita testit komennolla:

```python poetry run invoke test```

#### Testikattavuus
Generoi testikattavuusraportti komennolla:

```python poetry run invoke coverage-report```

Generoitu raportti löytyy htmlcov-hakemistosta
