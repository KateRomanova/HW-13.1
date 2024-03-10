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
        """Делаем список товаров приватным аттрибутом"""
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_unique_products += len(self.__products)
        self.list_products = []

    def __repr__(self):
        return f'Category {self.name}, {self.description}, {self.__products}'

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def products(self):
        return self.__products

    @property
    def updated_products(self):
        """Геттер выводит список продуктов в требуемом формате"""
        updated_products = ''
        for product in self.list_products:
            updated_products += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return updated_products

    @updated_products.setter
    def updated_products(self, item):
        """Принимает на вход объект товара и добавляет его в список"""
        self.list_products.append(item)


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
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return f'Product {self.name}, {self.description}, {self.__price}, {self.quantity}'

    @classmethod
    def add_new_product(cls, name, description, price, quantity):
        """Создает товар и возвращает объект, который можно добавлять в список товаров"""
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для атрибута цены"""
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            self.__price = new_price


# category_1 = Category('Пылесосы', 'убираются', ['dyson', 'irobot', 'xiaomi'])
# print(category_1)
# product_1 = Product('Dyson', 'black', 10000, 12)
# print(product_1)
# product_2 = Product.add_new_product('Xiaomi', 'white', 20000, 2)
# print(product_2)
#
# category_1.updated_products = product_1
# print(category_1.updated_products)
#
# print(product_1.price)
# product_1.price = 0
# print(product_1.price)
