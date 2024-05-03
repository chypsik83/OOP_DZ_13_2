class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, prod_dict):
        name = prod_dict["name"]
        description = prod_dict["description"]
        price = prod_dict["price"]
        quantity = prod_dict["quantity"]
        new_product = cls(name, description, price, quantity)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("цена введена некорректная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        if self.quantity == 0 or other.quantity == 0:
            raise ValueError('Нельзя складывать товары с нулевым количеством!')
        if type(other) == self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity

        raise TypeError('Нельзя складывать продукты разных типов')


