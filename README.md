## Idea
While using Youtube playlists more frequently, i sometimes noticed missing Videos from my playlists because they got deleted or went private. Sadly you don't get noticed <u>which</u> video exactly got removed from the playlist, youtube only provides the following info:

![alt text](https://raw.githubusercontent.com/sebastian-sl/yt-playlist-analyzer/main/img/missing%20videos.png)

<br>
The current plan is to use <u> windows task planner </u> to execute a check for every playlist in a certain timeframe (weekly, monthly) and lookup if all videos are still in the playlist or not. This way you can find out what video is missing and can (maybe) be replaced with the same video from another source. 

<br> 

## Workflow
* enter YT Credentials somewhere (config, CLI)
* start program 
* Option 1: Check all Playlists
* Option 2: Check certain Playlist (list all current PL with ID + Name to choose which)
* compare each playlist from API to DB
* Update corresponding video attributes & perform Database actions (insert/update)

<br>

## Lookout
Further development would be to develop a chrome extension that performs this tasks when you visit one of your own playlists.


## TO-DO:  
- [ ] write method to compare video comparison (like title/description changes)
- [ ] implement an ignore column in the Videos Database table or write a delete method
- [ ] implement business logic to count active/missing values in playlist
