from cgi import test
import sqlite3

def connect():
    connection = sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute("CREATE TABLE beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);")
