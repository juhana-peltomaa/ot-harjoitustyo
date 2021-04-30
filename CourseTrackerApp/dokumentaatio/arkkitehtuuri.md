# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen arkkitehtuurirakenne on kolmitasoinen ja se koostuu seuraavanlaisesta pakkausrakenteesta:

![Viikko4-pakkauskaavio](https://user-images.githubusercontent.com/55188494/115162660-122e3c00-a0a5-11eb-908c-f1968a0871e6.png)

Käyttöliittymä sisältyy pakkaukseen _ui_, sovelluslogiikka on eritelty pakkaukseen _services_ ja vastaavasti käytettyjen tietokohteiden pysyväisyystallennus pakkaukseen _repositories_. Sovelluksen käyttämät tietokohteet ovat pakkauksessa _entities_. 

## Käyttöliittymä

Käyttöliittymässä on kolme eri näkymää:
 - Kirjautumisnäkymä
 - Uuden käyttäjän luomisnäkymä
 - Kurssinäkymä

Näkymät sijaitsevat [_ui_](https://github.com/juhana-peltomaa/ot-harjoitustyo/tree/master/CourseTrackerApp/src/ui)-kansiossa, jossa kaikki näkymät on toteuttu omina luokkinaan. [UI](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/ui/ui.py)-luokka vastaa näkymien välillä siirtymisestä ja ainoastaan yksi näkymä on kerrallaan näkyvissä. 

Käyttöliittymässä tapahtuvat toiminnallisuudet on pyritty erottamaan sovelluslogiikasta, jolloin käyttöliittymä ainoastaan kutsuu sovelluslogiikasta vastaavan [CourseService](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py) -luokan metodeja.

## Sovelluslogiikka

Sovelluksen tietokohteet koostuvat kahdesta luokasta: [_User_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/entities/user.py) ja [_Course_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/entities/course.py). Nämä luokat sisältävät koodin sovelluksen käyttämistä käyttäjä sekä kurssi -olioista. 

![Viikko 4-pakkauskaavio-6](https://user-images.githubusercontent.com/55188494/115162423-badb9c00-a0a3-11eb-923e-c39171d18a86.png)

Sovelluksen toiminnallisuudet on tallennettu luokkaan [_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py), jonka avulla eri käyttöliittymä näkymien toiminnallisuuksia toteutetaan. Luokan [_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py) käyttää toteutuksessa hyväksi pääsyä tiedon pysyväistallennuksesta vastaaviin luokkiin [_UserRepo_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/repositories/user_repo.py) ja [_CourseRepo_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/repositories/course_repo.py). 


## Päätoiminnallisuudet

Alla kuvatuu sovelluksen olleellisia toimintalogiikan osia sekvenssikaavioiden avulla.

### Sisäänkirjatuminen sovellukseen

Sovelluksen käynnistäminen asettaa [_LoginView_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/ui/login_view.py) -näkymän käyttäjälle. Käyttäjän painaessa _"Login"_ -painiketta, täytettyään ensin näkymän syötekenttiin käyttäjätunnuksen ja salasanan, sovellusksen toiminnallisuus etenee seuraavasti:

![Käyttäjän kirjautuminen](https://user-images.githubusercontent.com/55188494/116088508-3809a100-a6a2-11eb-8bdc-18a19c7de7b1.png)

_"Login"_ -painike hakee syötekenttien sisällön ja käyttää niitä parametreinä kutsuessaan sovelluslogiikan [_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py) metodia _login_user_. Sovelluslogiikka tarkistaa, onko asetettu käyttäjätunnus olemassa kutsumalla _find_user_ -metodia _UserRepo_ -luokasta. 

Jos käyttäjä on olemassa, palauttaa metodi käyttäjän tiedot, jonka jälkeen sovelluslogiikka tarkistaa vastaavatko ne paramentreinä annettuja salasanaa ja käyttäjätunnusta. Jos täsmää, metodi asettaa käyttäjän nykykäyttäjäksi ja kutsuu _show_courses_view_-metodia, jolloin näkymäksi asetetaan [_CourseView_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/ui/course_view.py) -näkymä. 

### Uuden kurssin lisääminen sovellukseen

Kirjauduttua sisään, käyttäjä voi luoda ja tallentaa uuden kurssin sekä asettaa sen näkymäänsä painamalla _"Add new course"_ -painiketta. Tällöin sovelluksen toiminnallisuus etenee seuraavasti:

![Uuden kurssin lisääminen](https://user-images.githubusercontent.com/55188494/116094913-393dcc80-a6a8-11eb-94bd-3256acc272ac.png)

Luodessaan kurssia, käyttäjä voi antaa sovellukselle parametreinä kurssin nimen, opintopistemäärän, arvosanan ja suoritusstatuksen niille osoitetuissa kentissä. Käyttäjän tulee kuitenkin minimissään antaa kurssin nimi sekä opintopistemäärän, jotka annettuaan sekä painiketta _"Add new Course"_ painettuaan kutsutaan [_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py) metodia _create_new_course_. 

[_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py) tarkistaa onko käyttäjä jo tallentanut kyseisen kurssin, käyttäen hyväksi metodia _find_course_, joka sijaitsee _CourseRepo_ -luokassa. Ennen metodin suorittamista, [_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py) tarkistaa sen hetkisen käyttäjän ja antaa sen parametrinä _find_course_ -metodille yhdessä kurssin nimen kanssa. 

Jos käyttäjältä ei löydy annettua kurssia, metodi palauttaa arvon _None_. Tämän jälkeen tarkistetaan syötettyjen opintopistemäärän ja arvosanan oikeellisuus kutsumalla _validate_credit_ ja _validate_grade_ -metodeja. 

Tarkistuksien läpäistyä, [_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py) luo [_Course_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/entities/course.py) -olion annetuilla parametreilla ja tallentaa sen _CourseRepo_:oon metodilla _create_course_. Kurssien luomisen ja tallentamisen onnistuessa [_CourseView_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/ui/course_view.py) kutsuu metodia _display_all_courses_, joka hakee kaikki käyttäjän kurssit kutsumalla [_CourseService_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/services/course_service.py):in metodin _display_all_courses_ kautta _CourseRepo_:n metodia _find_all_courses_. Metodi palauttaa kaikki käyttäjän tämän hetkiset kurssit ja asettaa ne näkyville [_CourseView_](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/ui/course_view.py) -näkymään.

