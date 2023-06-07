from abc import ABC, abstractmethod


class PizzaBase:
    sizes = [30, 35, 40]

    def __init__(self, size):
        if size in PizzaBase.sizes:
            self.size = size
        else:
            print('We don\'t make pizzas of this size')

    @property
    def ratio(self):
        return self.size / min(PizzaBase.sizes)

    def __str__(self):
        return f'Pizza base {self.size} cm'


class Pizza(ABC):
    def __init__(self, base: PizzaBase):
        self.base = base

    @abstractmethod
    def cost(self):
        pass


class Palermo(Pizza):
    def __init__(self, base: PizzaBase, toppings=None):
        super().__init__(base)
        self.name = self.__class__.__name__
        self.toppings = toppings

    @property
    def base_cost(self):
        return 450

    @property
    def cost(self):
        return round(self.base_cost * self.base.ratio + self.toppings.cost, 2) if self.toppings \
            else round(self.base_cost * self.base.ratio, 2)

    def __str__(self):
        return f'{self.base.size}cm {self.name} pizza, {self.cost} rub'


class Hawaiian(Pizza):
    def __init__(self, base: PizzaBase, toppings=None):
        super().__init__(base)
        self.name = self.__class__.__name__
        self.toppings = toppings

    @property
    def base_cost(self):
        return 480

    @property
    def cost(self):
        return round(self.base_cost * self.base.ratio + self.toppings.cost, 2) if self.toppings \
            else round(self.base_cost * self.base.ratio, 2)

    def __str__(self):
        return f'{self.base.size}cm {self.name} pizza, {self.cost} rub'


class Pepperoni(Pizza):
    def __init__(self, base: PizzaBase, toppings=None):
        super().__init__(base)
        self.name = self.__class__.__name__
        self.toppings = toppings

    @property
    def base_cost(self):
        return 420

    @property
    def cost(self):
        return round(self.base_cost * self.base.ratio + self.toppings.cost, 2) if self.toppings \
            else round(self.base_cost * self.base.ratio, 2)

    def __str__(self):
        return f'{self.base.size}cm {self.name} pizza, {self.cost} rub'


class QuattroFormaggi(Pizza):
    def __init__(self, base: PizzaBase, toppings=None):
        super().__init__(base)
        self.name = self.__class__.__name__
        self.toppings = toppings

    @property
    def base_cost(self):
        return 400

    @property
    def cost(self):
        return round(self.base_cost * self.base.ratio + self.toppings.cost, 2) if self.toppings \
            else round(self.base_cost * self.base.ratio, 2)

    def __str__(self):
        return f'{self.base.size}cm {self.name} pizza, {self.cost} rub'


class Marinara(Pizza):
    def __init__(self, base: PizzaBase, toppings=None):
        super().__init__(base)
        self.name = self.__class__.__name__
        self.toppings = toppings

    @property
    def base_cost(self):
        return 600

    @property
    def cost(self):
        return round(self.base_cost * self.base.ratio + self.toppings.cost, 2) if self.toppings \
            else round(self.base_cost * self.base.ratio, 2)

    def __str__(self):
        return f'{self.base.size}cm {self.name} pizza, {self.cost} rub'


class Custom(Pizza):
    pricelist = {'sausage': 250,
                 'chicken': 280,
                 'olives': 100,
                 'parmesan': 120,
                 'mushrooms': 160,
                 'beef': 300}

    def __init__(self, base, toppings=None):
        super().__init__(base)
        self.name = self.__class__.__name__
        self.toppings = toppings
        self.ingredients = []
        self.base_cost = 0
        self.is_formed = False

    @property
    def cost(self):
        return round(self.base_cost * self.base.ratio + self.toppings.cost, 2) if self.toppings \
            else round(self.base_cost * self.base.ratio, 2)

    def make_pizza(self):
        [print(f'{k.capitalize()}, {v} rub', sep='\n') for k, v in Custom.pricelist.items()]
        print()
        while True:
            ingredients_choice = list(map(str.strip, input('Enter ingredients you would like to add '
                                                           '(comma-separated): ').split(',')))
            print()
            for ingredient in ingredients_choice:
                if ingredient.lower() not in Custom.pricelist:
                    print(f'"{ingredient.capitalize()}" is not on the list of ingredients\n')

                elif ingredient.lower() not in self.ingredients:
                    self.ingredients.append(ingredient.lower())

            if not self.ingredients:
                print('You cannot order a pizza without ingredients', "", sep='\n')
            else:
                self.is_formed = True
                self.base_cost = sum(Custom.pricelist[ingredient] for ingredient in self.ingredients)
                print(f'Your {self.name} pizza includes:\n')
                [print(f'{i}. {ingredient}', sep='\n') for i, ingredient in enumerate(self.ingredients, 1)]
                print()
                print(self, "", sep='\n')
                break

    def __str__(self):
        return f'{self.base.size}cm {self.name} pizza, {self.cost} rub'



class Toppings:
    pricelist = {'sweet onions': 20,
                 'chilli pepper': 35,
                 'pickled cucumber': 40,
                 'jalapeno': 45,
                 'prosciutto': 30}

    def __init__(self, lst, base):
        self.lst = [topping for topping in lst if topping in Toppings.pricelist]
        self.base = base

    @property
    def cost(self):
        base_cost = sum(Toppings.pricelist[topping] for topping in self.lst)
        return round(base_cost * self.base.ratio, 2)

    def __str__(self):
        return f'{self.lst}'


class Payment(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Cash(Payment):
    def __str__(self):
        return 'in cash'


class BankCard(Payment):
    def __str__(self):
        return 'by bank card'


class ApplePay(Payment):
    def __str__(self):
        return 'using Apple Pay'


class Pizzeria:
    def __init__(self, assortment):
        self.order = []
        self.assortment = assortment
        self.pizzas_sold = 0
        self.revenue = 0
        self.profit = 0
        self.margin = 0.2

    def save_order(self, payment_method):
        # screen
        print("your order".upper().center(50, '='), '=' * 50, sep='\n')
        print()
        for i, pizza in enumerate(self.order, 1):
            print(f'{i}. {pizza.name.upper()} PIZZA')
            if isinstance(pizza, Custom):
                print(f'Ingredients: ')
                [print(f'- {ingredient}') for ingredient in pizza.ingredients]
            print(f'Toppings: ')
            if pizza.toppings:
                [print(f'- {topping}') for topping in pizza.toppings.lst]
            if not pizza.toppings:
                print("None")
            print(f'Price: {pizza.cost} RUB\n')

        print(f'TOTAL: {round(sum([pizza.cost for pizza in self.order]), 2)} RUB\n'
              f'Payment method: {payment_method} upon delivery\n')

        # file
        with open('order.txt', 'w', encoding='utf-8') as file:
            file.write(f'your order'.upper().center(50, '=') + '\n')
            file.write('=' * 50 + "\n")

            for i, pizza in enumerate(self.order, 1):
                file.write(f'{i}. {pizza.name.upper()} PIZZA\n')
                if isinstance(pizza, Custom):
                    file.write(f'Ingredients:\n')
                    for ingredient in pizza.ingredients:
                        file.write(f'- {ingredient}\n')
                file.write(f'Toppings:\n')
                if pizza.toppings:
                    for topping in pizza.toppings.lst:
                        file.write(f'- {topping}\n')
                if not pizza.toppings:
                    file.write(f"None\n")
                file.write(f'Price: {pizza.cost} RUB\n\n')

            file.write(f'TOTAL: {round(sum([pizza.cost for pizza in self.order]), 2)} RUB\n'
                       f'Payment method: {payment_method} upon delivery\n')

        # finalize order
        self.sell_pizza()

    def sell_pizza(self):
        for pizza in self.order:
            self.pizzas_sold += 1
            self.revenue += pizza.cost
        self.revenue = round(self.revenue, 2)
        self.profit = round(self.revenue * self.margin, 2)
        self.order = []

    def view_accounting(self):
        print("accounting reporting-period-to-date".upper().center(50, '='), '=' * 50, sep='\n')
        print(f'Pizzas sold: {self.pizzas_sold} ea\n'
              f'Revenue: {self.revenue} rub\n'
              f'Profit: {self.profit} rub\n')


class Menu:
    @staticmethod
    def add_toppings(pizza_arr, pizza_ind=''):
        if len(pizza_arr) == 1:
            target_pizza = pizza_arr[0]
        else:
            target_pizza = [pizza for i, pizza in enumerate(pizza_arr, 1) if i == int(pizza_ind)][0]
        if toppings_choice == 'a':
            print(f'Adding toppings to your {target_pizza}:')
        [print(f'{k.capitalize()}, {v} rub', sep='\n') for k, v in Toppings.pricelist.items()]
        print()
        while True:
            toppings_lst = list(map(str.strip, input('Enter toppings you would like to add '
                                                 '(comma-separated, s - to skip): ').split(',')))
            print()

            if toppings_lst[0] == 's':
                break

            for topping in toppings_lst:
                if topping not in Toppings.pricelist:
                    print(f'"{topping.capitalize()}" topping does not exist\n')

            if target_pizza.toppings:
                for i in target_pizza.toppings.lst:
                    for j in toppings_lst:
                        if j == i:
                            print(f'Note that "{j}" topping was already on the list', "", sep='\n')
                toppings = [i.lower() for i in toppings_lst
                            if i.lower() in Toppings.pricelist and i.lower() not in target_pizza.toppings.lst]

                if not toppings:
                    print('You added no new toppings', "", sep='\n')
                else:
                    for topping in toppings:
                        if topping not in target_pizza.toppings.lst:
                            target_pizza.toppings.lst.append(topping)
            else:
                toppings = []
                for i in toppings_lst:
                    if i.lower() in Toppings.pricelist and i.lower() not in toppings:
                        toppings.append(i)
                if not toppings:
                    print('You added no new toppings', "", sep='\n')
                else:
                    pizza_toppings = Toppings(toppings, target_pizza.base)
                    target_pizza.toppings = pizza_toppings

            if target_pizza.toppings:
                print(f'You have the following toppings added to your '
                      f'{target_pizza.name} pizza:')
                [print(f'{i}. {topping}', sep='\n') for i, topping in enumerate(target_pizza.toppings.lst, 1)]
                print()
                print(target_pizza, "", sep='\n')
            break


assortment = [Palermo, Hawaiian, Pepperoni, QuattroFormaggi, Marinara, Custom]
pizzeria = Pizzeria(assortment)

while True:
    # select pizza
    [print(f"{i}. {pizza.__name__}", sep='\n') for i, pizza in enumerate(pizzeria.assortment, 1)]
    print()
    pizza_choice = input(f'Enter pizza to order (0 to quit): ')
    print()
    if pizza_choice == '0':
        break
    elif pizza_choice == 'accounting':
        pizzeria.view_accounting()
    elif pizza_choice.lower() not in [i.__name__.lower() for i in pizzeria.assortment]:
        print('Incorrect input. Try again', "", sep='\n')
    else:
        while True:
            # select base
            base_choice = input(f'Enter pizza diameter - 30, 35 or 40 cm (0 to go to main menu): ')
            print()
            if base_choice == '0':
                break
            elif not base_choice.isdigit() or int(base_choice) not in PizzaBase.sizes:
                print('Incorrect input. Try again', "", sep='\n')
            else:
                pizza_class = [i for i in pizzeria.assortment if i.__name__.lower() == pizza_choice.lower()][0]
                pizza_base = PizzaBase(int(base_choice))
                while True:
                    # select quantity
                    quantity = input(f'How many {pizza_choice.capitalize()} pizzas do you want to order '
                                     f'(0 to go to main menu)? ')
                    print()
                    if quantity == '0':
                        break
                    elif not quantity.isdigit():
                        print('Incorrect input. Try again', "", sep='\n')
                    else:
                        for i in range(int(quantity)):
                            pizzeria.order.append(pizza_class(pizza_base))
                        for j, pizza in enumerate(pizzeria.order, 1):
                            if isinstance(pizza, Custom) and not pizza.is_formed:
                                print(f'Ingredients for {pizza.name} pizza{f" (#{j} of your order)" if int(quantity) > 1 else ""}:\n')
                                pizza.make_pizza()
                        while True:
                            # select toppings
                            toppings_choice = input(f'Would you like to add '
                                                    f'{"some more " if any(obj.toppings is not None for obj in pizzeria.order) else ""}'
                                                    f'toppings to your pizza'
                                                    f'{"" if len(pizzeria.order) == 1 else "s"} '
                                                    f'({"a - to one, m - to many, " if len(pizzeria.order) > 1 else "a - to add, "}'
                                                    f'any other key - to choose payment method, 0 - to go to main menu)? ')
                            print()
                            if toppings_choice == '0':
                                break

                            elif toppings_choice == 'a':
                                if len(pizzeria.order) == 1:
                                    Menu.add_toppings(pizzeria.order)
                                else:
                                    while True:
                                        [print(f'{i}. {pizza.name}', sep='\n') for i, pizza in enumerate(pizzeria.order, 1)]
                                        print()
                                        target_pizza = input('Select ordinal number of the pizza to add toppings to '
                                                             '(0 to go to previous menu): ')
                                        print()
                                        if target_pizza == '0':
                                            break
                                        elif not target_pizza.isdigit() or \
                                                int(target_pizza) not in range(1, len(pizzeria.order) + 1):
                                            print('Incorrect input. Try again', "", sep='\n')
                                        else:
                                            Menu.add_toppings(pizzeria.order, pizza_ind=target_pizza)
                                            break

                            elif len(pizzeria.order) > 1 and toppings_choice == 'm':
                                for index, pizza in enumerate(pizzeria.order, 1):
                                    print(f'Adding toppings to:\n{index}. {pizza}\n')
                                    Menu.add_toppings(pizzeria.order, pizza_ind=str(index))
                            else:
                                while True:
                                    # Select payment method
                                    payment_method = input('Select payment method '
                                                           '(c - cash, b - bank card, a - Apple Pay): ')
                                    print()
                                    if payment_method not in ['c', 'b', 'a']:
                                        print('Incorrect input. Try again', "", sep='\n')
                                    elif payment_method == 'c':
                                        cash = Cash()
                                        pizzeria.save_order(cash)
                                        break
                                    elif payment_method == 'b':
                                        bank_card = BankCard()
                                        pizzeria.save_order(bank_card)
                                        break
                                    elif payment_method == 'a':
                                        apple_pay = ApplePay()
                                        pizzeria.save_order(apple_pay)
                                        break
                                break
                        break
                break


