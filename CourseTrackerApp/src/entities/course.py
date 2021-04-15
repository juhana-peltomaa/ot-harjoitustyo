class Course:

    # Huomio - Tässä vaiheessa kurssi instanssiin lisätään pakollisena ainoastaan nimi ja opintopisteiden määrä
    # Oletuksena uudet kurssit ovat suorittamattomia ja luodaan tarvittavat metodit, joilla arvosanaa ja statusta voidaan muokata
    # User-ilmaisee käyttäjä-olion, joka voidaan linkittää kurssisuorituksiin

    def __init__(self, name, credit, grade=None, status=False, user=None):
        self.name = name
        self.credit = credit
        self.grade = grade
        self.status = status
        self.user = user
