import datetime
from .db import DB

class Playlist(DB):
    tbl = "playlists"

    def __init__(self, pl_id, title):
        self.pl_id = pl_id
        self.title = title
        self.last_checked = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")