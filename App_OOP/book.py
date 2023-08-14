
class Book():
    def __init__(self, title, autor, stock):

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title should be a non-empty string.")
        if not isinstance(autor, str) or not autor.strip():
            raise ValueError("Author should be a non-empty string.")
        if not isinstance(stock, int):
            raise ValueError("Stock should be an integer.")

        self.title = title
        self.autor = autor
        self.stock = stock

    @property
    def info(self):
        return '{} writen by {}, {} remaining'.format(self.title, self.autor, self.stock)
