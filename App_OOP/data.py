from book import Book
from customer import Customer
from rented_book import Rented_book


class Data():
    def __init__(self):
        self.book_list = [Book('coucou', 'firmin', 12),
                          Book('bonjour', 'thelma', 15),
                          Book('Eragon', 'Paolini', 100)]

        self.customer_list = [Customer('Firmin', 'Moyen', 6761),
                              Customer('Thelma', 'Brasseur', 1348),
                              Customer('Jhon', 'Watson', 1234)]

        self.rented_list = []


### Book list related methodes ###

    def print_book_list(self):
        for book in self.book_list:
            print(book.info)

    def add_book(self, title, autor, stock):
        new_book = Book(title, autor, stock)
        self.book_list.append(new_book)

    def get_book_index_by_title(self, title):
        index = 0
        for book in self.book_list:
            if book.title == title:
                return index
            else:
                index += 1

    def remove_book(self, title):
        self.book_list = [
            book for book in self.book_list if book.title != title]


### customer list related methodes ###


    def print_customer_list(self):
        for customer in self.customer_list:
            print(customer.info)

    def add_customer(self, first_name, last_name, zip_code):
        new_customer = Customer(first_name, last_name, zip_code)
        self.customer_list.append(new_customer)

    def get_customer_index_by_full_name(self, full_name):
        index = 0
        for customer in self.customer_list:
            if customer.full_name == full_name:
                return index
            else:
                index += 1

    def remove_customer(self, full_name):
        self.customer_list = [
            customer for customer in self.customer_list if customer.full_name != full_name]

### renting and returning books related methodes ###

    def print_rented_book(self):
        for rent_order in self.rented_list:
            print(rent_order.info)

    def rent_book(self, book_title, customer_full_name):
        book = self.book_list[self.get_book_index_by_title(book_title)]

        customer = self.customer_list[self.get_customer_index_by_full_name(
            customer_full_name)]

        if book.stock > 0:
            new_rent_order = Rented_book(customer, book)
            self.rented_list.append(new_rent_order)
            book.stock = book.stock - 1
        else:
            print('{} is not available anymore').format(book.title)

    def return_book(self, rent_order):
        self.rented_list = [
            order for order in self.rented_list if order.book != rent_order.book or order.customer != rent_order.customer]
