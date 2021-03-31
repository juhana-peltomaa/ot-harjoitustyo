from entities.user import User
from database_connection import get_database_connection

CREATE_USER = "INSERT INTO USERS (username, password) VALUES (?, ?);"


class UserRepo:
    def __init__(self, connection):
        self.connection = connection

    def create_user(connection, username, password):
        cursor = self._connection.cursor()

        cursor.execute(CREATE_USER, (username, password))

        return user


user_repository = UserRepo(get_database_connection())
