def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.upper().center(50, '='))
            result = func(*args, **kwargs)
            print('='*50)
            return result
        return wrapper
    return decorator


class View:
    @add_title('Awaiting user input')
    def wait_user_answer(self):
        print('Available commands:\n'
              '1. Add new item\n'
              '2. Show all shoes\n'
              '3. Find shoes\n'
              '4. Delete item\n'
              '0. Exit\n')
        query = input('Enter command: ')
        print()
        return query

    @add_title('Adding new item')
    def get_new_shoes_data(self):
        dict_shoes = {'id_': None,
                      'category': None,
                      'type_': None,
                      'color': None,
                      'price': None,
                      'manufacturer': None,
                      'size': None}
        for key in dict_shoes.keys():
            dict_shoes[key] = input(f'Enter shoes {key.lower()}: ')
        print()
        return dict_shoes

    @add_title('Shoes assortment')
    def show_shoes(self, shoes):
        if shoes:
            if isinstance(shoes, dict):
                [print(f'{i}. {shoes[item]}') for i, item in enumerate(shoes, 1)]
            else:
                [print(f'{i}. {item}') for i, item in enumerate(shoes, 1)]
            print()
        else:
            print('No items found', '', sep='\n')

    @add_title('Search')
    def get_keywords_to_find_shoes(self):
        key_words = input('Enter comma-separated list to search for: ').split()
        print()
        return key_words

    @add_title('Picking item for deletion')
    def get_shoes_item(self):
        shoes_item = input('Enter any shoes parameter: ')
        print()
        return shoes_item.strip()

    @add_title('Additional information')
    def get_deletion_context(self):
        number = int(input('Enter number for deletion: '))
        print()
        return number

    @add_title('Deletion confirmation')
    def return_delete_shoes(self, result):
        print(result, '', sep='\n')

    @add_title('Loading error')
    def throw_an_error(self, e):
        print('An error occurred while loading the database:', e, sep='\n')
