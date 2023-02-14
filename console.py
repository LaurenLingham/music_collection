from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Biffy Clyro")
artist_repository.save(artist_1)
artist_2 = Artist("Eminem")
artist_repository.save(artist_2)
artist_3 = Artist("Elton John")
artist_repository.save(artist_3)

album_1 = Album(artist_1, "Opposites", "Rock")
album_repository.save(album_1)
album_2 = Album(artist_1, "Blackened Sky", "Rock")
album_repository.save(album_2)
album_3 = Album(artist_2, "Revival", "Rap")
album_repository.save(album_3)
album_4 = Album(artist_3, "Too Low for Zero", "Pop")
album_repository.save(album_4)

breakpoint()