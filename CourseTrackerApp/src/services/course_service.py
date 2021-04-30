from entities.course import Course
from entities.user import User

import re
import requests
from repositories.course_repo import course_repository as c_repo
from repositories.user_repo import user_repository as u_repo


class ExistingUsernameError(Exception):
    pass


class LoginError(Exception):
    pass


class ExistingCourseError(Exception):
    pass


class CourseEntryError(Exception):
    pass


class CourseUpdateError(Exception):
    pass


class CourseValueError(Exception):
    pass


class InvalidUrlError(Exception):
    pass


class CourseService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, course_repository=c_repo, user_repository=u_repo):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan luokan

        Args:
            course_repository:
                        Vapaaehtoinen, oletusarvoltaan CourseRepo -olio.
                        Olio, jolla on CourseRepo -luokan metodit.
            user_repository:
                        Vapaaehtoinen, oletusarvoltaan UserRepo -olio.
                        Olio, jokka on UserRepo -luokan metodit.

        """

        self._user = None
        self._c_repo = course_repository
        self._u_repo = user_repository

    def login_user(self, username, password):
        """Kirjaa käyttäjän sovellukseen sisään, jos käyttäjä on olemassa ja syötteet vastaavat tallennettuja tietoja.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.

        Raises:
            LoginError: Virheellinen käyttäjätunnus tai salasana.

        Returns:
            user, joka sisältää tietokantaan tallennetun käyttäjän tiedot
        """

        user = self._u_repo.find_user(username, password)

        if user:
            username_check = user["username"]
            password_check = user["password"]

            if str(username_check) != str(username) or str(password_check) != str(password):
                raise LoginError("Login failed! Invalid username or password.")

            self._user = user
            return user

        raise LoginError("Login failed! Invalid username or password.")

    def create_new_user(self, username, password):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.

        Raises:
            ExistingUsernameError: Käyttäjätunnus on jo käytössä.

        Returns:
            new_user, joka kuvastaa käyttäjän lisäystä tietokantaan.
        """

        exists = self._u_repo.find_username(username)

        if exists:
            raise ExistingUsernameError(
                f"Username {username} is already in-use!")

        new_user = self._u_repo.create_user(User(username, password))
        return new_user

    def current_user(self):
        """Palauttaa nykyisen käyttäjän tunnuksen.

        Returns:
            Nykyisen käyttäjän käyttäjätunnus.
        """

        return self._user["username"]

    def logout_user(self):
        """Kirjaa käyttäjän ulos, asettamalla nykyisen käyttäjän arvoksi None.

        """

        self._user = None

    def create_new_course(self, name, credit, grade, status, url):
        """Luo uuden kurssin annetuilla syötteillä.

        Args:
            name: Merkkijonoarvo, joka kuvaa kurssin nimejä.
            credit: Numeroarvo, joka kuvaa kurssin opintopiste määrää.
            grade: Numeroarvo, joka kuvaa kurssin arvosanaa.
            status: Boolean-arvo, joka kuvaa kurssin suoritustilaa.
            url: Merkkijonoarvo, joka kuvastaa kurssiin liittyvää URL-osoitetta.

        Raises:
            CourseEntryError: Kurssin nimeä tai opintopistemäärää ei ole annettu.
            ExistingCourseError: Käyttäjällä on jo saman niminen kurssi tallennettuna
            CourseValueError: Kurssin opintopiste tai arvosana syöte ei ole sallitulla välillä.
            InvalidUrlError: Kurssin URL syöte ei ole sallitussa muodossa.

        Returns:
            course, joka kuvastaa kurssin lisäystä tietokantaan
        """

        exists = self._c_repo.find_course(name, self.current_user())

        # Nimi ja opintopiste määrä tulee antaa kurssia luodessa
        if len(name) <= 0 or len(credit) <= 0:
            raise CourseEntryError()

        if exists:
            raise ExistingCourseError()

        # Tarkistetaan opintopiste, arvosana ja url syötteiden oikeellisuus
        if self.validate_credit(str(credit)) is not True:
            raise CourseValueError()

        if self.validate_grade(str(grade), status) is not True:
            raise CourseValueError()

        if self.validate_url(str(url)) is not True:
            raise InvalidUrlError()

        # Jos syötteet ovat valideja, luo uuden kurssin ja tallentaa sen tietokantaan
        user = self.current_user()
        course = Course(name, credit, grade, str(
            status), user, url)
        course = self._c_repo.create_course(course)
        return course

    def validate_credit(self, credit):
        """Tarkistaa, että syöte opintopisteille on " " tai väliltä 0-10.

        Args:
            credit: Numeroarvo, joka kuvaa kurssin opintopiste määrää.

        Returns:
            True, jos syöte on sallittu, muussa tapauksessa False
        """

        accepted = re.compile(r'^([0-9]|1[0]|\s)$')
        if accepted.match(credit):
            return True
        return False

    def validate_grade(self, grade, status):
        """Tarkistaa, että arvosana on " " tai väliltä 0-5. Lisäksi, kun status on "Completed" tarkistetaan, että arvosana on annettu.

        Args:
            grade: Numeroarvo, joka kuvaa kurssin arvosanaa.
            status: Boolean-arvo, joka kuvaa kurssin suoritustilaa.

        Returns:
            True, jos syöte on sallitulta väliltä, muuten False.
        """

        if status == "Completed":
            accepted = re.compile(r'([0-5])$')

            if accepted.match(grade):
                return True

            return False

        if len(grade) == 0:
            grade = " "

        accepted = re.compile(r'([0-5]|\s)$')

        if accepted.match(grade):
            return True

        return False

    def validate_url(self, url):
        """Tarkistaa, onko URL-syöte annettu oikeassa muodossa, jos syöte sisältää tekstiä.

        Args:
            url: Merkkijonoarvo, joka kuvastaa kurssiin liittyvää URL-osoitetta.

        Raises:
            InvalidUrlError: URL ei ole sallitussa muodossa.

        Returns:
            True, jos syöte on sallittu, muussa tapauksessa False.
        """

        if len(url) == 0 or url == " ":
            return True

        try:
            website = requests.get(url, stream=True)
        except Exception:
            raise InvalidUrlError()

        if website.status_code == 200:
            return True

        return False

    def display_all_courses(self):
        """ Hakee tietokannasta kaikki kurssit ja palauttaa käyttäjälle kuuluvat kurssit listana

        Returns:
            course_list, joka sisältää tiedot käyttäjän kursseista listassa. Jos käyttäjällä ei ole kursseja, palautetaan None.
        """

        course_list = []
        courses = self._c_repo.find_all_courses()

        if courses:
            for row in courses:
                id = row["id"]
                name = row["name"]
                credit = row["credit"]
                grade = row["grade"]
                status = row["status"]
                user = row["user"]
                url = row["url"]

                if user == self.current_user():
                    course_list.append(
                        [id, name, credit, grade, status, user, url])

            return course_list

        return None

    def statistics(self):
        """Luo statistiikka käyttäjän suorittamista kursseista.

        Returns:
            completed_courses, joka sisältää kurssien lukumäärän, joiden status on "Completed".
            completed_credits, joka sisältää opintopiste määrän kursseista, joiden status on "Completed".
            avg_gpa, joka sisältää painotetun keskiarvon kursseista, joiden status on "Completed".
        """

        completed_courses = 0
        completed_credits = 0
        avg_gpa = 0

        courses = self._c_repo.find_all_courses()

        if courses:
            for row in courses:
                id = row["id"]
                credit = row["credit"]
                grade = row["grade"]
                status = row["status"]
                user = row["user"]

                if user == self.current_user() and status == "Completed":
                    completed_courses += 1
                    completed_credits += credit
                    weighted_grade = credit * grade
                    avg_gpa += weighted_grade

        if completed_courses > 0:
            avg_gpa = avg_gpa / completed_credits
            avg_gpa = round(avg_gpa, 2)

        return completed_courses, completed_credits, avg_gpa

    def remove_all_courses(self):
        """Poistaa tietokannasta kaikki käyttäjälle kuuluvat kurssit

        Raises:
            CourseUpdateError: Kurssien poistaminen epäonnistui.

        Returns:
            True, jos kurssien poistaminen onnistui.
        """

        try:
            self._c_repo.delete_all(self._user["username"])
            return True
        except Exception:
            raise CourseUpdateError()

    def remove_one_course(self, name):
        """Poistaa tietokannasta käyttäjälle kuuluvan kurssin sen nimen perusteella

        Args:
            name: Merkkijonoarvo, joka kuvaa kurssin nimejä.

        Raises:
            CourseUpdateError: Kurssin poistaminen epäonnistui.

        Returns:
            True, jos kurssin poistaminen onnistui.
        """

        try:
            self._c_repo.delete_one_course(name, self.current_user())
            return True
        except Exception:
            raise CourseUpdateError()

    def update_course_info(self, id, name, credit, grade, status, url):
        """Päivittää kurssin tiedot, tarkistaa syötteiden oikeellisuuden

        Args:
            name: Merkkijonoarvo, joka kuvaa kurssin nimejä.
            credit: Numeroarvo, joka kuvaa kurssin opintopiste määrää.
            grade: Numeroarvo, joka kuvaa kurssin arvosanaa.
            status: Boolean-arvo, joka kuvaa kurssin suoritustilaa.
            url: Merkkijonoarvo, joka kuvastaa kurssiin liittyvää URL-osoitetta.

        Raises:
            CourseValueError: Kurssin opintopiste tai arvosana syöte ei ole sallitulla välillä.
            InvalidUrlError: Kurssin URL syöte ei ole sallitussa muodossa.

        Returns:
            True, jos kurssin tietojen päivittäminen onnistui.
        """

        if self.validate_credit(str(credit)) is not True:
            raise CourseValueError()
        if self.validate_grade(str(grade), status) is not True:
            raise CourseValueError()
        if self.validate_url(str(url)) is not True:
            raise InvalidUrlError()

        self._c_repo.update_course_info(
            id, name, credit, grade, str(status), self.current_user(), url)
        return True


course_service = CourseService()
