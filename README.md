## Idea
While using Youtube playlists more frequently, i sometimes noticed missing Videos from my playlists because they got deleted or went private. Sadly you don't get noticed <u>which</u> video exactly got removed from the playlist, youtube only provides the following info:

![alt text](https://raw.githubusercontent.com/sebastian-sl/yt-playlist-analyzer/main/img/missing%20videos.png)

<br>
The current plan is to use <u> windows task planner </u> to execute a check for every playlist in a certain timeframe (weekly, monthly) and lookup if all videos are still in the playlist or not. This way you can find out what video is missing and can (maybe) be replaced with the same video from another source. 

<br> 

## Workflow
- [X] implement Youtube authorization and connection
- [X] retrieve response for Playlist and PlaylistItems from Youtube API
- [X] check Video for availability and if its already stored in DB
- [X] update status or insert API Videos to DB
- [X] implement business logic to count active/missing values in playlist
- [ ] implement attribute check for certain columns (title, description etc)
- [X] implement an ignore column in the database (in case a Video is already replaced) and/or write delete method
- [X] return all Missing Videos in CLI
- [ ] implement some kind of frontend
<br>
