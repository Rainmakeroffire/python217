# Задание 2
# Создайте класс для числа. В классе должна быть реализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

class Number:
    def __init__(self, value: int):
        self.value = value if type(value) == int else 0

    def set_value(self):
        query = input('Enter new value: ')
        self.value = int(query) if query.isdigit() else 0
        return 'Value updated'

    def save(self):
        with open('save.txt', 'w', encoding='utf-8') as file:
            file.write(str(self.value))
            return 'Saved successfully'

    def load(self):
        with open('save.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            self.value = int(data) if data.isdigit() else 0
            return 'Loaded successfully'

    def make_oct(self):
        return oct(self.value)

    def make_hex(self):
        return hex(self.value)

    def make_bin(self):
        return bin(self.value)

    def __str__(self):
        return str(self.value)
