import datetime
from .db import DB

class Playlist(DB):
    tbl = "playlists"
    sub_tbl = "videos"

    def __init__(self, pl_id, title):
        self.pl_id = pl_id
        self.title = title
        self.last_checked = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")

    # returns all Videos corresponding to a playlist as a dict
    def collect_all_videos(self):
        sql = f"SELECT * FROM {Playlist.sub_tbl} WHERE pl_id = ?"

        response = DB.cursor.execute(sql, (self.pl_id,)).fetchall()

        cols = [col[0] for col in DB.cursor.description]
        rows = [dict(zip(cols, row)) for row in response]

        return rows
    
    # updates the count_active and count_missing in the playlist Table
    def update_count(self):
        sql = f"UPDATE {Playlist.tbl} SET count_active = 0, count_missing = 0 WHERE pl_id = ?"
        DB.cursor.execute(sql, (self.pl_id,))
        DB.con.commit()

        sql = f"""
            UPDATE {Playlist.tbl} SET
            count_active = (SELECT SUM(active) FROM videos WHERE {Playlist.tbl}.pl_id = {Playlist.sub_tbl}.pl_id),
            count_missing = (SELECT SUM(missing) FROM videos WHERE {Playlist.tbl}.pl_id = {Playlist.sub_tbl}.pl_id)
            WHERE {Playlist.tbl}.pl_id = ?
        """

        DB.cursor.execute(sql, (self.pl_id,))
        DB.con.commit()