# Zadanie 2. Stwórz klasę Movie z polami przechowującymi tytuł, rok oraz ocenę filmu. Dodaj w klasie konstruktor
# (metodę __init__) ustawiającą wszystkie pola tej klasy.
# Następnie stwórz listę zawierającą co najmniej 10 obiektów tego typu. Posortuj listę wg różnych klucz na co najmniej 5 różnych
# sposobów. W komentarzach umieść informację o zasadach sortowania.

class Movie:

    def __init__(self, title, year, score):
        self.title = title if isinstance(title, str) else ''
        self.year = year if isinstance(year,int) else '2000'
        self.score = score if isinstance(score, float) else '0'

    def __repr__(self):
        return f"Title = {self.title} | year = {self.year} | score = {self.score}"

    def __lt__(self, other):
        if isinstance(other,Movie):
            return (self.year, self.score) < (other.year, other.score)

m1 = Movie('Pulp Fiction', 1994, 8.9)
m2 = Movie('The Godfather', 1972, 9.2)
m3 = Movie("Schindler's List", 1994, 9.0)
m4 = Movie('Forrest Gump', 1994, 8.8)
m5 = Movie('The Matrix', 1999, 8.7)
m6 = Movie('The Silence of the Lambs', 1991, 8.7)
m7 = Movie('The Green Mile', 1999, 8.5)
m8 = Movie('Back to the Future', 1985, 8.5)
m9 = Movie('Casablanca', 1942, 8.5)
m10 = Movie('The Pianist', 2002, 8.4)

movies = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
print(movies)
movies.sort() # Sorting in ascending order by year and then by score
print(movies)


m_by_title = sorted(movies, key=lambda x: x.title) # Sorting alphabetically by title
print(m_by_title)

m_by_score = sorted(movies, key=lambda x: x.score) # Sorting by score in ascending order
print(m_by_score)

m_by_score_desc = sorted(movies, key=lambda x: x.score, reverse=True) # Sorting by score in descending order
print(m_by_score_desc)

m_by_title_year = sorted(movies, key=lambda x: (x.year, x.title), reverse=True) # Sorting by title, then year in descending order
print(m_by_title_year)

m_by_year = sorted(movies, key=lambda x: x.year, reverse=True) # Sorting by year in descending order
print(m_by_year)
