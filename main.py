# Google & OAuth Imports
import googleapiclient.discovery
from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

# Local imports
from src.playlist import Playlist
from src.video import Video
from src.db import DB

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
client_secrets_file = "google_credentials.json"
cred_file = "credentials.json"

def authorize():
    api_service_name = "youtube"
    api_version = "v3"

    store = Storage(cred_file)
    credentials = store.get()

    if not credentials:
        flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
        credentials = tools.run_flow(flow, store)

    return googleapiclient.discovery.build(api_service_name, api_version, credentials = credentials)


def playlist_request():
    youtube = authorize()

    request = youtube.playlists().list(
        part="contentDetails, snippet",
        mine=True,
        maxResults = 50
    )

    response = request.execute()

    return response

    
def playlist_items_request(playlistId):
    youtube = authorize()

    request = youtube.playlistItems().list(
        part = "contentDetails, snippet",
        maxResults = 50,
        playlistId = playlistId
    )

    response = request.execute()

    return response


def main():
    playlists = playlist_request()

    for playlist in playlists["items"]:
        pl = Playlist(pl_id = playlist["id"], title = playlist["snippet"]["title"])

        # Inserts Playlist into the Database Table (or ignore if ID already exists)
        pl.insert()

        # Fetching all Videos from the API to playlist ID
        fetch_api = playlist_items_request(pl.pl_id)

        # Setting all Videos in Database to Inactive/Missing (This removes needage to iterate over Database entries)
        Video.set_all_missing()


        for video in fetch_api["items"]:
            # Check if each Video is in Database & if its an available Video (not private, deleted etc.)
            match = Video.check_db(video["id"])
            available = Video.check_availability(video["snippet"]["description"])

            # If in DB and Available update the Database record to Active (we set all to inactive, see above)
            if match and available:
                Video.update_status(1, 0, video["id"])
            
            # If not in DB but available, create an Instance of Video (serializing) and insert to Database
            elif not match and available:
                vid = Video(video, 1, 0)
                vid.insert()

if __name__ == "__main__":
    main()