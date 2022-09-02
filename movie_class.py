class Movie:
    genre = ''

    def __init__(self, name, director, year):
        self.name = name
        self.director = director
        self.year = year

    def has_genre(self):
        return len(self.genre) > 0

my_movie = Movie('Batman', 'Christopher Nolan', 2008)
my_movie.genre = 'Thriller'

print(my_movie.has_genre())
