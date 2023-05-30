from model import Model, DecodeError
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model('db.txt')
        except DecodeError as e:
            self.view.throw_an_error(e)

    def run(self):
        query = None
        while query != '0':
            query = self.view.wait_user_answer()
            self.resolve_user_answer(query)
            if query not in ['1', '2', '3', '4', '0', None]:
                print('Incorrect input. Try again', '', sep='\n')

    def resolve_user_answer(self, query):
        if query == '1':
            shoes_data = self.view.get_new_shoes_data()
            self.model.add_new_shoes(shoes_data)
        elif query == '2':
            shoes = self.model.shoes
            self.view.show_shoes(shoes)
        elif query == '3':
            key_words = self.view.get_keywords_to_find_shoes()
            shoes = self.model.find_shoes(key_words)
            self.view.show_shoes(shoes)
        elif query == '4':
            shoes_item = self.view.get_shoes_item()
            shoes = self.model.find_shoes(shoes_item)
            result = self.model.delete_shoes(shoes)
            self.view.return_delete_shoes(result)
            if result == 'Too many items':
                self.view.show_shoes(shoes)
                number = self.view.get_deletion_context()
                try:
                    result = self.model.delete_shoes([shoes[number - 1]])
                    self.view.return_delete_shoes(result)
                except IndexError:
                    print('Incorrect input. Go back to function and try again', '', sep='\n')


