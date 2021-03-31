from entities.user import User
from database_connection import get_database_connection


# nyt mahdollista ainoastaan luoda uusi käyttäjä - lisätään ominaisuuksia myöhemmin

CREATE_USER = "INSERT INTO users (username, password) VALUES (?, ?);"


class UserRepo:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, password):
        cursor = self._connection.cursor()

        user = cursor.execute(CREATE_USER, (username, password))

        return user


user_repository = UserRepo(get_database_connection())
