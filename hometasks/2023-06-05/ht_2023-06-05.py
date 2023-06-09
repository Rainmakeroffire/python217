# Задание 1
# При старте приложения запускаются три процесса.Первый процесс заполняет список случайными числами. Два других процесса
# ожидают заполнения. Когда списокзаполнен оба процесса запускаются. Первый процесс находит сумму элементов списка,
# второй процесс среднеарифметическое значение в списке. Полученный список, сумма и среднеарифметическое выводятся на
# экран.

import multiprocessing
from random import randint


def fill_arr(arr):
    for i in range(10):
        arr.append(randint(0, 9))
    print(arr)


def get_sum(arr):
    print(sum(arr))


def get_mean(arr):
    print(sum(arr) / len(arr))


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    nums = manager.list()

    pr1 = multiprocessing.Process(target=fill_arr, args=(nums,))
    pr2 = multiprocessing.Process(target=get_sum, args=(nums,))
    pr3 = multiprocessing.Process(target=get_mean, args=(nums,))

    pr1.start()
    pr1.join()

    pr2.start()
    pr3.start()

    pr2.join()
    pr3.join()


# Задание 2
# Пользователь с клавиатуры вводит путь к файлу. После чего запускаются три процесса. Первый процесс заполняет файл
# случайными числами. Два других процесса ожидают заполнения. Когда файл заполнен оба процесса стартуют. Первый процесс
# находит все простые числа, второй процесс факториал каждого числа в файле. Результаты поиска каждый процесс должен
# записать в новый файл. Наэкран необходимо отобразить статистику выполненных операций.

import multiprocessing
from csv import reader, writer
from functools import wraps
from random import randint


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_message = f'Function "{func.__name__}" was called with arguments {(*args, *kwargs.items())}, ' \
                      f'generated array {result[0]} and saved it to "{result[1]}".'
        print(log_message)
        return result

    return wrapper


@logger
def fill_file(filename):
    with open(filename + '.csv', 'w', newline='') as file:
        csv_writer = writer(file)
        array = [randint(0, 9) for i in range(10)]
        csv_writer.writerow(array)
        return [array, file.name]

@logger
def save_primes(filename):
    primes = []
    is_prime = lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1

    with open(filename + '.csv', 'r', newline='') as file:
        csv_reader = reader(file)
        for arr in csv_reader:
            for num in arr:
                if is_prime(int(num)):
                    primes.append(int(num))

    with open('primes.csv', 'w', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow(primes)

    return [primes, file.name]

@logger
def save_factorials(filename):
    factorials = []
    factorial = lambda x: 1 if x <= 1 else x * factorial(x - 1)

    with open(filename + '.csv', 'r', newline='') as file:
        csv_reader = reader(file)
        for arr in csv_reader:
            for num in arr:
                factorials.append(factorial(int(num)))

    with open('factorials.csv', 'w', newline='') as file:
        csv_writer = writer(file)
        csv_writer.writerow(factorials)

    return [factorials, file.name]

if __name__ == '__main__':
    filename = input('Enter filename: ')

    pr1 = multiprocessing.Process(target=fill_file, args=(filename,))
    pr2 = multiprocessing.Process(target=save_primes, args=(filename,))
    pr3 = multiprocessing.Process(target=save_factorials, args=(filename,))

    pr1.start()
    pr1.join()

    pr2.start()
    pr3.start()

    pr2.join()
    pr3.join()
