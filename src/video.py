import datetime
from .db import DB

class Video(DB):
    tbl = "videos"

    # Sets all Videos in Database as not active, this elimnates the need to iterate over all DB Rows
    @staticmethod
    def set_all_missing():
        sql = f"UPDATE {Video.tbl} SET active = 0, missing = 1"
        DB.cursor.execute(sql)
        DB.con.commit()

    # Check whether Video is stored in database
    @staticmethod
    def check_db(video_pl_id):
        sql = f"SELECT * FROM {Video.tbl} WHERE video_pl_id = ?"

        data = (video_pl_id,)
        result = DB.cursor.execute(sql, data).fetchall()

        return True if len(result) > 0 else False
    
    # Check if the Video coming from the API is available or not
    @staticmethod
    def check_availability(description):
        missing_conditions = ["This video is private.", "This video is unavailable."]

        return False if description in missing_conditions else True
    
    # Update the corresponding Database record for a given Video ID
    @staticmethod
    def update_status(active, missing, video_pl_id):
        now = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")
        
        sql = f"UPDATE {Video.tbl} SET active = ?, missing = ?, last_checked = ? WHERE video_pl_id = ?"

        data = (active, missing, now, video_pl_id)
        DB.cursor.execute(sql, data)
        DB.con.commit()

    # TO-DO: implement attribute check for certain columns (title) + ignore column (if a video is replaced)

    # Init (Serializing)
    def __init__(self, d, active, missing):
        self.video_pl_id = d["id"]
        self.id = d["contentDetails"]["videoId"]
        self.title = d["snippet"]["title"]
        self.description = d["snippet"]["description"][:30]
        self.thumbnail = d["snippet"]["thumbnails"]["default"]["url"]
        self.channel = d["snippet"]["videoOwnerChannelTitle"]
        self.channel_id = d["snippet"]["videoOwnerChannelId"]
        self.pl_id = d["snippet"]["playlistId"]
        self.pl_position = d["snippet"]["position"]
        self.active = active
        self.missing = missing
        self.last_checked = datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")