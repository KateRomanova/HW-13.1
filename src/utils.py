import json


def load_products():
    """Загружает данные по категориям и товарам из файла JSON"""
    with open('/Users/Kate/PycharmProjects/Homework_13.1/src/products.json', 'r', encoding='utf-8') as p:
        products = json.load(p)

    return products




def count_categories():
    """Считает количество Категорий"""
    all_products = load_products()
    number_of_categories = len(all_products)
    return number_of_categories


def count_unique_products():
    """Считает количество уникальных продуктов"""
    all_products = load_products()
    number_of_unique_products = 0
    for p in all_products:
        number_of_unique_products += len(p['products'])
    return number_of_unique_products
