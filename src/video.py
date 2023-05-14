class Video:
    # Initialize with relevant Video Information 
    def __init__(self, title, channel, year):
        self.title = title
        self.channel = channel
        self.year = year

    # Updates the current Object attributes with new Information (first seen, last seen, active, missing)
    def update(self):
        pass

    # Dumps Object into Database or updates existing DB Entry
    def dump(self):
        pass