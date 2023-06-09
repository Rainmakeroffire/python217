# Задание 2
# Создайте класс Рецепт. Необходимо хранить следующую информацию:
# ■ название рецепта;
# ■ автор рецепта;
# ■ тип рецепта (первое, второе блюдо и т.д.);
# ■ текстовое описание рецепта;
# ■ ссылка на видео с рецептом;
# ■ список ингредиентов;
# ■ название кухни (итальянская, французская, украинская и т.д.).
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Рецепт и код для использования
# модели, контроллера и представления.

from controller import Controller


def main():
    app = Controller()
    app.run()


if __name__ == '__main__':
    main()