import os
import json

# Google & OAuth Imports
import googleapiclient.discovery
from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

# Local imports
from src.db import DB
from src.playlist import Playlist
from src.video import Video

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
        prettyPrint=True,
        maxResults = 20
    )

    response = request.execute()

    # with open("./resp/playlist_response.json", "w") as f:
    #     json.dump(response, f, indent = 4)

    return response

    
def playlist_items_request():
    youtube = authorize()

    request = youtube.playlistItems().list(
        part = "contentDetails, snippet",
        maxResults = 2,
        playlistId = "PLhqCGkIlCJBrOfUVhwa3SZ6LDsjycW3ut"
    )

    response = request.execute()

    # with open("./resp/playlist_items_response.json", "w") as f:
    #     json.dump(response, f, indent = 4)

    return response



def main():
    con = DB().connect()

    playlists = playlist_request()

    for pl in playlists["items"]:
        obj = Playlist(
            pl_id = pl["id"],
            title = pl["snippet"]["title"],
            con = con
        )

        obj.insert_new()
        obj.dump_date()

if __name__ == "__main__":
    main()