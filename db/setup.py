import sqlite3

fp = r"./db/database.db"

con = sqlite3.connect(fp)


con.execute("DROP TABLE IF EXISTS playlists")
con.execute(""" CREATE TABLE IF NOT EXISTS playlists (
                pl_id VARCHAR(255) NOT NULL PRIMARY KEY,
                title VARCHAR(255),
                last_checked DATETIME,
                count_active INTEGER,
                count_missing INTEGER
                )
""")


con.execute("DROP TABLE IF EXISTS videos")
con.execute(""" CREATE TABLE IF NOT EXISTS videos (

                video_pl_id VARCHAR(255) NOT NULL PRIMARY KEY,

                id VARCHAR(255) NOT NULL,
                title VARCHAR(255) NOT NULL,
                description VARCHAR(255),
                thumbnail VARCHAR(255),
                channel  VARCHAR(255) NOT NULL,
                channel_id VARCHAR(255) NOT NULL,

                pl_id VARCHAR(255) NOT NULL,
                pl_position INTEGER NOT NULL,

                last_checked DATETIME,
                active INTEGER,
                missing INTEGER,

                ignore BOOLEAN DEFAULT FALSE,

                FOREIGN KEY (pl_id) REFERENCES playlists(id)
                )
""")