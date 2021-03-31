from database_connection import get_database_connection

# huomio, että nyt luodaan ainoastaan user TABLE! Lisää myöhemmin tulevat tähän1

CREATE_USER_TABLE = "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT);"

DROP_USER_TABLE = "DROP TABLE IF EXISTS users"


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute(DROP_USER_TABLE)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(CREATE_USER_TABLE)

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
