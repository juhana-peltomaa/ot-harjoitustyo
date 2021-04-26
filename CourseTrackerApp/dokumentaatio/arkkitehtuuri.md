# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen arkkitehtuurirakenne on kolmitasoinen ja se koostuu seuraavanlaisesta pakkausrakenteesta:

![Viikko4-pakkauskaavio](https://user-images.githubusercontent.com/55188494/115162660-122e3c00-a0a5-11eb-908c-f1968a0871e6.png)

Käyttöliittymä sisältyy pakkaukseen _ui_, sovelluslogiikka on eritelty pakkaukseen _services_ ja vastaavasti käytettyjen tietokohteiden pysyväisyystallennus pakkaukseen _repositories_. Sovelluksen käyttämät tietokohteet ovat pakkauksessa _entities_. 


## Sovelluslogiikka

Sovelluksen tietokohteet koostuvat kahdesta luokasta: _User_ ja _Course_. Nämä luokat sisältävät koodin sovelluksen käyttämistä käyttäjä sekä kurssi -olioista. 

![Viikko 4-pakkauskaavio-6](https://user-images.githubusercontent.com/55188494/115162423-badb9c00-a0a3-11eb-923e-c39171d18a86.png)

Sovelluksen toiminnallisuudet on tallennettu luokkaan _CourseServices_, jonka avulla eri käyttöliittymä näkymien toiminnallisuuksia toteutetaan. Luokan _CourseServices_ käyttää toteutuksessa hyväksi pääsyä tiedon pysyväistallennuksesta vastaaviin luokkiin _UserRepo_ ja _CourseRepo_. 


## Päätoiminnallisuudet

Alla kuvatuu sovelluksen olleellisia toimintalogiikan osia sekvenssikaavioiden avulla.

### Sisäänkirjatuminen sovellukseen

Sovelluksen käynnistäminen asettaa _LoginView_-näkymän käyttäjälle. Käyttäjän painaessa _"Login"_ -painiketta, täytettyään ensin näkymän syötekenttiin käyttäjätunnuksen ja salasanan, sovellusksen toiminnallisuus etenee seuraavasti:

![Käyttäjän kirjautuminen](https://user-images.githubusercontent.com/55188494/116088508-3809a100-a6a2-11eb-8bdc-18a19c7de7b1.png)

_"Login"_ -painike hakee syötekenttien sisällön ja käyttää niitä parametreinä kutsuessaan sovelluslogiikan _CourseServices_ metodia _login_user_. Sovelluslogiikka tarkistaa onko asetettu käyttäjätunnus olemassa kutsumalla _find_user_ -metodia _UserRepo_ -luokasta. 

Jos käyttäjä on olemassa, palauttaa metodi käyttäjän tiedot, jonka jälkeen sovelluslogiikka tarkistaa vastaavatko ne paramentreinä annettuja salasanaa ja käyttäjätunnusta. Jos täsmää, metodi asettaa käyttäjän nykykäyttäjäksi ja kutsuu _show_courses_view_-metodia, jolloin näkymäksi asetetaan _CourseView_-näkymä. 

### Uuden kurssin lisääminen sovellukseen

Kirjauduttua sisään, käyttäjä voi luoda uuden kurssin näkymäänsä painamalla _"Add new Course"_ -painiketta, jolloin sovelluksen toiminnallisuus etenee seuraavasti:

![Uuden kurssin lisääminen](https://user-images.githubusercontent.com/55188494/116094913-393dcc80-a6a8-11eb-94bd-3256acc272ac.png)

Kurssia luotaessa käyttäjä voi syöttää parametreinä kurssin nimen, opintopistemäärän, arvosanana ja suoritusstatuksen niille osotetuissa kentissä. Minimissään käyttäjän tulee syöttää kurssin nimi sekä opintopistemäärän, jotka annettuaan sekä painiketta _"Add new Course"_ painettuaan kutsutaan _CourseServices_ metodia _create_new_course_. 

Vastaavasti _CourseServices_ tarkistaa, onko käyttäjä jo tallentanut kyseisen kurssin käyttäen hyväksi metodia _find_course_, joka sijaitsee _CourseRepo_ -luokassa. Ennen metodin suorittamista, _CourseServices_ tarkistaa sen hetkisen käyttäjän ja antaa sen parametrinä _find_course_ -metodille yhdessä kurssin nimen kanssa. 

Jos kurssia ei löydy, palauttaa metodi arvon _None_, jonka jälkeen tarkistetaan syötettyjen opintopistemäärän ja arvosanan oikeellisuus kutsumalla _validate_credit_ ja _validate_grade_ -metodeja. 

Tarkistuksien läpäistyä, _CourseService_ luo _Course_ -olion annetuilla parametreillä ja tallentaa sen _CourseRepo_:oon metodilla _create_course_. Kurssien luomisen ja tallentamisen onnistuessa _CourseView_ kutsuu metodia _display_all_courses_, joka hakee kaikki käyttäjän kurssit kutsumalla _CourseService_:in metodin _display_all_courses_ kautta _CourseRepo_:n _find_all_courses()_ -metodia. Tällöin käyttäjän näkymässä on nähtävillä myös juuri luotu uusi kurssi. 
