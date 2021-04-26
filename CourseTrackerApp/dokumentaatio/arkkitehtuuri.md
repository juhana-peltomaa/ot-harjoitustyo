# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen arkkitehtuurirakenne on kolmitasoinen ja se koostuu seuraavanlaisesta pakkausrakenteesta:

![Viikko4-pakkauskaavio](https://user-images.githubusercontent.com/55188494/115162660-122e3c00-a0a5-11eb-908c-f1968a0871e6.png)

Käyttöliittymä sisältyy pakkaukseen _ui_, sovelluslogiikka on eritelty pakkaukseen _services_ ja vastaavasti käytettyjen tietokohteiden pysyväisyystallennus pakkaukseen _repositories_. Sovelluksen käyttämät tietokohteet ovat pakkauksessa _entities_. 


## Sovelluslogiikka

Sovelluksen tietokohteet koostuvat kahdesta luokasta: _User_ ja _Course_. Nämä luokat sisältävät koodin sovelluksen käyttäjistä sekä kursseista. 

![Viikko 4-pakkauskaavio-6](https://user-images.githubusercontent.com/55188494/115162423-badb9c00-a0a3-11eb-923e-c39171d18a86.png)

Sovelluksen toiminnallisuudet on tallennettu luokkaan _CourseServices_, jonka avulla eri käyttöliittymä näkymien toiminnallisuuksia toteutetaan. Luokan _CourseServices_ käyttää toteutuksessa hyväksi pääsyä tiedon pysyväistallennuksesta vastaaviin luokkiin _UserRepo_ ja _CourseRepo_. 


## Päätoiminnallisuudet

Alla kuvatuu sovelluksen olleellisia toimintalogiikan osia sekvenssikaavioiden avulla.

### Sisäänkirjatuminen sovellukseen

![Käyttäjän kirjautuminen](https://user-images.githubusercontent.com/55188494/116088508-3809a100-a6a2-11eb-8bdc-18a19c7de7b1.png)

### Uuden kurssin lisääminen sovellukseen
![Uuden kurssin luominen ](https://user-images.githubusercontent.com/55188494/116088299-085a9900-a6a2-11eb-8c99-36132471bfa7.png)
