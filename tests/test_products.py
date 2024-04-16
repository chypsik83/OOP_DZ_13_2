import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def products():
    return [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)]


def test_product(products):
    assert Category.counter_product == 0


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_init(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == None
    assert product.quantity == 5


@pytest.fixture
def create():
    return Product("Iphone 15", "512GB, Gray space", 19990.0, 8)


def test_create_product(create):
    create.price = 19990.0
    assert create.price == None
    assert create.name == "Iphone 15"
    assert create.description == "512GB, Gray space"
