from database_connection import get_database_connection


CREATE_COURSE = "INSERT OR IGNORE INTO courses (name, credit, grade, status, user, url) VALUES (?, ?, ?, ?, ?, ?);"

FIND_COURSE = "SELECT * FROM courses WHERE name = ? and user = ?;"

DELETE_ALL_COURSES = "DELETE FROM courses WHERE user = ?;"

EMPTY_COURSES = "DELETE FROM courses;"

DELETE_ONE_COURSE = "DELETE FROM courses WHERE name = ? AND user = ?;"

FIND_ALL_COURSES = "SELECT * FROM courses;"

UPDATE_COURSE_INFO = "UPDATE courses SET name = ?, credit = ?, grade = ?, status = ?, url = ? WHERE id = ? AND user = ?;"


class CourseRepo:

    """Luokka, jolla kuvataan kursseja tallentavaa repositoria.

    Attributes:
        connection: Yhteys alustettuun tietokantaan.
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka luo uuden kurssi repositorin.

        Args:
            connection: Yhteys alustettuun tietokantaan.
        """

        self._connection = connection

    def create_course(self, new_course):
        """Lisää uuden kurssin tietokantaan.

        Args:
            new_course: Course-olio, joka kuvaa kurssia.

        Returns:
            course, joka kuvastaa kurssin lisäystä tietokantaan
        """

        cursor = self._connection.cursor()

        course = cursor.execute(
            CREATE_COURSE, (new_course.name, new_course.credit, new_course.grade, new_course.status, new_course.user, new_course.url))

        self._connection.commit()

        return course

    def find_course(self, name, user):
        """Hakee tietokannasta kurssia siihen liitetyn käyttäjän ja kurssinimen perusteella.

        Args:
            name: Merkkijonoarvo, joka kuvaa kurssin nimeä.
            user: Merkkijonoarvo, jonka arvona uniiki käyttäjänimi.

        Returns:
            course_info, joka sisältää tietokantaan tallennetut tiedot kurssista, jos se on olemassa. Muussa tapauksessa None.
        """

        cursor = self._connection.cursor()

        cursor.execute(FIND_COURSE, (name, user))

        self._connection.commit()

        course_info = cursor.fetchone()

        if course_info is not None:
            return course_info

        return None

    def find_all_courses(self):
        """Hakee tietokannasta kaikki sinne tallennetut kurssit.

        Returns:
            course_info, joka sisältää kaikkien tietokantaan tallennettujen kurssien tiedot.
        """

        cursor = self._connection.cursor()

        cursor.execute(FIND_ALL_COURSES)

        self._connection.commit()

        course_info = cursor.fetchall()

        return course_info

    def delete_all(self, user):
        """Poistaa kaikki käyttäjän (user) tietokantaan lisäämät kurssit.

            Args:
                user: Merkkijonoarvo, jonka arvona uniiki käyttäjänimi.
        """

        cursor = self._connection.cursor()

        cursor.execute(DELETE_ALL_COURSES, (user, ))

        rows_effected = cursor.rowcount

        self._connection.commit()

        return rows_effected

    def delete_one_course(self, name, user):
        """Poistaa käyttäjän (user) tietokantaan tallentaman kurssin sen nimen perusteella.

            Args:
                name: Merkkijonoarvo, joka kuvaa kurssin nimeä.
                user: Merkkijonoarvo, jonka arvona uniiki käyttäjänimi.
        """

        cursor = self._connection.cursor()

        cursor.execute(DELETE_ONE_COURSE, (name, user))

        rows_effected = cursor.rowcount

        self._connection.commit()

        return rows_effected

    def update_course_info(self, id, name, credit, grade, status, user, url):
        """Päivittää kurssin tietokantaan tallennettuja tietoja syötettyjen arvojen perusteella.

        Args:
            id: Numeroarvo, joka on uniikki jokaiselle kurssille.
            name: Merkkijonoarvo, joka kuvaa kurssin nimejä.
            credit: Numeroarvo, joka kuvaa kurssin opintopiste määrää.
            grade: Numeroarvo, joka kuvaa kurssin arvosanaa.
            status: Boolean-arvo, joka kuvaa kurssin suoritustilaa.
            user: Merkkijonoarvo, joka saa arvoksi uniikin käyttäjän nimen.
            url: Merkkijonoarvo, joka kuvastaa kurssiin liittyvää URL-osoitetta.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            UPDATE_COURSE_INFO, (name, credit, grade, status, url, id, user))

        self._connection.commit()

    def empty_courses(self):
        """Poistaa kaikien käyttäjien kaikki tietokantaan tallentamat kurssit. Metodia käytetään testien alustamiseksi.

        """

        cursor = self._connection.cursor()

        cursor.execute(EMPTY_COURSES)

        self._connection.commit()


course_repository = CourseRepo(get_database_connection())
