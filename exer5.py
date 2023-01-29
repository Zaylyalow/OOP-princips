"""
Перед вами программа, которая умеет высчитывать расстояние от одной точки на карте до другой.
В коде описан класс Point (точка на карте), у него есть свойства — широта и долгота, 
и метод distance(self, other) — это расстояние между двумя точками в километрах 
(параметр other должен получить другой объект Point).
Создайте два класса-наследника класса Point:
City(Point, name, population) описывает город, в конструктор передаются координаты 
города (объект класса Point), его название и численность населения;
Mountain(Point, name, height) описывает гору, в конструктор передаются координаты горы 
(объект класса Point), её название и высота в метрах.
Ваша задача — вывести на экран расстояние от Москвы до Эвереста.
"""
# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
        self.longitude - other.longitude)

        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population 
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height
        
    def show(self):
        print(f"Высота горы {self.name} - {self.height} м.")
    
    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    # и добавьте свойства name и height

    # Создайте метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."


# эта функция печатает расстояние
# между двумя любыми наследниками класса Point
def print_how_far(geo_object_1, geo_object_2):
    print(f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}» — {geo_object_1.distance(geo_object_2)} км.')


# основной код
moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)

moscow.show()
everest.show()
print_how_far(moscow, everest)
print_how_far(moscow, chelyabinsk)