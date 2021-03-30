import os
import sqlite3

dirname = os.path.dirname(__file__)

# nämä on vielä kova koodattu, muista vaihtaa!
# connection = sqlite3.connect(os.path.join(
#   __dirname, "..", "data", "database.sqlite"))
connection = sqlite3.connect("practice.db")
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
