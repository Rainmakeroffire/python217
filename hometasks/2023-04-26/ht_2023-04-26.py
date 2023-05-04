# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип списка нужно выбрать
# в зависимости от поставленной ниже задачи). После чего нужно показать меню, в котором предложить пользователю набор
# пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом,
# без добавления числа);
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления);
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца);
# 4. Проверить есть ли значение в списке;
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения).
# В зависимости от выбора пользователя выполняется действие, после чего меню отображается снова.

import random


class Stack:
    def __init__(self, array):
        self.stack = [int(i) if i.isdigit() else random.randint(0, 9) for i in array]

    def append(self, value):
        if type(value) != int:
            print('Invalid data type')
        else:
            self.stack.append(value)

    def remove(self, value):
        if len(self.stack) != 0:
            self.stack = [i for i in self.stack if i != int(value)]

    def show(self, value):
        if value == "d":
            print(' -> '.join(map(str, self.stack)), "", sep='\n')
        else:
            result = self.stack
            result.reverse()
            print(' <- '.join(map(str, result)), "", sep='\n')

    def is_listed(self, value):
        return int(value) in self.stack if value.isdigit() else False

    def replace(self, value, replacer, option):
        if option == 'a':
            self.stack = [i if i != value else replacer for i in self.stack]
        else:
            for i in range(len(self.stack)):
                if self.stack[i] == value:
                    self.stack[i] = replacer
                    break


lst = [input('Enter number: ') for i in range(5)]
nums = Stack(lst)
nums.show('d')

while True:
    action = input(
        'Select action: (1) add new number, (2) remove all occurrences of a number, (3) show list, '
        '(4) check if a value is in the list, (5) replace value, (0) exit: ')
    if action not in ['0', '1', '2', '3', '4', '5']:
        print('Incorrect input. Try again.')
        print()

    if action == '1':
        while True:
            adding = input('Enter number to add. Enter (q) to quit: ')
            if not adding.isdigit() and adding != 'q':
                print('Incorrect input. Digits only.')
            elif adding == 'q':
                break
            elif int(adding) in nums.stack:
                print(f'Can\'t add {adding}, it\'s already in the list')
            else:
                nums.append(int(adding))
                print(f'Value has been added: {" -> ".join(map(str, nums.stack))}', "", sep='\n')
                break

    if action == '2':
        while True:
            removing = input('Enter number to remove. Enter (q) to quit: ')
            if not removing.isdigit() and removing != 'q':
                print('Incorrect input. Digits only.')
            elif removing == 'q':
                break
            elif int(removing) not in nums.stack:
                print('No such value')
            else:
                nums.remove(removing)
                print(f'Value has been removed: {" -> ".join(map(str, nums.stack))}', "", sep='\n')
                break

    if action == '3':
        while True:
            option = input('Print the list in direct (d) or reversed (r) order? Enter (q) to quit: ')
            if option not in ['d', 'r', 'q']:
                print('Incorrect input. Try again.')
                print()
            elif option == 'q':
                break
            else:
                nums.show(option)
                break

    if action == '4':
        while True:
            check_value = input('Enter value to check. Enter (q) to quit: ')
            if check_value == 'q':
                break
            else:
                print(f'{check_value} is {"" if nums.is_listed(check_value) else "not "}in the list', "", sep='\n')
                break

    if action == '5':
        while True:
            option = input('Replace all (a) value occurrences or first (f) only? Enter (q) to quit: ')
            if option not in ['a', 'f', 'q']:
                print('Incorrect input. Try again.')
                print()
            elif option == 'q':
                break
            else:
                while True:
                    value = input('Enter value to replace: ')
                    if value not in map(lambda x: str(x), nums.stack):
                        print("No such value")
                    else:
                        while True:
                            replacer = input('Enter replacer: ')
                            if not replacer.isdigit():
                                print("Incorrect input. Digits only")
                            else:
                                nums.replace(int(value), int(replacer), option)
                                print(f'{value} has been replaced with {replacer}: '
                                      f'{" -> ".join(map(str, nums.stack))}', "", sep='\n')
                                break
                        break
                break

    if action == '0':
        break


# Задания 2 и 3
# 2)
# Реализуйте класс стека для работы со строками (стек строк). Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать необходимую операцию.

# 3)
# Измените стек из второго задания, таким образом, чтобы его размер был нефиксированным.

class Stack:
    def user_menu(self):
        while True:
            action = input(
                'Select action: (1) add new string, (2) pop string, (3) count strings, '
                '(4) check if stack is empty, (5) check if stack is full, (6) clear stack , (7) peek value, (0) exit: ')
            if action not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                print('Incorrect input. Try again.')
                print()

            if action == '1':
                while True:
                    adding = input('Enter string to add. Enter (q) to quit: ')
                    if adding == 'q':
                        break
                    else:
                        self.append(adding)
                        break

            if action == '2':
                message_1 = "No values to pop out. Stack is empty"
                message_2 = " has been popped out:"
                print(f'{message_1 if self.is_empty() else self.pop() + message_2}\n'
                      f'{" -> ".join(map(str, self.stack))}', "", sep='\n')

            if action == '3':
                self.count()

            if action == '4':
                print(f'Stack is {"" if self.is_empty() else "not "}empty', "", sep='\n')

            if action == '5':
                print(f'Stack is {"" if self.is_full() else "not "}full', "", sep='\n')

            if action == '6':
                self.clear()
                print("Stack has been cleared", "", sep='\n')

            if action == '7':
                print(f'{"Peeked value: " + self.peek() if not self.is_empty() else "No values to peek"}', "", sep='\n')

            if action == '0':
                break

    def __init__(self, size):  # <= параметр для фиксированного стека
        self.size = size  # <= атрибут для фиксированного стека
        self.stack = list()
        self.menu = self.user_menu()

    def append(self, value):
        if len(self.stack) >= self.size:
            print('Stack is full', "", sep='\n')
        else:
            self.stack.append(str(value))
            print(f'Value has been added: {" -> ".join(map(str, self.stack))}', "", sep='\n')

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def count(self):
        count = len(self.stack)
        print(f'Stack has {count if count > 0 else "no"} value{"" if count == 1 else "s"}', "", sep='\n')

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):  # <= метод для фиксированного стека
        return len(self.stack) == self.size

    def clear(self):
        self.stack = []

    def peek(self):
        return self.is_empty() or self.stack[-1]


new_stack = Stack(5)  # <= аргумент для фиксированного стека
