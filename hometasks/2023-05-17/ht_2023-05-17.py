# Задание 1
# Создайте реализацию паттерна Command. Протестируйте работу созданного класса.

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def turn_on(self):
        print("Light is on.")

    def turn_off(self):
        print("Light is off.")


class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        command = self.commands.get(command_name)
        if command:
            command.execute()
        else:
            print("Command not found.")


if __name__ == "__main__":
    light = Light()

    turn_on_command = TurnOnCommand(light)
    turn_off_command = TurnOffCommand(light)

    remote_control = RemoteControl()
    remote_control.register_command("on", turn_on_command)
    remote_control.register_command("off", turn_off_command)

    remote_control.execute_command("on")
    remote_control.execute_command("off")
    remote_control.execute_command("toggle")


# Задание 2
# Есть класс, предоставляющий доступ к набору чисел. Источником этого набора чисел является некоторый файл. С
# определенной периодичностью данные в файле меняются (надо реализовать механизм обновления). Приложение должно получать
# доступ к этим данным и выполнять набор операций над ними (сумма, максимум, минимум и т.д.). При каждой попытке доступа
# к этому набору необходимо вносить запись в лог-файл. При реализации используйте паттерн Proxy (для логгирования)
# и другие необходимые паттерны.

from csv import reader, writer


class Logger:
    def __init__(self):
        self.log_name = 'log.txt'

    def log_func(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log_message = f'Function {func.__name__} was called with arguments {(*args, *kwargs.items())} ' \
                          f'and returned {result}'
            with open(self.log_name, 'a', encoding='utf-8') as file:
                file.write('\n' + log_message)
            return result

        return wrapper


logger = Logger()


class ArrayHandler:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, 'r', encoding='utf-8', newline='') as file:
                file_content = list(reader(file))
                self.array = [int(val) for val in file_content[0] if val.isdigit()]
        except FileNotFoundError:
            print(f'File {self.filename} not found')
            self.array = []
            self.update()

    @logger.log_func
    def __str__(self):
        return f'List: {self.array}'

    @logger.log_func
    def find_min(self):
        return f'List min value: {min(self.array)}' if self.array else 'List is empty'

    @logger.log_func
    def find_max(self):
        return f'List max value: {max(self.array)}' if self.array else 'List is empty'

    @logger.log_func
    def find_sum(self):
        return f'Sum of list values: {sum(self.array)}' if self.array else 'List is empty'

    @logger.log_func
    def update(self):
        query = list(map(str, input('Enter new values, separated by a space: ').split()))
        self.array = [int(val) for val in query if val.isdigit()]
        with open(self.filename, 'w', encoding='utf-8', newline='') as file:
            writer(file).writerow(query)
        return f'Updated list: {self.array}'


arr = ArrayHandler('db.csv')

print(arr.find_min())
print(arr.find_max())
print(arr.find_sum())

print(arr)


# Задание 3
# Создайте приложение для работы в библиотеке. Оно должно оперировать следующими сущностями: Книга, Библиотекарь,
# Читатель. Приложение должно позволять вводить, удалять, изменять, сохранять в файл, загружать из файла, логгировать
# действия, искать информацию (результаты поиска выводятся на экран или файл) о сущностях. При реализации используйте
# максимально возможное количество паттернов проектирования.

import pickle
import random
import string
from abc import ABC, abstractmethod


def display_ojb_arrays(arr):
    result = ''
    for i in arr:
        result += str(i) + "\n"
    return result


class Logger:
    def __init__(self):
        self.log_name = 'log.txt'

    def log_func(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            log_message = f'Function {func.__name__} was called with arguments {(*args, *kwargs.items())} ' \
                          f'and returned {result}'
            with open(self.log_name, 'a', encoding='utf-8') as file:
                file.write('\n' + log_message)
            return result

        return wrapper


logger = Logger()


class BaseStrategy(ABC):
    @abstractmethod
    def do_work(self, obj):
        pass


class File(BaseStrategy):
    def do_work(self, obj):
        with open(input('Save object as (enter file name): '), 'wb') as file:
            pickle.dump(obj, file)
            print('Object has been saved', "", sep='\n')


class Console(BaseStrategy):
    def do_work(self, obj):
        print(f'{"=" * 20}{library.name.upper()}{"=" * 20}\n'
              f'Books checked out:\n', *library.books_checked_out,
              *library.readers, sep='\n')


class Book:
    def __init__(self, title, author, genre, publisher):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher

    def __str__(self):
        return f'Book title: {self.title}\n' \
               f'Author: \t{self.author}\n' \
               f'Genre: \t\t{self.genre}\n' \
               f'Publisher:  {self.publisher}\n'


The_Three_Body_Problem = Book('The Three-Body Problem', 'Liu Cixin', 'Science fiction', 'Chongqing Press')
The_Three_Musketeers = Book('The Three Musketeers', 'Alexandre Dumas', 'Historical novel', 'Simon & Schuster')
For_Whom_the_Bell_Tolls = Book('For Whom the Bell Tolls', 'Ernest Hemingway', 'War novel',
                               'Charles Scribner\'s Sons')

books = [The_Three_Body_Problem, The_Three_Musketeers, For_Whom_the_Bell_Tolls]


class Reader:
    def __init__(self, first_name, second_name, library_card_No):
        self.first_name = first_name
        self.second_name = second_name
        self.library_card_No = library_card_No
        self.books_checked_out = []

    def __str__(self):
        return f'{"=" * 20}Reader Details{"=" * 20}\n' \
               f'First Name: {self.first_name}\n' \
               f'Second Name: {self.second_name}\n' \
               f'Library Card No.: {self.library_card_No}\n' \
               f'Books Checked out:\n\n{display_ojb_arrays(self.books_checked_out)}\n'


class Library:
    def __init__(self, name, address, library_stock):
        self.name = name
        self.address = address
        self.library_stock = library_stock
        self.books_checked_out = dict()
        self.readers = []

    def __str__(self):
        return f'{self.name} located at {self.address}'

    @logger.log_func
    def replenish_stock(self, book_obj):
        self.library_stock.append(book_obj)

    @logger.log_func
    def remove_from_stock(self, book_obj):
        self.library_stock.remove(book_obj)

    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    @logger.log_func
    def save(self):
        self.strategy.do_work(self)

    @logger.log_func
    def load(self):
        with open(input('Enter file to open: '), 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def search():
        search = input('Enter book title: ')
        print()
        print(f'{"=" * 20}Search Results{"=" * 20}')
        for book in library.library_stock:
            if book.title.lower().startswith(search.lower()):
                print(book)


library = Library('Russian State Library', '3/5 Vozdvizhenka St, Bldg 2, Moscow', books)


class Librarian:
    @logger.log_func
    def create_reader(self):
        reader = Reader(input('Enter first name: '), input('Enter second name: '),
                        ''.join(random.choice(string.ascii_lowercase) for i in range(3)) +
                        ''.join(str(random.randint(0, 9)) for i in range(5)))
        print()
        library.readers.append(reader)
        return reader

    @logger.log_func
    def update_reader(self, reader_obj):
        first_name = input('Enter first name (blank entry to leave as is): ')
        second_name = input('Enter second name (blank entry to leave as is): ')
        library_card_No = input('Enter library card No. (blank entry to leave as is): ')
        print()

        reader_obj.first_name = first_name if first_name != '' else reader_obj.first_name
        reader_obj.second_name = second_name if second_name != '' else reader_obj.second_name
        reader_obj.library_card_No = library_card_No if library_card_No != '' else reader_obj.library_card_No

    @logger.log_func
    def delete_reader(self, reader_obj):
        if not reader_obj.books_checked_out:
            library.readers.remove(reader_obj)
            print('Profile has been deleted', "", sep='\n')
        else:
            print('Impossible to delete reader\'s profile before all the checked out books are surrendered',
                  "", sep='\n')

    @logger.log_func
    def check_in(self, book_obj, reader_obj):
        del library.books_checked_out[book_obj]
        reader_obj.books_checked_out.remove(book_obj)

    @logger.log_func
    def check_out(self, book_obj, reader_obj):
        library.books_checked_out[book_obj] = reader_obj
        reader_obj.books_checked_out.append(book_obj)


librarian = Librarian()

while True:
    action = input(
        'Select action: (1) add new reader, (2) update reader\'s profile, (3) remove reader, '
        '(4) search books, (5) save data, (6) load data, (7) book check-in, (8) book check-out, '
        '(9) replenish library stock, (10) remove items from stock, (11) view library stock, '
        '(12) view checked out books, (0) exit: \n')
    if action not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
        print('Incorrect input. Try again.', "", sep='\n')

    if action == '1':
        reader = librarian.create_reader()
        print('Profile has been created:', reader, sep='\n')

    if action == '2':
        if library.readers:
            i = 0
            for reader in library.readers:
                i += 1
                print(f'{i}.\n{reader}\n')
            while True:
                profile = input('Select a profile to update (enter ordinal number, 0 - to exit): ')
                if profile == '0':
                    break
                elif not profile.isdigit() or int(profile) not in [i for i in range(1, len(library.readers) + 1)]:
                    print('Incorrect input. Try again.', "", sep='\n')
                else:
                    librarian.update_reader(library.readers[int(profile) - 1])
                    print('Profile has been updated:', library.readers[int(profile) - 1], sep='\n')
                    break

        else:
            print('No readers registered', "", sep='\n')

    if action == '3':
        if library.readers:
            i = 0
            for reader in library.readers:
                i += 1
                print(f'{i}.\n{reader}\n')
            while True:
                profile = input('Select a profile to delete (enter ordinal number, 0 - to exit): ')
                if profile == '0':
                    break
                elif not profile.isdigit() or int(profile) not in [i for i in range(1, len(library.readers) + 1)]:
                    print('Incorrect input. Try again.', "", sep='\n')
                else:
                    librarian.delete_reader(library.readers[int(profile) - 1])
                    break

        else:
            print('No readers registered', "", sep='\n')

    if action == '4':
        library.search()

    if action == '5':
        while True:
            strategy = input('Would you like to save data to file (f) or display in console (c), 0 - to exit: ')
            if strategy == '0':
                break
            elif strategy == 'f':
                library.set_strategy(File())
                library.save()
                break
            elif strategy == 'c':
                library.set_strategy(Console())
                library.save()
                break
            else:
                print('Incorrect input. Try again.', "", sep='\n')

    if action == '6':
        try:
            library = library.load()
            print('Object has been loaded', "", sep='\n')
        except FileNotFoundError:
            print('Failed to load object. File not found', "", sep="\n")

    if action == '7':
        if library.books_checked_out:
            book_title = input('Enter book title in full: ')
            print()
            match_found = False
            for book, reader in library.books_checked_out.items():
                if book_title.lower() == book_title.lower():
                    librarian.check_in(book, reader)
                    match_found = True
                    print(f'The book below\n{book}has been successfully checked in by'
                          f' {reader.first_name} {reader.second_name}', "", sep='\n')
                    break

            if not match_found:
                print('Incorrect input. Try again.', "", sep='\n')
                break
        else:
            print('No books to check in', "", sep='\n')
            break

    if action == '8':
        if library.readers:
            i = 0
            for reader in library.readers:
                i += 1
                print(f'{i}.\n{reader}\n')
            while True:
                reader = input('Select a reader (enter ordinal number, 0 - to exit): ')
                if reader == '0':
                    break
                elif not reader.isdigit() or int(reader) not in [i for i in range(1, len(library.readers) + 1)]:
                    print('Incorrect input. Try again.', "", sep='\n')
                else:
                    while True:
                        if library.library_stock:
                            available_stock = [j for j in library.library_stock if j not in library.books_checked_out]
                            i = 0
                            for book in available_stock:
                                i += 1
                                print(f'{i}.\n{book}\n')
                            while True:
                                book = input('Select a book to check out (enter ordinal number, 0 - to exit): ')
                                if book == '0':
                                    break
                                elif not book.isdigit() or int(book) not in [i for i in
                                                                             range(1, len(available_stock) + 1)]:
                                    print('Incorrect input. Try again.', "", sep='\n')
                                else:
                                    librarian.check_out(available_stock[int(book) - 1],
                                                        library.readers[int(reader) - 1])
                                    print('Book has been checked out:', available_stock[int(book) - 1], sep='\n')
                                    break

                        else:
                            print('No books registered', "", sep="\n")
                        break
                break
        else:
            print('No readers registered', "", sep='\n')

    if action == '9':
        book = Book(input('Enter book title: '), input('Enter author: '), input('Enter genre: '),
                    input('Enter publisher: '))
        print()
        library.replenish_stock(book)

    if action == '10':
        if library.library_stock:
            i = list(enumerate(library.library_stock))[0][0]
            for book in library.library_stock:
                i += 1
                print(f'{i}.\n{book}\n')
            while True:
                book = input('Select a book to delete (enter ordinal number, 0 - to exit): ')
                if book == '0':
                    break
                elif not book.isdigit() or int(book) not in [i for i in range(1, len(library.library_stock) + 1)]:
                    print('Incorrect input. Try again.', "", sep='\n')
                else:
                    library.remove_from_stock(library.library_stock[int(book) - 1])
                    print('Book has been deleted', "", sep='\n')
                    break

        else:
            print('No readers registered', "", sep="\n")

    if action == '11':
        print(f'{"=" * 20}Library Stock{"=" * 20}\n')
        for book in library.library_stock:
            print(book)

    if action == '12':
        print(f'{"=" * 20}Checked out Books{"=" * 20}')
        dicti = library.books_checked_out
        for book in dicti:
            print(book)
            print(f'Current book holder:\n{dicti[book].first_name} {dicti[book].second_name}', "", sep='\n')

    if action == '0':
        break
