class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.add_to_genres(genre)
        Song.add_to_artist(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # @classmethod
    # def add_song_to_count(cls,song):
    #     cls.count.append(song)
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_artist(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Empire State of Mind", "Jay-Z", "Rap")
song3 = Song("Halo", "Beyoncé", "Pop")

print(ninety_nine_problems.name)
print(ninety_nine_problems.artist)
print(ninety_nine_problems.genre)

print(Song.count)                    
print(Song.genres)                  
print(Song.artists)                  
print(Song.genre_count)
print(Song.genre_count)

print(ninety_nine_problems.__dict__)
print(song2.__dict__)
print(song3.__dict__)