import datetime

class Video:
    # Initialize with relevant Video Information 
    def __init__(self, video_pl_id, idd, title, description, thumbnail, channel, channel_id, pl_id, pl_position, con):
        self.video_pl_id = video_pl_id

        self.id = idd
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.channel = channel
        self.channel_id = channel_id

        self.pl_id = pl_id
        self.pl_position = pl_position

        self.con = con

        self.last_checked = datetime.datetime.now().strftime('%Y-%m-%d')

    # Overwriting the equal function, makes it easier to compare all attributes of 2 objects
    def __eq__(self, other):
        if not isinstance(other, Video):
            return NotImplemented
        
        return self.__dict__ == other.__dict__
    


    # Update the last_checked attribute if they are otherwise equal
    def dump_date(self):
        pass

    # Updates the status if the video is missing
    def dump_status(self):
        pass


    # Dumps Object into Database
    def insert_new(self):
        sql = """
            INSERT OR IGNORE INTO videos (video_pl_id, id, title, description, thumbnail, channel, channel_id, pl_id, pl_position, last_checked)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        data = (self.video_pl_id, self.id, self.title, self.description, self.thumbnail, self.channel, self.channel_id, self.pl_id, self.pl_position, self.last_checked)

        self.con.cursor().execute(sql, data)
        self.con.commit()