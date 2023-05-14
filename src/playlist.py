class Playlist:
    # Initialize Playlist with given name
    def __init__(self, name, privacy):
        self.name = name
        self.privacy = privacy


    # updates current object attributes with new info (first seen, last seen)
    def update(self):
        pass

    # Collects all videos corresponding to the playlist from API or DB
    def set_videos(self):
        pass

    # returns all videos from the playlist
    def get_videos(self):
        pass

    # compares two playlists (from different sources)
    # by length and/or name comparison
    @classmethod
    def compare(first_playlist, second_playlist):
        pass

    # gives out all videos from the playlist that are missing
    def report_missing(self):
        pass