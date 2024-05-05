from src.print_mixin import PrintMixin
from src.products import Product


class Smartphone(Product, PrintMixin):

    def __init__(self, name: str, description: str, price: float, quantity: int, perfomance: int, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)

        self.perfomance = perfomance
        self.model = model
        self.memory = memory
        self.color = color

    def get_details(self):
        return f"{self.name} - {self.description}, ${self.price} - {self.description}"

    def __repr__(self):
        return super().__repr__()