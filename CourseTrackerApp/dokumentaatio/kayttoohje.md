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

![LoginView](https://user-images.githubusercontent.com/55188494/117688190-d6285b80-b1b8-11eb-83c7-7510977b6066.png)

Sovellukseen voi kirjatua syöttämällä olemassaoleva käyttäjätunnus sekä salasana niille varattuihin syötekenttiin ja painamalla _"Login"_-painiketta

## Uuden käyttäjän luominen

Uuden käyttäjän luomisnäkymään voi siirtä kirjautumisnäkymästä painamalla _"Create User"_ -painiketta.

Tässä näkymässä voit luoda uuden käyttäjän syöttämällä käyttäjätunnuksen sekä salasanan niille varattuihin syötekenttiin ja painamalla _"Create"_-painiketta.

![Käyttäjän luomisnäkymä](https://user-images.githubusercontent.com/55188494/116752122-54407180-aa05-11eb-8cb0-3a71f438f9cf.png)

Jos käyttäjän luominen onnistuu saat ilmoituksen onnistuneesta tapahtumasta. Tämän jälkeen voit siirtyä takaisin kirjautumisnäkymään painamalla _"Back to Login"_-painiketta ja kirjatua sisään seuraamalla edellisen kohdan ohjeita.

![Onnistunut rekisteröinti](https://user-images.githubusercontent.com/55188494/116752193-74703080-aa05-11eb-8bf6-bb6a80ba3ba5.png)

Jos käyttäjätunnus on jo olemassa tai annetut syötteet eivät ole valideja saat virheilmoituksen.

![Olemassa oleva käyttäjä](https://user-images.githubusercontent.com/55188494/116752233-8baf1e00-aa05-11eb-831c-0cd724b6c16a.png)

## Kurssien hallinnointi

Kirjauduttuaan sovellukseen, käyttäjä näkee kaikki lisäämänsä kurssit. Tässä näkymässä käyttäjän voi lisätä uusia kursseja, muokata olemassa olevien kurssien tietoja sekä poistaa yksittäisiä tai kaikki kurssit. Käyttäjä näkee myös statistiikkaa kursseista, jotka on merkinnyt suoritetuiksi antamalla niiden statukseksi _"Completed"_.

![CoursesView](https://user-images.githubusercontent.com/55188494/117687973-a11c0900-b1b8-11eb-9ece-c02f03c5d978.png)

### Kurssin lisääminen

Uuden kurssin voi lisätä syöttämällä kurssin nimen, opintopiste määrän, arvosanan, suoritusstatuksen sekä kurssiin liittyvän URL-osoitteen niille varattuihin kenttiin. 

![Kurssin lisäys](https://user-images.githubusercontent.com/55188494/117688528-230c3200-b1b9-11eb-8b38-483f1dc7cadb.png)

Tämän jälkeen klikkaamalla _"Add new course"_ -painiketta, kurssi lisätään tietokantaan ja esitetään taulukossa:

![Päivitetty kurssinäkymä](https://user-images.githubusercontent.com/55188494/117688651-433bf100-b1b9-11eb-9f57-785703648517.png)

Huomioitahan, että kurssille on syötettävä minimissään nimi ja opintopiste määrä. Muutoin saat virhe-ilmoituksen:

![Puuttuvat opintopisteet](https://user-images.githubusercontent.com/55188494/116752760-522ae280-aa06-11eb-8c21-e4dbc0a0da0e.png)

### Kurssin tietojen muokkaaminen

Jo tallennettujen kurssien tietoja voi muokata valitsemalla kurssi taulukosta sitä klikkaamalla. Tällöin kurssin kaikki tiedot ovat latautuvat _Course information_ -syötekenttiin. Tämän jälkeen käyttäjä voi muuttaa haluamiaan kenttiä ja klikata _"Update course"_ -painiketta, jolloin kurssin tiedot päivittyvät taulukossa. 

![CourseUpdate](https://user-images.githubusercontent.com/55188494/117689354-f1e03180-b1b9-11eb-860b-736242ff0d77.gif)

Huom! Yllä päivitetty kurssi sai statukseksi _"Completed"_, jolloin samalla päivittyi _"Course Statistics for 'Completed' courses"_-kentän tiedot. Tämä kenttä huomioi ainoastaan kurssit, joiden status on _"Completed"_. Näistä kursseista ilmoitetaan niiden lukumäärä, opintopisteiden yhteismäärä sekä kurssien painotettu keskiarvo. 

Jos annat kurssille statuksen _"Completed"_, täytyy sinun antaa kurssille myös arvosana. Muutoin saat seuraavan virhe ilmoituksen:

![Completed_courses_need_Grade](https://user-images.githubusercontent.com/55188494/116788192-92db3800-aaa8-11eb-9cce-53bbb2369781.png)

### Yksittäisen kurssin poistaminen

Käyttäjä voi poistaa yksittäisen kurssin valitsemalla kurssin taulukosta sitä klikkaamalla ja tämän jälkeen painamalla _"Remove course"_ -painiketta: 

![Kurssin-poistaminen](https://user-images.githubusercontent.com/55188494/117690401-1b4d8d00-b1bb-11eb-9ac5-54198e35f499.gif)

Kurssin poistamisen yhteydessä myös kursseihin liittyvä statistiikka päivittyi. 

### Kaikkien kurssien poistaminen 

Käyttäjä voi myös poistaa kaikki tallentamansa kurssit painamalla _"Remove all course"_ -painiketta: 

![DeleteAllCourses](https://user-images.githubusercontent.com/55188494/117691113-d4ac6280-b1bb-11eb-80c1-5f8805cf01d3.gif)

### Käyttäjän poistaminen

Käyttäjä voi poistaa kaikki oman käyttäjänsä painamalla _"Delete User"_ -painiketta. Käyttäjä saa vielä ilmoituksen, jossa varmistetaan, että käyttäjä tietää poistamisen seuraamukset. Jos käyttäjä valitsee ilmoitusnäkymässä _"Yes"_, poistetaan käyttäjän kaikki tiedot ja käyttäjä kirjautuu ulos:


