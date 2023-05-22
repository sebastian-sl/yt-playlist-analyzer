import datetime

class Playlist:
    def __init__(self, pl_id, title, con):
        self.pl_id = pl_id
        self.title = title
        self.last_checked = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")
        self.con = con

    def insert_new(self):
        sql = """
            INSERT OR IGNORE INTO playlists (pl_id, title)
            VALUES (?, ?)
        """
        
        data = (self.pl_id, self.title)

        self.con.cursor().execute(sql, data)
        self.con.commit()

    def dump_date(self):
        sql = """
            UPDATE playlists SET
            last_checked = CURRENT_TIMESTAMP
            WHERE pl_id = ?
        """
        data = self.pl_id
        self.con.cursor().execute(sql, (data,))
        self.con.commit()

    def update_stats(self):
        counts = self.con.cursor.execute(f"SELECT SUM(active), SUM(missing) FROM videos WHERE pl_id = {self.id}")

        sql = (f""" 
            UPDATE playlists SET
            count_active = ?,
            count_missing = ?
            WHERE pl_id = ?
        """)

        data = (counts[0], counts[1], self.pl_id)
        self.con.cursor().execute(sql, data)
        self.con.commit()