class Library(object):

    def __init__(self, number, adress):
        self.adress = adress
        self.number = number
        self.books = []

    def __add__(self, book):
        self.books += [book]
        return self

    def __iadd__(self, book):
        return self.__add__(book)

    def __iter__(self):
        for book in self.books:
            yield book