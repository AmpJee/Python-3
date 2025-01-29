import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/song-db.db")

con.execute("CREATE TABLE songs (id INTEGER PRIMARY KEY, name TEXT, artist TEXT, album TEXT)")
con.execute("CREATE TABLE albums (id INTEGER PRIMARY KEY, name TEXT, artist TEXT, year INTEGER)")
con.execute("CREATE TABLE songs_on_albums (song_id INTEGER, album_id INTEGER)")

con.execute("INSERT INTO songs (name, artist, album) VALUES ('Espresso', 'Sabrina Carpenter', 'Short n'' Sweet')")
con.execute("INSERT INTO songs (name, artist, album) VALUES ('Please Please Please', 'Sabrina Carpenter', 'Short n'' Sweet')")
con.execute("INSERT INTO songs (name, artist, album) VALUES ('BMF', 'Sza', 'SOS Deluxe: LANA')")
con.execute("INSERT INTO songs (name, artist, album) VALUES ('I Hate U', 'SZA', 'SOS')")
con.execute("INSERT INTO songs (name, artist, album) VALUES ('PUSH 2 START', 'Tyla', 'TYLA+')")
con.execute("INSERT INTO songs (name, artist, album) VALUES ('Jump', 'Tyla', 'TYLA+')")

con.execute("INSERT INTO albums (name, artist, year) VALUES ('Short n'' Sweet', 'Sabrina Carpenter', 2024)")
con.execute("INSERT INTO albums (name, artist, year) VALUES ('SOS', 'Sza', 2023)")
con.execute("INSERT INTO albums (name, artist, year) VALUES ('TYLA+', 'Tyla', 2024)")

con.execute("INSERT INTO songs_on_albums (song_id, album_id) VALUES (1, 1)")
con.execute("INSERT INTO songs_on_albums (song_id, album_id) VALUES (2, 1)")
con.execute("INSERT INTO songs_on_albums (song_id, album_id) VALUES (3, 2)")
con.execute("INSERT INTO songs_on_albums (song_id, album_id) VALUES (4, 2)")
con.execute("INSERT INTO songs_on_albums (song_id, album_id) VALUES (5, 3)")
con.execute("INSERT INTO songs_on_albums (song_id, album_id) VALUES (6, 3)")

cursor = con.execute("SELECT * FROM songs WHERE artist = 'Sabrina Carpenter'")
print('Songs by Sabrina Carpenter:')
for row in cursor:
    print(row)

# (song, artist) from song in 2024 albums
cursor = con.execute("SELECT s.name, s.artist FROM songs s "
                     "JOIN songs_on_albums soc ON s.id = soc.song_id "
                     "JOIN albums a ON soc.album_id = a.id "
                     "WHERE a.year = 2024")
print('Songs by artists in 2024:')
for row in cursor:
    print(row)

con.commit()