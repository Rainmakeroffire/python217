from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model('recipes.csv')

    def run(self):
        query = None
        while query != '0':
            query = self.view.wait_user_answer()
            self.evaluate_user_answer(query)
            if query not in ['1', '2', '3', '4', '0', None]:
                print('Incorrect input. Try again', '', sep='\n')

    def evaluate_user_answer(self, query):
        if query == '1':
            recipe_data = self.view.get_recipe_data()
            self.model.add_new_recipe(recipe_data)
        elif query == '2':
            target = self.view.get_target()
            recipes = self.model.get_recipe_by(target)
            self.view.print_recipes(recipes)
        elif query == '3':
            target = self.view.get_target()
            recipes = self.model.get_recipe_by(target)
            result = self.model.delete_recipes(recipes)
            self.view.return_deleted_value(result)
            if result == 'Too many items':
                self.view.print_recipes(recipes)
                number = self.view.get_deletion_context(recipes)
                try:
                    result = self.model.delete_recipes([recipes[number - 1]])
                    self.view.return_deleted_value(result)
                except IndexError:
                    print('Incorrect input. Go back to function and try again', '', sep='\n')
        elif query == '4':
            recipes = self.model.database
            self.view.print_recipes(recipes)
