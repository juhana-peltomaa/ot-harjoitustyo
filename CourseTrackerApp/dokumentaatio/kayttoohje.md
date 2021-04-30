## Ohjelman käynnistäminen

1. Siirry hakemistoon CourseTrackerApp komennolla:

```cd CourseTrackerApp```

2. Ennen sovelluksen käynnistystä, asenna riippuvuudet komennolla:

```poetry install``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry install```

3. Tämän jälkeen suorita tietokannan alustaminen komennolla:

```poetry run invoke build``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke build```

4. Käynnistä sovellus komennolla:

```poetry run invoke start``` tai vaihtoehtoisesti, jos edellinen ei toimi kokeile: ```python3 -m poetry run invoke start```

## Kirjautuminen

Kun sovellus käynnistetään, avautuu kirjautumisnäkymä:

[Insert picture LoginView]

Sovellukseen voi kirjatua syöttämällä olemassaoleva käyttäjätunnus sekä salasana niille varattuihin syötekenttiin ja painamalla "Login"-painiketta

## Uuden käyttäjän luominen

Uuden käyttäjän luomisnäkymään voi siirtä kirjautumisnäkymästä painamalla "Create user" -painiketta.

Tässä näkymässä voit luoda uuden käyttäjän syöttämällä käyttäjätunnuksen sekä salasanan niille varattuihin syötekenttiin ja painamalla "Create new user"-painiketta.

[Insert picture CreateUserView]

Jos käyttäjän luominen onnistuu saat ilmoituksen onnistuneesta tapahtumasta. Tämän jälkeen voit siirtyä takaisin kirjautumisnäkymään painamalla "Back to Login"-painiketta ja kirjatua sisään seuraamalla edellisen kohdan ohjeita.

[Insert success message]

Jos käyttäjätunnus on jo olemassa tai annetut syötteet eivät ole valideja saat virheilmoituksen.

[Insert fail message]

## Kurssien lisääminen ja hallinnointi

Kirjatuneelle käyttäjä näkee kaikki lisäämänsä kurssit. Näkymässä käyttäjän on myös mahdollista hallinnoida kurssejaan.

[Insert CourseView]

