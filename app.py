from multiprocessing import connection


import database

def menu():
    connection = database.connect()
    database.create_tables(connection)
    
