# Zadanie 6. Napisz klasę Car, która będzie reprezentować samochód. Klasa powinna zawierać atrybuty instancyjne make, model, year,
# mileage oraz price, inicjalizator, właściwości dla mileage oraz price (umożliwiające odczyt i zapis z walidacją wartości)
# oraz metody magiczne __str__ i __repr__. Dodatkowo, klasa powinna posiadać metody drive (aktualizującą przebieg samochodu)
# oraz calculate_depreciation (obliczającą spadek wartości samochodu na podstawie jego przebiegu i wieku).

import datetime


class Car:

    def __init__(self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = year if isinstance(year, int) else 0
        self.__mileage = mileage if isinstance(mileage, int) else 0
        self.__price = price if isinstance(price, float) else float(price)

    def __str__(self):
        return f"Car: {self.make} {self.model} from {self.year}, mileage: {self.__mileage} km, price: {self.__price} PLN"

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, mileage={self.__mileage} km, year={self.year}, price={self.__price} PLN"

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, val):
        if val >= 0:
            self.__mileage = val
        else:
            raise ValueError("Please provide positive value")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if val >= 0:
            self.__price = float(val)
        else:
            raise ValueError("Please provide positive value")

    def drive(self, dist):
        self.__mileage += dist
        # return self._mileage

    def calculate_depreciation(self, initial_mileage):
        per_mile = 0.1
        per_year = 1500
        current_year = datetime.date.today().year
        age_diff = current_year - self.year
        depreciation = (self.mileage - initial_mileage)*per_mile + age_diff*per_year
        self.__price -= depreciation
        return self.__price


c1 = Car('Honda', 'Civic', 2000, 124000, 88000)
print(c1)
print(c1.mileage)
c1.set_mileage = 126000
print(c1.mileage)
c1.drive(500)
print(c1.mileage)
print(c1.calculate_depreciation(124000))







