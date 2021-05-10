# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa `CourseService`-luokkaa testataan [TestCourseService](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/tests/course_service_test.py) -luokalla. 



### Repositorio-luokat

Repositorio-luokkia `CourseRepo` ja `UserRepo` testataan ainoastaan testeissä määritetyillä muuttujilla. `CourseRepo`-luokkaa testataan [TestCourseRepo](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/tests/course_repo_test.py) -luokalla ja `UserRepo`-luokkaa [TestUserRepo](https://github.com/juhana-peltomaa/ot-harjoitustyo/blob/master/CourseTrackerApp/src/tests/user_repo_test.py) -luokalla.

Testauksessa käytettävä SQLite -tietokanta ja ympäristomuuttujat on konfiguroitu _.env.test_-tiedostoon.

### Testauskattavuus



## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla macOS -ympäristössä. Sovelluksen konfiguraatiossa hyödynnetään _.env_- ja _.env.test_-tiedostoja normaalin käytön sekä testauksen tietokantojen erottamiseksi. 

Sovellusta on testattu tilanteissa, jossa käyttäjän tietoja tallentavat tietokannat ovat olemassa sekä tilanteissa, jossa nämä puuttuvat ja ohjelma luo tietokannat itse.

### Toiminnallisuudet

Testauksessa on pyritty huomioimaan kaikki [määrittelydokumentin](./vaatimusmaarittely.md) ja [käyttöohjeen](./kayttoohje.md) sisältämät toiminnallisuudet. Listattujen toiminnallisuuksien toimivuutta on testattu erilaisilla virheellisillä arvoilla ja käyttäjälle annetaan kuvaavia virheilmoituksia tilanteesta riippuen.

## Sovellukseen jääneet laatuongelmat
Käyttäjä ei saa virheilmoituksia mm. seuraavissa tilanteissa:

 - Käyttäjällä ei ole konfiguraatiossa määriteltyihin tiedostoihin oikeuksia
 - Pysyväistallennukseen käytettävää tietokantaa ei ole alustettu. Tällöin tulisi suorittaa _"python -m poetry run invoke build"_-komento.
