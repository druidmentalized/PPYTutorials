class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        
    def __str__(self) -> str:
        return f"Movie title: {self.title}, year: {self.year}"
    
    def __repr__(self) -> str:
        return f"Movie(title={self.title},year={self.year})"
    
# a)
movie_test = Movie("Inception", 2010)

# b) + c)
print(movie_test)
print(f"{movie_test=}")