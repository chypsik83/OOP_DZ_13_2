from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @classmethod
    @abstractmethod
    def prod(cls, *args, **kwargs):
        pass
