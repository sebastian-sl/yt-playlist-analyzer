import sqlite3

# Database Class for Con
class DB:
    fp = r"./db/database.db"
    con = sqlite3.connect(fp)
    cursor = con.cursor()

    # Inherits insert function to Subclasses, 
    # Object can be dumped to Database into the Table which is represented by Class Attribute
    # and dumps all attribute values into the attribute names = column names
    def insert(self):
        keys = ", ".join([key for key in self.__dict__])
        values = [self.__dict__[key] for key in self.__dict__]

        wildcards = ", ".join(["?" for i in range(len(values))])

        sql = f"INSERT OR IGNORE INTO {self.tbl} ({keys}) VALUES ({wildcards})"

        DB.cursor.execute(sql, values)
        DB.con.commit()