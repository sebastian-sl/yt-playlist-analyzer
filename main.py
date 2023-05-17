import os
import googleapiclient.discovery

from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

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


def main():
    youtube = authorize()

    request = youtube.playlists().list(
        part="snippet, contentDetails",
        mine=True
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()