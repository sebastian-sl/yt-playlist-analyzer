import sqlite3

class DB:

    def __init__(self):
        self.storage_location = r"./src/db/database.db"

    def connect(self):
        self.conn = sqlite3.connect(self.storage_location)

        return self.conn