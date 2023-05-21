import os
import json

# Google & OAuth Imports
import googleapiclient.discovery
from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

# Local imports
from src.DB import DB
from src.Playlist import Playlist
from src.Video import Video

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


def yt_test():
    youtube = authorize()

    request = youtube.playlists().list(
        part="snippet",
        mine=True,
        prettyPrint=True,
        maxResults = 50
    )
    response = request.execute()

    titles = []
    for item in response["items"]:
        title = item["snippet"]["title"]
        titles.append(title)

    print(titles)


def db_con_test():
    database = DB()
    database.connect()

if __name__ == "__main__":
    yt_test()