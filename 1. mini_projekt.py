# Zadanie 1. Stwórz klasę Time zajmującą się obsługą czasu. Dodaj w niej dwa pola (zmienna) o nazwie hour i minute do przechowywania
# godzin i minut. W klasie dodaj następujące metody:
# - funkcja, która zwraca wartość logiczną sprawdzającą czy zawartość pól może być poprawną godziną w formacie 24-godzinnym
# - funkcja, która odpowiada za dodawanie dwóch obiektów typu Time. W środku należy dodać godziny do godzin, minuty do minuty.
#   Jeśli minuty są większe lub równe niż 60, to należy odpowiednie zwiększyć pole godzin i pomniejszyć o 60 minuty. Jeśli godziny są
#   większe lub równe niż 24, to należy od godzin odjąć 24. Funkcja ma zwrócić obiekt typu Time przechowujący “sumę”.
# - dodaj odpowiednią metodę, która odpowiada za sortowanie obiektów typu Time (wg dowolnego wybranego przez siebie klucza)
# Następnie stwórz co najmniej 3 obiekty i wywołaj na nich każdą z funkcji co najmniej 1 raz.

class Time:

    def __init__(self, hour, minute):
        self.hour = hour if isinstance(hour,int) else 0
        self.minute = minute if isinstance(minute,int) else 0

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    def check_if_time_correct(self):
        if 0 <= self.hour < 24:
            if 0 <= self.minute <= 60:
                return self.__str__()
        else:
            return False

    def add_time(self, h, m):
        new_hour = self.hour + h
        new_min = self.minute + m
        print(f'new_hour: {new_hour}, new_min: {new_min}')

        # Adjust minutes and hours if minutes>=60
        if new_min >= 60:
            new_hour += new_min // 60
            new_min %= 60
        if new_hour >= 24:
            new_hour %= 24
        self.hour = new_hour
        self.minute = new_min
        print(f'new_hour: {new_hour}, new_min: {new_min}')
        return f'{new_hour}:{new_min}'

    def __lt__(self, other):
        if isinstance(other, Time):
            return (self.hour, self.minute) < (other.hour, other.minute)
        

t1 = Time(4,50)
print(f'Time t1: {t1}')

t2 = Time(44,30)
print(f'Time t2: {t2}')
print(t2.check_if_time_correct())

t3 = Time(23,30)
print(f'Time t3: {t3}')

t4 = Time(23,50)
print(f'Time t4: {t4}')
t4.add_time(0,50)
print(f'Time t4: {t4}')
t4.add_time(1,25)
print(f'Time t4: {t4}')
t4.add_time(1,125)
print(f'Time t4: {t4}')

print(t1 > t3)

times = [t1, t2, t3, t4] # List of Time objects
valid_times = [time for time in times if time.check_if_time_correct()] # List comprehension
print([str(time) for time in valid_times])
valid_times.sort()
print([str(time) for time in valid_times])

