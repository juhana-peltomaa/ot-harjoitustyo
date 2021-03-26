class Course:

    # Huomio - Tässä vaiheessa kurssi instanssiin lisätään pakollisena ainoastaan nimi ja opintopisteiden määrä
    # Oletuksena uudet kurssit ovat suorittamattomia ja luodaan tarvittavat metodit,
    # joilla arvosanaa ja statusta voidaan muokata

    def __init__(self, name, credits, grade=None, status=False):
        self.name = name
        self.credits = credits
        self.grade = grade
        self.status = status
