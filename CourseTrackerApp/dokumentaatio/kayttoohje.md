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

![Kirjautumisnäkymä](https://user-images.githubusercontent.com/55188494/116752036-3246ef00-aa05-11eb-8d85-e795f9fca38d.png)

Sovellukseen voi kirjatua syöttämällä olemassaoleva käyttäjätunnus sekä salasana niille varattuihin syötekenttiin ja painamalla "Login"-painiketta

## Uuden käyttäjän luominen

Uuden käyttäjän luomisnäkymään voi siirtä kirjautumisnäkymästä painamalla "Create User" -painiketta.

Tässä näkymässä voit luoda uuden käyttäjän syöttämällä käyttäjätunnuksen sekä salasanan niille varattuihin syötekenttiin ja painamalla "Create new user"-painiketta.

![Käyttäjän luomisnäkymä](https://user-images.githubusercontent.com/55188494/116752122-54407180-aa05-11eb-8cb0-3a71f438f9cf.png)

Jos käyttäjän luominen onnistuu saat ilmoituksen onnistuneesta tapahtumasta. Tämän jälkeen voit siirtyä takaisin kirjautumisnäkymään painamalla "Back to Login"-painiketta ja kirjatua sisään seuraamalla edellisen kohdan ohjeita.

![Onnistunut rekisteröinti](https://user-images.githubusercontent.com/55188494/116752193-74703080-aa05-11eb-8bf6-bb6a80ba3ba5.png)

Jos käyttäjätunnus on jo olemassa tai annetut syötteet eivät ole valideja saat virheilmoituksen.

![Olemassa oleva käyttäjä](https://user-images.githubusercontent.com/55188494/116752233-8baf1e00-aa05-11eb-831c-0cd724b6c16a.png)

## Kurssien hallinnointi

Kirjatuneelle käyttäjä näkee kaikki lisäämänsä kurssit. Näkymässä käyttäjän on myös mahdollista hallinnoida kurssejaan.

![Kurssinäkymä](https://user-images.githubusercontent.com/55188494/116752299-ad100a00-aa05-11eb-9e64-7ac43be0bce4.png)

### Kurssin lisääminen

Uuden kurssin voi lisätä antamalla kurssille nimen, opintopiste määrän, arvosanan, suoritusstatuksen sekä kurssiin liittyvän URL-osoitteen niille varattuihin kenttiin. 

![Kurssin lisäys](https://user-images.githubusercontent.com/55188494/116752583-15f78200-aa06-11eb-8483-a6f3ddde8b6e.png)

Tämän jälkeen klikkaamalla _"Add new course"_ -painiketta, kurssi lisätään tietokantaan ja esitetään taulukossa. 
![Päivitetty kurssinäkymä](https://user-images.githubusercontent.com/55188494/116752986-a8982100-aa06-11eb-86ce-bfa92d900ac3.png)

Huomioitahan, että kurssille on syötettävä minimissään nimi ja opintopiste määrä. Muutoin saat virhe-ilmoituksen:
![Puuttuvat opintopisteet](https://user-images.githubusercontent.com/55188494/116752760-522ae280-aa06-11eb-8c21-e4dbc0a0da0e.png)

### Kurssin tietojen muokkaaminen

Jo tallennettujen kurssien tietoja voi muokata valitsemalla kurssi taulukosta sitä klikkaamalla. Tällöin kurssin kaikki tiedot ovat esillä _Course information_ -syötekentissä. Tämän jälkeen voit muuttaa haluamiasi kenttiä ja klikata _"Update course"_ -painiketta, jolloin kurssin tiedot päivittyvät taulukossa. 

![Update_course_instruct](https://user-images.githubusercontent.com/55188494/116754420-fe6dc880-aa08-11eb-887a-8df45c9e6bd1.gif)

Koska päivitetty kurssi sai statukseksi _"Completed"_ päivittyi samalla _"Course Statistics for 'Completed' course"_-kentässä olevat tiedot. Tämä kenttä ilmoittaa suoritettujen kurssien lukumäärän, suoritettujen opintopisteiden määrän sekä suoritettujen kurssien painotetun keskiarvon. 

### Kurssin poistaminen

TBA

