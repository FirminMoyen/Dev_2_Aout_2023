
class Book():
    def __init__(self, title, autor, stock):
        self.title = title
        self.autor = autor
        self.stock = stock

    @property
    def info(self):
        return '{} writen by {}, {} remaining'.format(self.title, self.autor, self.stock)
