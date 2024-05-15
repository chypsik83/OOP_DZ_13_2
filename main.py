from src.category import Category
from src.grass import Grass
from src.products import Product
from src.smartphone import Smartphone

if __name__ == '__main__':
    category = Category('Смартфоны',
                        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                        [{
                            "name": "Samsung Galaxy C23 Ultra",
                            "description": "256GB, Серый цвет, 200MP камера",
                            "price": 180000.0,
                            "quantity": 5
                        }])

    name_category = Category("Смартфоны",
                             "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",

                             [Product("Samsung Galaxy C23 Ultra",
                                      "256GB, Серый цвет, 200MP камера",
                                      180000.0,
                                      5
                                      )])

    print(name_category)

    object_1 = Product("Смартфоны",
                       "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                       50000.0, 2)
    object_2 = Product("Телевизоры",
                       "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                       60000.0, 2)
    object_3 = object_1 + object_2
    print(f"Сумма всего: {object_3}")

    Samsung_Galaxy_C23_Ultra = Smartphone('Samsung Galaxy C23 Ultra', '200MP камера', 180000.0, 10, 12, "256GB", 256,
                                          "Серый")

    print(Samsung_Galaxy_C23_Ultra)
    smartphone = Smartphone("iPhone 12", "256GB, Серый цвет, 200MP камера", 180000.0, 15, 54, "А15", 256, "Белый")
    lawn_grass = Grass("Bermuda Grass", "Широкая", 1200, 10, "мануфактура", "03,05,2024", "Зеленая")

    print(smartphone)
    print(lawn_grass)
    try:
        zero_quantity = Product("Телевизоры",
                                "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                                60000.0, 0)
    except ValueError as e:
        print(e)

    category_1 = Category("Смартфоны",
                          "Описание_1",

                          [])
    # category_1.add_product(Product("Смартфоны",
    #                             "Описание_1",
    #                            0, 3))
    # category_1.add_product(Product("Телевизоры",
    #                          "Описание_2",
    #                          0, 2))
    print(int(category_1.calculate_price()))
