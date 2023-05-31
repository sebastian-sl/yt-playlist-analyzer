import datetime
from .db import DB

class Video(DB):
    tbl = "videos"

    # Sets all Videos in Database as not active, this elimnates the need to iterate over all DB Rows
    @staticmethod
    def set_all_missing(pl_id):
        sql = f"UPDATE {Video.tbl} SET active = 0, missing = 1 WHERE pl_id = ?"
        DB.cursor.execute(sql, (pl_id,))
        DB.con.commit()

    # Check whether Video is stored in database
    def check_db(self):
        sql = f"SELECT * FROM {Video.tbl} WHERE video_pl_id = ?"

        data = (self.video_pl_id,)
        result = DB.cursor.execute(sql, data).fetchall()

        return True if len(result) > 0 else False
    
    # Check if the Video coming from the API is available or not
    @staticmethod
    def check_availability(description):
        missing_conditions = ["This video is private.", "This video is unavailable."]

        return False if description in missing_conditions else True
    
    # Update the corresponding Database record for a given Video ID
    def update_video(self):
        now = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")
        
        sql = f"UPDATE {Video.tbl} SET active = ?, missing = ?, last_checked = ? WHERE video_pl_id = ?"

        sql = f"""
        UPDATE {Video.tbl} SET
        title = ?,
        description = ?,
        thumbnail = ?,
        pl_position = ?,
        last_checked = ?,
        active = ?,
        missing = ?
        """

        data = (self.title, self.description, self.thumbnail, self.pl_position, now, self.active, self.missing) 
        DB.cursor.execute(sql, data)
        DB.con.commit()

    # Init (Serializing)
    def __init__(self, d, active, missing):
        self.video_pl_id = d["id"]
        self.id = d["contentDetails"]["videoId"]
        self.title = d["snippet"]["title"]
        self.description = d["snippet"]["description"][:75]
        self.thumbnail = d["snippet"]["thumbnails"]["high"]["url"]
        self.channel = d["snippet"]["videoOwnerChannelTitle"]
        self.channel_id = d["snippet"]["videoOwnerChannelId"]
        self.pl_id = d["snippet"]["playlistId"]
        self.pl_position = d["snippet"]["position"]
        self.active = active
        self.missing = missing
        self.last_checked = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")