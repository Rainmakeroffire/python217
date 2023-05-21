# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте работу созданного класса.

class Bike:
    def __init__(self):
        self.cross_country = False
        self.downhill = False
        self.free_ride = False
        self.attachments = []
        self.suspension = []

    def __str__(self):
        string = ""
        if self.cross_country:
            string += f"CROSS COUNTRY BIKE\n"
        if self.downhill:
            string += f"DOWNHILL BIKE\n"
        if self.free_ride:
            string += f"FREE RIDE BIKE\n"
        else:
            string += "BIKE\n"
        if self.attachments:
            string += "Attachments installed:\n"
        for module in self.attachments:
            string += "- " + str(module) + "\n"
        if self.suspension:
            string += "Suspension system installed:\n"
        for system in self.suspension:
            string += "- " + str(system) + "\n"
        return string


class Shifter:
    def __str__(self):
        return "shifter"


class Wheels:
    def __str__(self):
        return "wheels"


class HandleBar:
    def __str__(self):
        return "handle bar"


class Pedals:
    def __str__(self):
        return "pedals"


class Mirror:
    def __str__(self):
        return "rear view mirror"


class Seat:
    def __str__(self):
        return "seat"


class HardtailSuspensionSystem:
    def __str__(self):
        return "hardtail"


class FullSuspensionSystem:
    def __str__(self):
        return "full suspension"


from abc import ABC, abstractmethod


class BikeDesigner(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def mount_attachments(self):
        pass

    @abstractmethod
    def mount_suspension(self):
        pass


class BikeAssembler(BikeDesigner):
    def __init__(self):
        self.product = Bike()

    def reset(self):
        self.product = Bike()

    def get_product(self):
        return self.product

    def mount_attachments(self):
        self.product.free_ride = True
        self.product.attachments.append(Wheels())
        self.product.attachments.append(HandleBar())

    def mount_suspension(self):
        self.product.suspension.append(FullSuspensionSystem())


assembler = BikeAssembler()
assembler.mount_attachments()
assembler.mount_suspension()
print(assembler.get_product())


# Задание 2
# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

from abc import ABC, abstractmethod


class Pasta(ABC):
    @abstractmethod
    def add_pasta(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_toppings(self):
        pass

    @abstractmethod
    def add_additives(self):
        pass


class Carbonara(Pasta):
    def __init__(self):
        self.pasta = 'spaghetti'
        self.sauce = 'cream sauce'
        self.toppings = ['yolks', 'bacon']
        self.additives = ['parsley', 'parmesan', 'garlic']

    def add_pasta(self):
        return self.pasta

    def add_sauce(self):
        return self.sauce

    def add_toppings(self):
        return self.toppings

    def add_additives(self):
        return self.additives


class Alfredo(Pasta):
    def __init__(self):
        self.pasta = 'fettuccine'
        self.sauce = 'mushroom sauce'
        self.toppings = ['champignons', 'chicken']
        self.additives = ['parsley', 'parmesan', 'cream']

    def add_pasta(self):
        return self.pasta

    def add_sauce(self):
        return self.sauce

    def add_toppings(self):
        return self.toppings

    def add_additives(self):
        return self.additives


class Marinara(Pasta):
    def __init__(self):
        self.pasta = 'penne'
        self.sauce = 'wine vinegar'
        self.toppings = ['shrimps', 'mussels']
        self.additives = ['basil', 'oregano', 'parmesan']

    def add_pasta(self):
        return self.pasta

    def add_sauce(self):
        return self.sauce

    def add_toppings(self):
        return self.toppings

    def add_additives(self):
        return self.additives


class Kitchen:
    def __init__(self):
        self.pasta = None
        self.order = input('Which pasta would you like to order?\n')
        if self.order.lower() in ['carbonara', 'alfredo', 'marinara']:
            class_name = self.order.capitalize()
            if class_name in globals():
                self.pasta = globals()[class_name]()
                print("", self.cook_pasta(), sep='\n')
            else:
                raise ValueError('Sadly, we cannot cook this type of pasta')
        else:
            raise ValueError('Invalid pasta choice')

    def cook_pasta(self):
        if self.pasta:
            toppings = ''
            additives = ''
            for topping in self.pasta.add_toppings():
                toppings += "- " + topping + "\n"
            for additive in self.pasta.add_additives():
                additives += "- " + additive + "\n"
            return f'Your order: {self.pasta.__class__.__name__}\n' \
                   f'Description: {self.pasta.add_pasta().capitalize()} with {self.pasta.add_sauce()}\n' \
                   f'Toppings:\n{toppings}' \
                   f'Additives:\n{additives}'
        else:
            return 'No pasta ordered'


order = Kitchen()


# Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.

import copy
from abc import ABCMeta, abstractmethod


class Courses(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Python(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Python Course"

    def course(self):
        print("Inside Python::course() method")


class JS(Courses):
    def __init__(self):
        super().__init__()
        self.type = "JavaScript Course"

    def course(self):
        print("Inside JS::course() method.")


class GoLang(Courses):
    def __init__(self):
        super().__init__()
        self.type = "GoLang Course"

    def course(self):
        print("Inside GoLang::course() method.")


class CoursesCache:
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = CoursesCache.cache.get(sid, None)
        return COURSE.clone()

    @staticmethod
    def load():
        python = Python()
        python.set_id("1")
        CoursesCache.cache[python.get_id()] = python

        js = JS()
        js.set_id("2")
        CoursesCache.cache[js.get_id()] = js

        golang = GoLang()
        golang.set_id("3")
        CoursesCache.cache[golang.get_id()] = golang


CoursesCache.load()

python = CoursesCache.get_course("1")
print(python.get_type())

js = CoursesCache.get_course("2")
print(js.get_type())

golang = CoursesCache.get_course("3")
print(golang.get_type())
