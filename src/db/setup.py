import sqlite3

fp = r"./src/db/database.db"

con = sqlite3.connect(fp)


con.execute("DROP TABLE IF EXISTS playlists")

con.execute(""" CREATE TABLE IF NOT EXISTS playlists (
                id VARCHAR(255) NOT NULL PRIMARY KEY,
                title VARCHAR(255),
                created_at DATETIME NOT NULL,
                last_checked DATETIME
                )
""")


con.execute("DROP TABLE IF EXISTS videos")
con.execute(""" CREATE TABLE IF NOT EXISTS videos (

                id VARCHAR(255) NOT NULL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description VARCHAR(255),
                thumbnail VARCHAR(255),
                channel  VARCHAR(255) NOT NULL,
                channel_id VARCHAR(255) NOT NULL,

                pl_id VARCHAR(255) NOT NULL,
                pl_position INTEGER NOT NULL,

                video_pl_id VARCHAR(255) NOT NULL,


                FOREIGN KEY (pl_id) REFERENCES playlists(id)
                )
""")