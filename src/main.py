from src.category import Category
from src.products import Product

category = Category('Смартфоны', "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", [])
apple = Product.create_product("Apple", "Последний айфон", 134000.0, 5)
category.add_product(apple)


print(apple)
print(category.get_products)
