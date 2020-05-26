
class Taggable:
    @staticmethod
    def tag(self):
        pass
        
class Book(Taggable):
    count = 0
    def __init__(self, author, name):
        if not name  or  not author:
            raise ValueError("Book(\"KekLand\",\"Kek I.O\")")  
        Book.count += 1
        self.name = name
        self.author = author
        self.code = Book.count

    def tag(self):
        return [i for i in self.name.split() if i.istitle()]

    def __str__(self):
        return "[%d] %s '%s'" % (self.code, self.author, self.name)