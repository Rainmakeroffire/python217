# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем
# двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

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


Maserati_MC20 = Auto('MC20', '2020', 'Maserati', '2992', 'White', '215000')

Maserati_MC20.display()
Maserati_MC20.data_input()
Maserati_MC20.display()


# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора,
# цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы
# класса.

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


The_Three_Body_Problem = Book('The Three-Body Problem', '2008', 'Chongqing Press', 'Science fiction', 'Liu Cixin', '12')

The_Three_Body_Problem.display()
The_Three_Body_Problem.data_input()
The_Three_Body_Problem.display()


# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город,
# вместимость. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через
# методы класса.

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


Camp_Nou = Stadium('Camp Nou', '1957', 'Spain', 'Barcelona', '99354')

Camp_Nou.display()
Camp_Nou.data_input()
Camp_Nou.display()
