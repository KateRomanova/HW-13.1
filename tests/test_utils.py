from src.utils import count_categories, count_unique_products


def test_count_categories():
    """Проверяет подсчет количества уникальных продуктов"""
    assert count_categories() == 2


def test_count_unique_products():
    assert count_unique_products() == 4