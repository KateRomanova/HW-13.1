# from utils import


class Category:
    """Создаем класс и определяем его свойства"""
    number_of_categories = 0
    number_of_unique_products = 0
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Добавляем инициализацию так, чтобы каждый параметр был передан в инициализацию объекта и сохранен.
        Добавляем два атрибута, в которых будут храниться общее количество категорий и общее количество уникальных
        продуктов, не учитывая количество в наличии."""
        self.name = name
        self.description = description
        self.products = products
        Category.number_of_categories += 1
        Category.number_of_unique_products += 1


class Product:
    """Создаем класс и определяем его свойства"""
    number_of_unique_products = 0
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.number_of_unique_products += 1
