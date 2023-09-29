class Song:

    count =0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count ={}
        for genre in cls.genres:
            count = sum(1 for song in cls.all_songs() if song.genre == genre)
            cls.genre_count[genre] = count

    @classmethod
    def add_to_artist_count(cls): 
        cls.artist_count ={}
        for artist in cls.artists:
            count = sum(1 for song in cls.all_songs() if song.artist == artist)
            cls.artist_count[artist] = count

    @classmethod
    def all_songs(cls): 
        return [song for song in cls.__subclasses__()]

# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# another_song = Song("Song 2", "Blur", "Rock")
# yet_another_song = Song("Song 3", "Johnny Cash", "Country")
# Song.add_to_genre_count()
# print(Song.add_to_artist_count())

# print(Song.genre_count) 
# print(Song.artist_count) 

song1 = Song("Song 1", "Artist 1", "Pop")
song2 = Song("Song 2", "Artist 2", "Rock")
song3 = Song("Song 3", "Artist 3", "Hip Hop")
print(Song.count)