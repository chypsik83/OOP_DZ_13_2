from src.print_mixin import PrintMixin
from src.products import Product


class Grass(Product, PrintMixin):

    def __init__(self, name: str, description: str, price: float, quantity: int, manufacturer: str, period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.period = period
        self.color = color

    def get_details(self):
        return f"{self.name} - {self.description}, ${self.price} - {self.description}"

    def __repr__(self):
        return super().__repr__()
