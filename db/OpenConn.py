import sqlite3
from sqlite3 import Error

class ConnManager(object):
    def __init__(self):
        self.db = None

    def __enter__(self):
        try:
            self.db = sqlite3.connect("db/flashcards.db")
            return self.db.cursor()
        except Error as e:
            print(e)

        return None

    def __exit__(self, type, value, traceback):
        self.db.commit()
        self.db.close()
        
