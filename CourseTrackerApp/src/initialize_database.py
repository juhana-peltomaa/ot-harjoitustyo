from database_connection import get_database_connection


CREATE_USER_TABLE = "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT);"

DROP_USER_TABLE = "DROP TABLE IF EXISTS users"

CREATE_COURSES_TABLE = "CREATE TABLE IF NOT EXISTS courses (name TEXT PRIMARY KEY, credit INTEGER, grade INTEGER, status TEXT, user TEXT);"

DROP_COURSES_TABLE = "DROP TABLE IF EXISTS courses"


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute(DROP_USER_TABLE)

    cursor.execute(DROP_COURSES_TABLE)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(CREATE_USER_TABLE)

    cursor.execute(CREATE_COURSES_TABLE)

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
