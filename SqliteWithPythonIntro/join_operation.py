import sqlite3

conn = sqlite3.connect("database/chinook.db")

cursor = conn.cursor() # bağlantı oluşturduk
sorgu = " select albums.Title,artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId " # albums.Title(albums tablosundan) ve artists.Name al(artists tablosundan) ve burada artists.ArtistId ile albums.ArtistsId eşitle
cursor.execute(sorgu) # sorguyu çalıştırdık
for data in cursor:
    print("Title = {}\tName = {}".format(data[0],data[1]))

conn.close() # bağlantıyı kapattık