import sqlite3

conn = sqlite3.connect("trackdb01.sqlite")
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
    );

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
            len INTEGER,
            rating INTEGER,
            count INTEGER
    );
''')

fh = open("tracks.csv")

for line in fh:
    parts = line.split(',')
    track_title =parts[0]
    artist_name = parts[1]
    album_title = parts[2]
    count = parts[3]
    rating = parts[4]
    length = parts[5]
    genre = parts[6]

#    print(track_title,artist_name,album_title,count,rating,length,genre)

    cur.execute('INSERT OR IGNORE INTO Artist(name) VALUES (?)',(artist_name,))
    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)',(genre,))
    cur.execute('SELECT id FROM Artist WHERE name =?', (artist_name,))
    art_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Album(artist_id,title) VALUES(?,?)',(art_id,album_title))
    cur.execute('SELECT id FROM Album WHERE title=?',(album_title,))
    alb_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Genre WHERE name =?',(genre,))
    gn_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Track(title,album_id,genre_id,len,rating,count) VALUES(?,?,?,?,?,?)',(track_title,alb_id,gn_id,length,rating,count))
conn.commit()
