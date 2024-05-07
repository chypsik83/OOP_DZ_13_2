
from src.products import Product


class Grass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, manufacturer: str, period: str,
                 color: str):
        self.manufacturer = manufacturer
        self.period = period
        self.color = color
        super().__init__(name, description, price, quantity)
