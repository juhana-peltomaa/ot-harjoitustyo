import sqlite3
from config import DATABASE_FILE_PATH

dirname = os.path.dirname(__file__)

# Alla kova koodattu versio, muista vaihtaa!
# import os
# connection = sqlite3.connect(os.path.join(
#   __dirname, "..", "data", "database.sqlite"))

# DATABASE_FILE_PATH on määritelty .env tiedostossa

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
