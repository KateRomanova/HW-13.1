from abc import ABC, abstractmethod


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

    def __repr__(self):
        return f'Category {self.name}, {self.description}, {self.__products}'

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    def __len__(self):
        result = 0
        for i in self.__products:
            result += i.quantity
        return result

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    @property
    def products(self):
        return self.__products

    @property
    def updated_products(self):
        """Геттер выводит список продуктов в требуемом формате"""
        updated_products = []
        for product in self.__products:
            updated_products.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')

        return updated_products

    @updated_products.setter
    def updated_products(self, item):
        """Принимает на вход объект товара и добавляет его в список"""
        if isinstance(item, self.__class__):
            self.__products.append(item)
        raise TypeError


class Commodity(ABC):
    """Создаем абстрактный базовый класс для классов "Продукт", "Смартфоны" и "Трава Газонная"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def add_product(self, list_of_products):
        pass


class MixinLog:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f'Создан объект {self.__class__.__name__}, {self.__dict__.items()}'


class Product(MixinLog, Commodity):
    """Создаем класс и определяем его свойства"""
    number_of_unique_products = 0
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    # def __repr__(self):
    #     return f'Product {self.name}, {self.description}, {self.__price}, {self.quantity}, {self.color}'

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            total_amount = self.__price * self.quantity + other.__price * other.quantity
            return total_amount
        raise TypeError

    @classmethod
    def add_new_product(cls, name, description, price, quantity, color):
        """Создает товар и возвращает объект, который можно добавлять в список товаров"""
        return cls(name, description, price, quantity, color)

    @property
    def price(self):
        """Геттер для атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для атрибута цены"""
        if new_price <= 0:
            print("Цена введена некорректно")
        elif new_price > self.__price:
            self.__price = new_price
        else:
            while True:
                user_answer = input("Подтвердите понижение цены: y/n")
                if user_answer == 'y':
                    self.__price = new_price
                    print('Цена изменилась')
                    break
                elif user_answer == 'n':
                    print('Цена не изменилась')
                    break
                else:
                    print('Введите корректный ответ')

    def add_product(self, list_of_products):
        """Проверяет кол-во товара схожего по имени. В случае, если товар уже существует, складывает кол-во в наличии
        старого товара и нового. При конфликте цен выбирает более высокую цену."""

        for prod in list_of_products:
            if prod.name == self.name:
                prod.quantity += self.quantity
                if self.price > prod.price:
                    prod.price = self.price


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, productivity, model, memory, color):
        self.productivity = productivity
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)

    def __add__(self, other):
        if isinstance(other, Smartphone):
            total_amount = self.__price * self.quantity + other.__price * other.quantity
            return total_amount
        raise TypeError

    @classmethod
    def add_new_product(cls, name, description, price, quantity, productivity, model, memory, color):
        """Создает товар и возвращает объект, который можно добавлять в список товаров"""
        return cls(name, description, price, quantity, productivity, model, memory, color)


class Grass(Product):
    def __init__(self, name, description, price, quantity, country, terms, color):
        self.country = country
        self.terms = terms
        super().__init__(name, description, price, quantity, color)

    def __add__(self, other):
        if isinstance(other, Grass):
            total_amount = self.price * self.quantity + other.price * other.quantity
            return total_amount
        raise TypeError

    @classmethod
    def add_new_product(cls, name, description, price, quantity, country, term, color):
        """Создает товар и возвращает объект, который можно добавлять в список товаров"""
        return cls(name, description, price, quantity, country, term, color)


class CategoryIter:
    """Принимает на вход категорию и дает возможность использовать цикл for для прохода по всем товарам данной
    категории"""

    def __init__(self, name, products):
        self.name = name
        self.__products = products
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.__products):
            raise StopIteration
        else:
            return self.__products[self.index]


# category_1 = Category('Пылесосы',
#                       'убираются',
#                       [Product('Dyson', 'black', 10000, 12, 'white'),
#                        Product('Xiaomi', 'blue', 25000, 10, 'black')])

# Vacuum_cleaners = CategoryIter(category_1.name, category_1.products)
# for item in Vacuum_cleaners:
#     print(item)
#
gr = Grass("Полынь", "ввв", 10000, 2, "Рос", 2, "зеленая")
print(gr.__repr__())
# gr1 = Grass("Полынь2", "ввв", 5000, 3, "Рос", 2, "зеленая")
# print(gr.price)
# print('*')
# res = gr + gr
# print(res)
#
sm = Smartphone('LG', 'ddd', 30000, 5, 'ddd', 'x', '32', 'blue')
print(sm.__repr__())
# print(type(sm))
# res = gr + sm

# print(category_1)
product_1 = Product('Dyson', 'black', 10000, 12, 'green')
print(product_1.__repr__())
# product_2 = Product.add_new_product('Xiaomi', 'white', 7000, 2, 'purple')
# print(product_2)
# product_2.price = 5000
# print(product_2)
# # product_2.add_product(category_1.products)
# print(category_1.products)
# category_1.updated_products = product_2
# print(category_1.updated_products)
# print(str(category_1))
# print(len(category_1))
#
# print(product_1.price)
# product_1.price = 0
# print(product_1.price)

# total = product_1 + product_2
# print(total)
