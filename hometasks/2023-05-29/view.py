def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.upper().center(50, '*'), sep='\n')
            result = func(*args, **kwargs)
            print('*' * 50)
            return result

        return wrapper

    return decorator


class View:
    @add_title('Awaiting user input')
    def wait_user_answer(self):
        print('List of commands:\n'
              '1. Add new recipe\n'
              '2. Find recipes\n'
              '3. Remove recipe\n'
              '4. Show all recipes\n'
              '0. Exit program\n')
        query = input('Enter command: ')
        print()
        return query

    @add_title('Adding new recipe')
    def get_recipe_data(self):
        props = ['name', 'author', 'course', 'description', 'link', 'ingredients', 'cuisine']
        data = [input(f'Input {prop}: ') for prop in props]
        print()
        return data

    @add_title('Search recipes')
    def get_target(self):
        words = input('Enter comma-separated keywords to search for: ')
        print()
        return words

    @add_title('List of recipes')
    def print_recipes(self, recipes):
        if recipes:
            [print(f'{i}.\n{recipe}') for i, recipe in enumerate(recipes, 1)]
        else:
            print('No items found', '', sep='\n')

    @add_title('Additional information')
    def get_deletion_context(self, recipes):
        print()
        self.print_recipes(recipes)
        number = int(input('Enter ordinal number of recipe to delete: '))
        print()
        return number

    @add_title('Deletion confirmation')
    def return_deleted_value(self, result):
        print(result, '', sep='\n')

