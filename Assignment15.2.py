import sqlite3

conn = sqlite3.connect('iTunedb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
) ;
CREATE TABLE Genre(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);
CREATE TABLE Album(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
artist_id INTEGER,
title TEXT UNIQUE
);

CREATE TABLE Track(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE,
album_id INTEGER,
genre_id INTEGER,
length INTEGER,
rating INTEGER,
count INTEGER
);
''')

handle = open('tracks.csv')
for line in handle:
    line = line.strip()
    if len(line) < 8: continue
    pieces = line.split(',')
    songname = pieces[0]
    artistname = pieces[1]
    albumtitle = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]
    #other = pieces[7]

    cur.execute(' INSERT OR IGNORE INTO Artist(name) VALUES(?)', (artistname,))
    cur.execute('SELECT id FROM Artist WHERE name=?',(artistname,))
    artist_id = cur.fetchone()[0]

    cur.execute(' INSERT OR IGNORE INTO Album(title, artist_id) VALUES(?,?)', (albumtitle,artist_id))
    cur.execute('SELECT id FROM Album WHERE title=?',(albumtitle,))
    album_id = cur.fetchone()[0]

    cur.execute(' INSERT OR IGNORE INTO Genre(name) VALUES(?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name=?',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track(title,album_id,genre_id,length,rating,count) VALUES(?,?,?,?,?,?)''',
    (songname, album_id,genre_id,rating,length,count))
conn.commit()

    #print(songname, artistname, albumname, count, rating, length, genre)
