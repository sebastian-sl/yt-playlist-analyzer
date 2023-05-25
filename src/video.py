import datetime
from .db import DB

class Video(DB):
    tbl = "videos"
    
    # Initialize with relevant Video Information 
    def __init__(self, video_pl_id, idd, title, description, thumbnail, channel, channel_id, pl_id, pl_position):
        self.video_pl_id = video_pl_id

        self.id = idd
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.channel = channel
        self.channel_id = channel_id

        self.pl_id = pl_id
        self.pl_position = pl_position

        self.last_checked = datetime.datetime.now().strftime('%Y-%m-%d')

    # Overwriting the equal function, makes it easier to compare all attributes of 2 objects
    def __eq__(self, other):
        if not isinstance(other, Video):
            return NotImplemented
        
        return self.__dict__ == other.__dict__