class Course:

    """Luokka, jolla kuvataan yksittäistä kurssia.

    Attributes:
        name: Merkkijonoarvo, joka kuvaa kurssin nimejä.
        credit: Numeroarvo, joka kuvaa kurssin opintopiste määrää.
        grade: Numeroarvo, joka kuvaa kurssin arvosanaa.
        status: Boolean-arvo, joka kuvaa kurssin suoritustilaa.
        user: Merkkijonoarvo, joka saa arvoksi uniikin käyttäjän nimen.
        url: Merkkijonoarvo, joka kuvastaa kurssiin liittyvää URL-osoitetta.
    """

    def __init__(self, name, credit, grade=None, status=False, user=None, url=None):
        """Luokan konstruktori. Luo uuden kurssin.

        Args:
            name: Merkkijonoarvo, joka kuvaa kurssin nimeä.
            credit: Numeroarvo, joka kuvaa kurssin opintopiste määrää.
            grade:
                Vapaaehtoinen, oletusarvoltaan None.
                Numeroarvo, joka kuvaa kurssin arvosanaa.
            status:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvaa kurssin suoritustilaa.
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, jonka arvona uniiki käyttäjänimi.
            url:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka kuvastaa kurssiin liittyvää URL-osoitetta.
        """

        self.name = name
        self.credit = credit
        self.grade = grade
        self.status = status
        self.user = user
        self.url = url
