import pytest

from src.category import Category


@pytest.fixture
def category(products):
    return Category("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", ["Смартфоны", "Телевизоры"])


def test__init(category, products):
    assert category.name == "Samsung Galaxy C23 Ultra"
    assert category.description == "256GB, Серый цвет, 200MP камера"
    assert category.products == products


def test_category(category, products):
    assert Category.total_categories == 1

