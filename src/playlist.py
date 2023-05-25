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