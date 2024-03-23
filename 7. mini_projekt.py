# Zadanie 7. Napisz klasę Samochod, która będzie mieć następujące atrybuty instancyjne:
# marka - marka samochodu
# model - model samochodu
# rok_produkcji - rok produkcji samochodu
# przebieg - przebieg samochodu
# Klasa powinna mieć następujące metody:
# __init__(self, marka, model, rok_produkcji, przebieg) - konstruktor, który będzie inicjalizował atrybuty marka, model, rok_produkcji i przebieg
# __str__(self) - metoda magiczna, która będzie zwracać reprezentację napisową obiektu klasy Samochod
# __lt__(self, other) - metoda magiczna, która będzie porównywać dwa samochody po ich przebiegu. Metoda ma zwracać True,
# jeśli przebieg samochodu self jest mniejszy niż przebieg samochodu other, a w przeciwnym wypadku False.

class Samochod:

    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka if isinstance(marka, str) else ""
        self.model = model if isinstance(model, str) else ""
        self.rok_produkcji = rok_produkcji if isinstance(rok_produkcji, int) else int(rok_produkcji)
        self.przebieg = przebieg if isinstance(przebieg, int) else 0

    def __str__(self):
        return f"Samochód marki: {self.marka}, model: {self.model}, z przebiegiem: {self.przebieg}, rok produkcji: {self.rok_produkcji}"

    def __lt__(self, other):
        if isinstance(other, Samochod):
            return self.przebieg < other.przebieg


s1 = Samochod('Opel', 'Astra', 2018, 125000)
s2 = Samochod('Toyota', 'Yaris', 2021, 82000)
s3 = Samochod('Honda', 'Civic', 1999.0, '82K')
print(s1)
print(s3.przebieg)
print(s3)
print(s1 < s3)
