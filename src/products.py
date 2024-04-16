class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int):
        new_product = cls(name, description, price, quantity)
        return new_product

    @property
    def price(self):
        pass

    @price.setter
    def price(self, value):
        pass