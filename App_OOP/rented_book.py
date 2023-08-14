import datetime


class Rented_book:
    def __init__(self, customer, book):
        self.customer = customer
        self.book = book
        self.date = datetime.datetime.today().strftime('%Y-%m-%d')

    @property
    def info(self):
        return '{}, rented by {} on the {}'.format(self.book.title, self.customer.full_name, self.date)
