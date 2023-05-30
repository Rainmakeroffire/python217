import json


class Shoes:
    def __init__(self, id_, category, type_, color, price, manufacturer, size):
        self.id_ = id_
        self.category = category
        self.type_ = type_
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return f'{self.id_}, {self.category}, {self.type_}, {self.color}, ${self.price}, ' \
               f'{self.manufacturer}, size: {self.size}'


class DecodeError(Exception):
    pass


class Model:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__shoes = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for shoes in self.data.values():
                self.__shoes[f'{shoes["id_"]} {shoes["type_"]}'] = Shoes(*shoes.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')

    @property
    def shoes(self):
        return self.__shoes

    def save_shoes(self):
        dict_shoes = {f'{item.id_} {item.type_}': item.__dict__ for item in self.__shoes.values()}
        json.dump(dict_shoes, open(self.filepath, 'w', encoding='utf-8'))

    def add_new_shoes(self, shoes_data):
        new_shoes = Shoes(*shoes_data.values())
        self.__shoes[f'{new_shoes.id_} {new_shoes.type_}'] = new_shoes
        self.save_shoes()

    def find_shoes(self, key_words):
        shoes = []
        if isinstance(key_words, list):
            for item in self.__shoes.values():
                items_list = [i.lower() for i in key_words]
                check_list = [i.lower() for i in item.__dict__.values()]
                if all(word in check_list for word in items_list):
                    shoes.append(item)
        else:
            for item in self.__shoes.values():
                check_list = [i.lower() for i in item.__dict__.values()]
                if key_words.lower() in check_list:
                    shoes.append(item)

        return shoes

    def delete_shoes(self, shoes):
        if len(shoes) == 0:
            return 'No items found'
        elif len(shoes) == 1:
            item = shoes[0]
            key = f'{item.id_} {item.type_}'
            self.__shoes.pop(key)
            self.save_shoes()
            return 'Item has been deleted'
        else:
            return 'Too many items'
