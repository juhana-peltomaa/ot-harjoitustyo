from database_connection import get_database_connection


CREATE_USER = "INSERT INTO users (username, password) VALUES (?, ?);"

FIND_USER = "SELECT * FROM users WHERE username = ? AND password = ?;"

FIND_USERNAME = "SELECT * FROM users WHERE username = ?;"

DELETE_ALL = "DELETE FROM users;"

DELETE_USER = "DELETE FROM users WHERE username = ?;"

FIND_ALL_USERS = "SELECT * FROM users;"


class UserRepo:
    """Luokka, jolla kuvataan käyttäjiä tallentavaa repositoria.

    Attributes:
        connection: Yhteys alustettuun tietokantaan.
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka luo uuden käyttäjä repositorin.

        Args:
            connection: Yhteys alustettuun tietokantaan.
        """

        self._connection = connection

    def create_user(self, user):
        """Lisää uuden käyttäjän tietokantaan.

        Args:
            user: User-olio, joka kuvaa käyttäjää.

        Returns:
            user_execution, joka kuvastaa käyttäjän lisäystä tietokantaan.
        """

        cursor = self._connection.cursor()

        user_execution = cursor.execute(
            CREATE_USER, (user.username, user.password))

        self._connection.commit()

        return user_execution

    def find_user(self, username, password):
        """Hakee tietokannasta käyttäjän tiedot käyttäjän nimen ja salansanan perusteella.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.

        Returns:
            user_info, käyttäjän tiedot tietokannasta, jos käyttäjä on olemassa.
        """

        cursor = self._connection.cursor()

        cursor.execute(FIND_USER, (username, password))

        self._connection.commit()

        user_info = cursor.fetchone()

        return user_info

    def find_username(self, username):
        """Etsii tietokannasta käyttäjää käyttäjä nimen perusteella.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.

        Returns:
            True, jos käyttäjä on olemassa, muussa tapauksessa None.
        """

        cursor = self._connection.cursor()

        cursor.execute(FIND_USERNAME, (username,))

        self._connection.commit()

        user_info = cursor.fetchone()

        if user_info:
            return True

        return None

    def find_all_users(self):
        """Hakee kaikkien tietokantaan tallennettujen käyttäjien tiedot.

        Returns:
            users_info, joka sisältää kaikkien tietokantaan tallennettujen käyttäjien tiedot.
        """

        cursor = self._connection.cursor()

        cursor.execute(FIND_ALL_USERS)

        self._connection.commit()

        users_info = cursor.fetchall()

        return users_info

    def delete_all(self):
        """Poistaa kaikki tietokantaan tallennetut käyttäjät.

        """

        cursor = self._connection.cursor()

        cursor.execute(DELETE_ALL)

        self._connection.commit()

    def delete_user(self, user):
        """Poistaa valitun käyttäjän (user) tietokannasta

        """

        cursor = self._connection.cursor()
        cursor.execute(DELETE_USER, (user, ))

        self._connection.commit()


user_repository = UserRepo(get_database_connection())
