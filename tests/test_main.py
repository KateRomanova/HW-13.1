# Напишите тесты для классов, которые проверяют:
# подсчет количества продуктов, подсчет количества категорий.

from src.main import Category, Product
import pytest


@pytest.fixture()
def category_smartphones():
    return Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение '
                                 'дополнительных функций для удобства жизни', [list])


def test_init(category_smartphones):
    """Тест проверяет корректность инициализации объектов класса Category"""
    assert category_smartphones.name == 'Смартфоны'
    assert category_smartphones.description == ('Смартфоны, как средство не только коммуникации, но и получение '
                                                'дополнительных функций для удобства жизни')
    assert category_smartphones.products == [list]


@pytest.fixture()
def product_samsung():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0,
                   5, 'blue')


def test_init(product_samsung):
    """Тест проверяет корректность инициализации объектов класса Product"""
    assert product_samsung.name == 'Samsung Galaxy C23 Ultra'
    assert product_samsung.description == '256GB, Серый цвет, 200MP камера'
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


class TestCategory:
    number_of_categories = 7
    number_of_unique_products = 8


cat_1 = TestCategory


def test_category():
    assert cat_1.number_of_categories == 7
    assert cat_1.number_of_unique_products == 8
