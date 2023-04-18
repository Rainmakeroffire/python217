# Задание 1
# Создайте класс Device, который содержит информацию об устройстве. С помощью механизма наследования, реализуйте класс
# класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке). Каждый из классов
# должен содержать необходимые для работы методы.

from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, model, manufacturer, production_year):
        self.model = model
        self.manufacturer = manufacturer
        self.production_year = production_year

    @abstractmethod
    def name(self):
        pass

    def view_specs(self):
        print(f'Device: {self.name}\n'
              f'Model: {self.model}\n'
              f'Manufacturer: {self.manufacturer}\n'
              f'Year of production: {self.production_year}')


class Blender(Device):
    def __init__(self, model, manufacturer, production_year, output, dev_type, volume):
        super().__init__(model, manufacturer, production_year)
        self.output = output
        self.dev_type = dev_type
        self.volume = volume

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def view_specs(self):
        super().view_specs()
        print(f'Power output: {self.output}W\n'
              f'Type: {self.dev_type}\n'
              f'Volume: {self.volume} liters\n')


class MeatGrinder(Device):
    def __init__(self, model, manufacturer, production_year, output, noise_lvl, control):
        super().__init__(model, manufacturer, production_year)
        self.output = output
        self.noise_lvl = noise_lvl
        self.control = control

    @property
    def name(self):
        return self.__class__.__name__.lower()

    def view_specs(self):
        super().view_specs()
        print(f'Power output: {self.output}W\n'
              f'Noise level: {self.noise_lvl}dB\n'
              f'Control: {self.control}\n')


Polaris_PHB = Blender('PHB 1476', 'Polaris', 2022, 1400, 'submersible', 0.5)
Polaris_PHB.view_specs()

Kitfort_KT = MeatGrinder('КТ-2108', 'Kitfort', 2023, 1800, 82, 'mechanical')
Kitfort_KT.view_specs()


# Задание 2
# Создайте класс Ship, который содержит информацию о корабле. С помощью механизма наследования, реализуйте класс Frigate
# (содержит информацию о фрегате), класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию
# о крейсере).Каждый из классов должен содержать необходимые для работы методы.

class Ship(ABC):
    def __init__(self, name, displacement, launching_year):
        self.name = name
        self.displacement = displacement
        self.launching_year = launching_year

    @abstractmethod
    def ship_type(self):
        pass

    def view_specs(self):
        print(f'Type: {self.ship_type}\n'
              f'Name: {self.name}\n'
              f'Displacement: {self.displacement} tons\n'
              f'Year of launching: {self.launching_year}')


class Frigate(Ship):
    def __init__(self, name, displacement, launching_year, fr_class, subclass):
        super().__init__(name, displacement, launching_year)
        self.fr_class = fr_class
        self.subclass = subclass

    @property
    def ship_type(self):
        return self.__class__.__name__.lower()

    def view_specs(self):
        super().view_specs()
        print(f'Class: {self.fr_class}\n'
              f'Subclass: {self.subclass}\n')


class Destroyer(Ship):
    def __init__(self, name, displacement, launching_year, escort, intelligence):
        super().__init__(name, displacement, launching_year)
        self.escort = escort
        self.intelligence = intelligence

    @property
    def ship_type(self):
        return self.__class__.__name__.lower()

    def view_specs(self):
        super().view_specs()
        print(f'Involved in escort activities: {self.escort}\n'
              f'Involved in intelligence activities: {self.intelligence}\n')


class Cruiser(Ship):
    def __init__(self, name, displacement, launching_year, max_fighters_onboard, missile_launcher_type):
        super().__init__(name, displacement, launching_year)
        self.max_fighters_onboard = max_fighters_onboard
        self.missile_launcher_type = missile_launcher_type

    @property
    def ship_type(self):
        return self.__class__.__name__.lower()

    def view_specs(self):
        super().view_specs()
        print(f'Maximum fighters carried onboard: {self.max_fighters_onboard}\n'
              f'Missile launcher type: {self.missile_launcher_type}\n')


La_Fayette = Frigate('La Fayette', 3200, 1992, 'II', 'DLG')
La_Fayette.view_specs()

Bezuprechny = Destroyer('Bezuprechny', 6600, 1986, True, False)
Bezuprechny.view_specs()

A_Kuznetsov = Cruiser('Admiral Kuznetsov', 46540, 1985, 40, '4К-80')
A_Kuznetsov.view_specs()


# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами. В классе должны быть
# предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и поле для хранения копеек (центы,
# евроценты, копейки и т.д.). Реализовать методы для вывода суммы на экран, задания значений для частей.

class Money(ABC):
    def __init__(self, amount, sub_amount):
        self.amount = amount
        self.sub_amount = sub_amount

    @abstractmethod
    def currency(self):
        pass

    @abstractmethod
    def sub_currency(self):
        pass

    def display(self):
        print(f'Available amount: {self.amount} {self.currency} {self.sub_amount} {self.sub_currency}')

    def reset(self):
        while True:
            value = input(f'Enter new amount, {self.currency}: ')
            if value.isdigit():
                self.amount = int(value)
                break
            else:
                print('Incorrect input. Digits only')
        while True:
            value = input(f'Enter new amount, {self.sub_currency}: ')
            if value.isdigit() and (len(value) == 1 or len(value) == 2):
                self.sub_amount = int(value)
                break
            else:
                print('Incorrect input. Digits only (range: 1-99)')


class RUB(Money):
    @property
    def currency(self):
        return 'RUB'

    @property
    def sub_currency(self):
        return 'kopeks'


class EUR(Money):
    @property
    def currency(self):
        return 'EUR'

    @property
    def sub_currency(self):
        return 'cents'


class USD(Money):
    @property
    def currency(self):
        return 'USD'

    @property
    def sub_currency(self):
        return 'cents'


rub = RUB(1500, 32)
rub.display()
rub.reset()
rub.display()

eur = EUR(1000, 25)
eur.display()
eur.reset()
eur.display()

usd = USD(800, 0)
usd.display()
usd.reset()
usd.display()
