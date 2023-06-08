# Задание 1
# Создайте класс, содержащий набор целых чисел. В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса с помощью модульного тестирования(unittest).

class IntArrayHandler:
    def __init__(self, array: list[int]):
        self.array = array

    def get_sum(self):
        return sum(self.array)

    def get_mean(self):
        return sum(self.array) / len(self.array) if len(self.array) else 'You passed an empty list'

    def get_max(self):
        return max(self.array)

    def get_min(self):
        return min(self.array)
