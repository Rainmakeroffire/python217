import json
import pickle


# Задание 1
# К уже реализованному классу «Автомобиль» добавьте возможность упаковки и распаковки данных с использованием json и
# pickle.

class Auto:
    def __init__(self, model, manuf_year, automaker, engine_cc, color, price):
        self.model = model
        self.manuf_year = manuf_year
        self.automaker = automaker
        self.engine_cc = engine_cc
        self.color = color
        self.price = price

    def display(self):
        print(f'Model: {self.model}\n'
              f'Year of manufacture: {self.manuf_year}\n'
              f'Manufacturer: {self.automaker}\n'
              f'Engine displacement: {self.engine_cc} cc\n'
              f'Color: {self.color}\n'
              f'Price: ${self.price}\n')

    def data_input(self):
        self.model = input('Enter model: ')
        self.manuf_year = input('Enter year of manufacture: ')
        self.automaker = input('Enter manufacturer: ')
        self.engine_cc = input('Enter engine displacement: ')
        self.color = input('Enter color: ')
        self.price = input('Enter price, $: ')

    def dump_pickle(self):
        with open(input('Save object as (enter file name): '), 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle():
        with open(input('Enter file to open: '), 'rb') as file:
            return pickle.load(file)

    def dump_json(self):
        with open(input('Save object as (enter file name): '), 'w') as file:
            json.dump({self.__class__.__name__: self.__dict__}, file)

    @staticmethod
    def load_json():
        with open(input('Enter file to open: '), 'r') as file:
            loaded_obj = json.load(file)
            class_name = list(loaded_obj.keys())[0]
            obj_props = list(loaded_obj.values())[0]
            new_obj = globals()[class_name](**obj_props)
            return new_obj


Maserati_MC20 = Auto('MC20', '2020', 'Maserati', '2992', 'White', '215000')

Maserati_MC20.dump_pickle()
print(Maserati_MC20.load_pickle())
Maserati_MC20.dump_json()
print(Maserati_MC20.load_json())


# Задание 2
# К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных с использованием json и pickle.

class Book:
    def __init__(self, title, issue_year, publisher, genre, author, price):
        self.title = title
        self.issue_year = issue_year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display(self):
        print(f'Book title: {self.title}\n'
              f'Year of issue: {self.issue_year}\n'
              f'Publisher: {self.publisher}\n'
              f'Genre: {self.genre}\n'
              f'Author: {self.author}\n'
              f'Price: ${self.price}\n')

    def data_input(self):
        self.title = input('Enter book title: ')
        self.issue_year = input('Enter year of issue: ')
        self.publisher = input('Enter publisher: ')
        self.genre = input('Enter genre: ')
        self.author = input('Enter author: ')
        self.price = input('Enter price, $: ')

    def dump_pickle(self):
        with open(input('Save object as (enter file name): '), 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle():
        with open(input('Enter file to open: '), 'rb') as file:
            return pickle.load(file)

    def dump_json(self):
        with open(input('Save object as (enter file name): '), 'w') as file:
            json.dump({self.__class__.__name__: self.__dict__}, file)

    @staticmethod
    def load_json():
        with open(input('Enter file to open: '), 'r') as file:
            loaded_obj = json.load(file)
            class_name = list(loaded_obj.keys())[0]
            obj_props = list(loaded_obj.values())[0]
            new_obj = globals()[class_name](**obj_props)
            return new_obj


The_Three_Body_Problem = Book('The Three-Body Problem', '2008', 'Chongqing Press', 'Science fiction', 'Liu Cixin', '12')

The_Three_Body_Problem.dump_pickle()
print(The_Three_Body_Problem.load_pickle())
The_Three_Body_Problem.dump_json()
print(The_Three_Body_Problem.load_json())


# Задание 3
# К уже реализованному классу «Стадион» добавьте возможность упаковки и распаковки данных с использованием json и
# pickle.

class Stadium:
    def __init__(self, name, commissioning_year, country, city, capacity):
        self.name = name
        self.commissioning_year = commissioning_year
        self.country = country
        self.city = city
        self.capacity = capacity

    def display(self):
        print(f'Stadium name: {self.name}\n'
              f'Year of commissioning: {self.commissioning_year}\n'
              f'Country: {self.country}\n'
              f'City: {self.city}\n'
              f'Capacity: {self.capacity}\n')

    def data_input(self):
        self.name = input('Enter stadium name: ')
        self.commissioning_year = input('Enter year of commissioning: ')
        self.country = input('Enter country: ')
        self.city = input('Enter city: ')
        self.capacity = input('Enter capacity: ')

    def dump_pickle(self):
        with open(input('Save object as (enter file name): '), 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle():
        with open(input('Enter file to open: '), 'rb') as file:
            return pickle.load(file)

    def dump_json(self):
        with open(input('Save object as (enter file name): '), 'w') as file:
            json.dump({self.__class__.__name__: self.__dict__}, file)

    @staticmethod
    def load_json():
        with open(input('Enter file to open: '), 'r') as file:
            loaded_obj = json.load(file)
            class_name = list(loaded_obj.keys())[0]
            obj_props = list(loaded_obj.values())[0]
            new_obj = globals()[class_name](**obj_props)
            return new_obj


Camp_Nou = Stadium('Camp Nou', '1957', 'Spain', 'Barcelona', '99354')

Camp_Nou.dump_pickle()
print(Camp_Nou.load_pickle())
Camp_Nou.dump_json()
print(Camp_Nou.load_json())
