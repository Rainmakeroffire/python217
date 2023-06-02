import sys
from csv import reader, writer


class Recipe:
    def __init__(self, name, author, course, description, link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.course = course
        self.description = description
        self.link = link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def __str__(self):
        return f'{self.name.center(50, "*")}\n' \
               f'Cuisine: {self.cuisine}\n' \
               f'Course: {self.course}\n' \
               f'Ingredients: {self.ingredients}\n' \
               f'Description: {self.description}\n\n' \
               f'Recipe by: {self.author}\n' \
               f'Video: {self.link}\n'


class Model:
    def __init__(self, filename):
        self.filename = filename
        self.database = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = reader(file)
                for string in data:
                    self.database.append(self.__string_to_recipe__(string))
        except FileNotFoundError:
            print('Failed to load database. Proceed with empty data.', file=sys.stderr, sep='\n')

    @staticmethod
    def __string_to_recipe__(string):
        return Recipe(string.pop(0), string.pop(0), string.pop(0), string.pop(0), string.pop(0), string.pop(0),
                      string.pop(0))

    @staticmethod
    def __recipe_to_list__(recipe):
        return list(prop for prop in recipe.__dict__.values())

    def __save_data__(self):
        with open(self.filename, 'w', encoding='utf-8', newline='') as csv_file:
            data_writer = writer(csv_file)
            data_writer.writerows(map(self.__recipe_to_list__, self.database))

    def add_new_recipe(self, recipe_data):
        self.database.append(self.__string_to_recipe__(recipe_data))
        self.__save_data__()

    def get_recipe_by(self, words):
        words = list(map(str.strip, words.split(',')))
        recipes = []
        for word in words:
            for recipe in self.database:
                if word.lower() in ' '.join(map(str.lower, recipe.__dict__.values())) and recipe not in recipes:
                    recipes.append(recipe)
        return recipes

    def delete_recipes(self, recipes):
        if len(recipes) == 0:
            return 'No items found'
        elif len(recipes) == 1:
            try:
                index = [i for i, value in enumerate(self.database) if value == recipes[0]][0]
                deleted = self.database.pop(index)
                self.__save_data__()
                return f'The following recipe has been deleted:\n{deleted}'
            except IndexError:
                print('Unable to delete item. Please contact customer\'s support', "", sep='\n')
        else:
            return 'Too many items'