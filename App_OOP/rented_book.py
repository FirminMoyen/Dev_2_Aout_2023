import datetime
from book import Book
from customer import Customer


class Rented_book:
    def __init__(self, customer, book):

        if not isinstance(customer, Customer):
            raise ValueError(
                "The provided customer object is not an instance of the Customer class.")
        if not isinstance(book, Book):
            raise ValueError(
                "The provided book object is not an instance of the Book class.")

        self.customer = customer
        self.book = book
        self.date = datetime.datetime.today().strftime('%Y-%m-%d')

    @property
    def info(self):
        return '{}, rented by {} on the {}'.format(self.book.title, self.customer.full_name, self.date)
