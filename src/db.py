import sqlite3

class DB:

    def __init__(self):
        self.storage_location = r"./db/database.db"

    def connect(self):
        self.con = sqlite3.connect(self.storage_location)

        return self.con