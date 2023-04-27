import re
from abc import ABC, abstractmethod


# Задания 1 и 2
# 1)
# Создать базовый класс Фигура с методом для подсчета площади. Создать производные классы: прямоугольник, круг,
# прямоугольный треугольник, трапеция со своими методами для подсчета площади.

# 2)
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает информацию
# о фигуре).

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __int__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f'{self.__class__.__name__} with an area of {self.area()} square units'


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f'{self.__class__.__name__} with an area of {self.area()} square units'


class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f'{self.__class__.__name__} with an area of {self.area()} square units'


class Trapezoid(Figure):
    def __init__(self, side_a, side_b, height):
        self.side_a = side_a
        self.side_b = side_b
        self.height = height

    def area(self):
        return self.height / 2 * (self.side_a + self.side_b)

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f'{self.__class__.__name__} with an area of {self.area()} square units'


rectangle = Rectangle(10, 5)
circle = Circle(7)
r_triangle = RightTriangle(15, 9)
trapezoid = Trapezoid(8, 14, 6)

figures = [rectangle, circle, r_triangle, trapezoid]
for fig in figures:
    print(fig.area())
    print(int(fig))
    print(fig)
    print('***************')


# Задание 3
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
#
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника со сторонами,
# параллельными осям координат, и размерами этого прямоугольника.
#
# Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о каждой из фигур.

class Shape(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class Square(Shape):
    def __init__(self, x, y, side):
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(side, int):
            raise ValueError('Invalid data type')
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(f'{self.__class__.__name__} {self.side}x{self.side}\n'
              f'at x: {self.x}, y: {self.y}\n')

    def save(self):
        with open('shapes.txt', 'a', encoding='UTF-8') as file:
            file.writelines(f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, side: {self.side}}}\n')

    def load(self):
        with open('shapes.txt', 'r', encoding='UTF-8') as file:
            text = file.readlines()
            try:
                for line in text:
                    if line.startswith(self.__class__.__name__):
                        self.x = int(re.search(f'x:\s\d+', line).group(0)[3:])
                        self.y = int(re.search(f'y:\s\d+', line).group(0)[3:])
                        self.side = int(re.search(f'side:\s\d+', line).group(0)[6:])
                        return f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, side: {self.side}}}'
            except AttributeError:
                print(f'Failed to read file {file.name} due to invalid data type or format')
                return 'no data'


class Rectangle(Shape):
    def __init__(self, x, y, length, width):
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(length, int) or \
                not isinstance(width, int):
            raise ValueError('Invalid data type')
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def show(self):
        print(f'{self.__class__.__name__} {self.length}x{self.width}\n'
              f'at x: {self.x}, y: {self.y}\n')

    def save(self):
        with open('shapes.txt', 'a', encoding='UTF-8') as file:
            file.writelines(f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, '
                            f'length: {self.length}, width: {self.width}}}\n')

    def load(self):
        with open('shapes.txt', 'r', encoding='UTF-8') as file:
            text = file.readlines()
            try:
                for line in text:
                    if line.startswith(self.__class__.__name__):
                        self.x = int(re.search(f'x:\s\d+', line).group(0)[3:])
                        self.y = int(re.search(f'y:\s\d+', line).group(0)[3:])
                        self.length = int(re.search(f'length:\s\d+', line).group(0)[8:])
                        self.width = int(re.search(f'width:\s\d+', line).group(0)[7:])
                        return f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, ' \
                               f'length: {self.length}, width: {self.width}}}'
            except AttributeError:
                print(f'Failed to read file {file.name} due to invalid data type or format')
                return 'no data'


class Circle(Shape):
    def __init__(self, x, y, radius):
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(radius, int):
            raise ValueError('Invalid data type')
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f'{self.__class__.__name__} with a radius of {self.radius}\n'
              f'at x: {self.x}, y: {self.y}\n')

    def save(self):
        with open('shapes.txt', 'a', encoding='UTF-8') as file:
            file.writelines(f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, radius: {self.radius}}}\n')

    def load(self):
        with open('shapes.txt', 'r', encoding='UTF-8') as file:
            text = file.readlines()
            try:
                for line in text:
                    if line.startswith(self.__class__.__name__):
                        self.x = int(re.search(f'x:\s\d+', line).group(0)[3:])
                        self.y = int(re.search(f'y:\s\d+', line).group(0)[3:])
                        self.radius = int(re.search(f'radius:\s\d+', line).group(0)[8:])
                        return f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, radius: {self.radius}}}'
            except AttributeError:
                print(f'Failed to read file {file.name} due to invalid data type or format')
                return 'no data'


class Ellipse(Shape):
    def __init__(self, x, y, length, width):
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(length, int) or \
                not isinstance(width, int):
            raise ValueError('Invalid data type')
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def show(self):
        print(f'{self.__class__.__name__} {self.length}x{self.width}\n'
              f'at x: {self.x}, y: {self.y}\n')

    def save(self):
        with open('shapes.txt', 'a', encoding='UTF-8') as file:
            file.writelines(f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, '
                            f'length: {self.length}, width: {self.width}}}\n')

    def load(self):
        with open('shapes.txt', 'r', encoding='UTF-8') as file:
            text = file.readlines()
            try:
                for line in text:
                    if line.startswith(self.__class__.__name__):
                        self.x = int(re.search(f'x:\s\d+', line).group(0)[3:])
                        self.y = int(re.search(f'y:\s\d+', line).group(0)[3:])
                        self.length = int(re.search(f'length:\s\d+', line).group(0)[8:])
                        self.width = int(re.search(f'width:\s\d+', line).group(0)[7:])
                        return f'{self.__class__.__name__} = {{x: {self.x}, y: {self.y}, ' \
                               f'length: {self.length}, width: {self.width}}}'
            except AttributeError:
                print(f'Failed to read file {file.name} due to invalid data type or format')
                return 'no data'


square = Square(5, 8, 12)
rectangle = Rectangle(6, 11, 12, 5)
circle = Circle(3, 5, 9)
ellipse = Ellipse(7, 3, 10, 6)

shapes = [square, rectangle, circle, ellipse]
shapes_info = []

for shape in shapes:
    shape.save()
    shapes_info.append(shape.load())
    shape.show()
    print('=================')

print(*shapes_info, sep='\n')
