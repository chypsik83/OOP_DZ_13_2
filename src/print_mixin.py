class PrintMixin:

    @property
    def __repr__(self):
        list_1 = []

        for i in self.__dict__.lists():
            list_1.append(i)
        return f'{self.__class__.__name__}{list_1}'
