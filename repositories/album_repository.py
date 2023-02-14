from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (artist_id, title, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.artist.id, album.title, album.genre]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * from albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row["artist_id"])
        album = Album(artist, row["title"], row["genre"], row["id"])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.select(result["artist_id"])
        album = Album(artist, result["title"], result["genre"], result["id"])
    return album

def update(album):
    sql = "UPDATE albums set (artist_id, title, genre) = (%s, %s, %s, %s) WHERE id = %s"
    values = [album.artist.id, album.title, album.genre, album.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE ID = %s"
    values = [id]
    run_sql(sql, values)
