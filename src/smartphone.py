
from src.products import Product


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, perfomance: int, model: str,
                 memory: int, color: str):
        self.perfomance = perfomance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)
