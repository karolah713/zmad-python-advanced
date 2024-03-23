#Zadanie 3. Napisz klasę Vector2D, która będzie reprezentować wektor dwuwymiarowy. Klasa powinna zawierać metody
# magiczne __add__ oraz __radd__, aby umożliwić dodawanie dwóch wektorów 2D oraz dodawanie krotek (x, y) do wektorów.

class Vector2D:

    def __init__(self, x, y):
        self.x = x if isinstance(x, int) else 0
        self.y = y if isinstance(y, int) else 0

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Vector2D(self.x + other[0], self.y + other[1])

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f'({self.x}, {self.y})'


v1 = Vector2D(2,4)
v2 = Vector2D(3,5)
print(v1)

# Dodawanie dwóch wektorów 2D
print(v1 + v2)

# Dodawanie tupla
print(v1 + (7,8))

print((4, 4) + v2)
