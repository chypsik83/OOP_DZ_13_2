from src.category import Category
from src.products import Product

category = Category('Смартфоны',
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    [{
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5
                    }])

name_1 = Product("Samsung Galaxy C23 Ultra",
                 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                 180000.0, 5)

print(name_1)

name_category = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
<<<<<<< HEAD
                         [Product("Samsung Galaxy C23 Ultra",
                                  "256GB, Серый цвет, 200MP камера",
                                  180000.0,
                                  5
                                  )])
print(len(name_category))

# apple = Product.create_product({
# "name": "Samsung Galaxy C23 Ultra",
# "description": "256GB, Серый цвет, 200MP камера",
# "price": 180000.0,
# "quantity": 5
# })
# category.add_product(apple)

# print(apple)
print(category.products)

object_1 = Product("Смартфоны",
                   "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                   50000.0, 2)
object_2 = Product("Телевизоры",
                   "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                   60000.0, 2)
object_3 = object_1 + object_2
print(f"Сумма всего: {object_3}")
=======
                         [{
                             "name": "Samsung Galaxy C23 Ultra",
                             "description": "256GB, Серый цвет, 200MP камера",
                             "price": 180000.0,
                             "quantity": 5
                         }])
print(len(name_category))

apple = Product.create_product({
    "name": "Samsung Galaxy C23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5
})
category.add_product(apple)

print(apple)
print(category.products)

object_1 = Product("Смартфоны","Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", 50000.0, 2)
object_2 = Product("Телевизоры","Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",60000.0, 2)
object_3 = object_1 + object_2
print(f"Сумма всего: {object_3}")


>>>>>>> origin/main
