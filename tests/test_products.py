import pytest

from src.products import Product


@pytest.fixture
def product1():
    return Product("Iphone 15", "512GB, Gray space", 19990.0, 8)


@pytest.fixture
def product2():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_init(product2):
    assert product2.name == "Samsung Galaxy C23 Ultra"
    assert product2.description == "256GB, Серый цвет, 200MP камера"
    assert product2.price == 180000.0
    assert product2.quantity == 5


def test_create_product(product1):
    product1.price = 0
    assert product1.price == 19990.0
    product1.price = 12000.0
    assert product1.price == 12000.0


def test_str():
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product) == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5'


def test_add():
    product1 = Product("Iphone 15", "512GB, Gray space", 100.0, 5)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 500, 2)
    for_add = product1 + product2
    assert for_add == 1500.0
