import sqlite3

class DB:
    fp = r"./db/database.db"
    con = sqlite3.connect(fp)
    cursor = con.cursor()

    def insert(self, columnArray = None):

        # If an Array of specific columns are given, it will only drop these attributes to the DB
        if columnArray:
            keys = ", ".join([key for key in columnArray])
            values = [self.__dict__[key] for key in columnArray]

        # If no Array of columns is given, all attributes of the Object will be written to DB
        else:
            keys = ", ".join([key for key in self.__dict__])
            values = [self.__dict__[key] for key in self.__dict__]

        wildcards = ", ".join(["?" for i in range(len(values))])

        sql = f"INSERT OR IGNORE INTO {self.tbl} ({keys}) VALUES ({wildcards})"

        DB.cursor.execute(sql, values)
        DB.con.commit()