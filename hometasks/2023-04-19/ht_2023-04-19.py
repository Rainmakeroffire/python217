# Задание 1
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей (операция ==);
# ■ Сравнения длин двух окружностей (операции >, <, <=,>=);
# ■ Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.__area = radius ** 2 * 3.14
        self.__length = 2 * 3.14 * radius

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.radius = (value / 3.14) ** 0.5
        self.__area = self.radius ** 2 * 3.14

    @area.deleter
    def area(self):
        raise Exception('One does not simply delete the circle area')

    def __str__(self):
        return f'Circle area: {self.__area}\nCircle radius: {self.radius}\n'

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.__length > other.__length

    def __lt__(self, other):
        return self.__length < other.__length

    def __le__(self, other):
        return self.__length <= other.__length

    def __ge__(self, other):
        return self.__length >= other.__length

    def __add__(self, other):
        self.radius += other
        self.__area = self.radius ** 2 * 3.14
        return self

    def __sub__(self, other):
        self.radius -= other
        self.__area = self.radius ** 2 * 3.14
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)


a = Circle(5)
b = Circle(3)
print(a)
a += 10
print(a)
a -= 3
print(a)
print(a + 20)
print(a - 20)
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# Задание 2
# Создайте класс Complex (комплексное число). Более подробно ознакомиться с комплексными числами можно по ссылке.
# Создайте перегруженные операторы для реализации арифметических операций для по работе с комплексными числами
# (операции +, -, *, /).

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__i = -1

    @property
    def z(self):
        return self.a + (self.b * self.__i)

    def __str__(self):
        return f'{self.z}'

    def __add__(self, other):
        return self.a + other.a + (self.b + other.b) * self.__i

    def __sub__(self, other):
        return self.a - other.a + (self.b - other.b) * self.__i

    def __mul__(self, other):
        return (self.a * other.a - self.b * other.b) + (self.a * other.b + other.a * self.b) * self.__i

    def __truediv__(self, other):
        return (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2) + (
                (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)) * self.__i


com_1 = Complex(3, 6)
com_2 = Complex(4, 10)

print(com_1 + com_2)
print(com_1 - com_2)
print(com_1 * com_2)
print(com_1 / com_2)


# Задание 3
# Вам необходимо создать класс Airplane (самолет). С помощью перегрузки операторов организовать:
# ■ Проверка на равенство типов самолетов (операция ==);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).

class Airplane:
    def __init__(self, name, manufacturer, haul_type, decks, capacity, pass_onboard):
        self.name = name
        self.manufacturer = manufacturer
        self.haul_type = haul_type
        self.decks = decks
        self.capacity = capacity
        self.pass_onboard = pass_onboard

    def __str__(self):
        return f'Aircraft: {self.manufacturer} {self.name}\n' \
               f'Haul Type: {self.haul_type}\n' \
               f'Decks: {self.decks}-decker\n' \
               f'Capacity: {self.capacity} passengers\n' \
               f'Passengers Onboard: {self.pass_onboard} passengers\n'

    def __eq__(self, other):
        return self.haul_type == other.haul_type

    def __add__(self, other):
        self.pass_onboard += other
        return self

    def __sub__(self, other):
        self.pass_onboard -= other
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity


Boeing_747 = Airplane('747', 'Boeing', 'LH', 'double', 366, 330)
Airbus_A320 = Airplane('A320', 'Airbus', 'MH', 'single', 220, 198)
print(Boeing_747, Airbus_A320, sep='\n')

print(Boeing_747 + 15)
print(Airbus_A320 - 3)

print(Boeing_747 == Airbus_A320)
print(Boeing_747 > Airbus_A320)
print(Boeing_747 < Airbus_A320)
print(Boeing_747 >= Airbus_A320)
print(Boeing_747 <= Airbus_A320)


# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, type, area, price, address):
        self.type = type
        self.area = area
        self.price = price
        self.address = address


    def __str__(self):
        return f'A {self.type} flat located at {self.address}\n' \
               f'Area: {self.area} m2\n' \
               f'Price: ${self.price}\n'

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


studio = Flat('studio', 25, 100000, '1050 Rue du Tabellion 10, Brussels, Belgium')
two_bedroom = Flat('two-bedroom', 52, 350000, '75007 11 Rue Chevert, Paris, France')
print(studio, two_bedroom, sep='\n')

print(studio == two_bedroom)
print(studio != two_bedroom)
print(studio > two_bedroom)
print(studio < two_bedroom)
print(studio >= two_bedroom)
print(studio <= two_bedroom)
