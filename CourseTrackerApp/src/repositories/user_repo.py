from database_connection import get_database_connection


CREATE_USER = "INSERT INTO users (username, password) VALUES (?, ?);"

FIND_USER = "SELECT * FROM users WHERE username = ? AND password = ?;"

FIND_USERNAME = "SELECT * FROM users WHERE username = ?;"

DELETE_ALL = "DELETE FROM users;"

FIND_ALL_USERS = "SELECT * FROM users;"


class UserRepo:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        cursor = self._connection.cursor()

        user = cursor.execute(CREATE_USER, (user.username, user.password))

        self._connection.commit()

        return user

    def find_user(self, username, password):
        cursor = self._connection.cursor()

        cursor.execute(FIND_USER, (username, password))

        self._connection.commit()

        user_info = cursor.fetchone()

        return user_info

    def find_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(FIND_USERNAME, (username,))

        self._connection.commit()

        user_info = cursor.fetchone()

        if user_info:
            return True

        return None

    def find_all_users(self):
        cursor = self._connection.cursor()

        cursor.execute(FIND_ALL_USERS)

        self._connection.commit()

        users_info = cursor.fetchall()

        return users_info

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute(DELETE_ALL)

        self._connection.commit()


user_repository = UserRepo(get_database_connection())
