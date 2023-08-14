from book import Book
from customer import Customer


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
        book_to_remove = self.get_book_index_by_title(title)
        self.book_list.remove(self.book_list[book_to_remove])


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
        customer_to_remove = self.get_customer_index_by_full_name(full_name)
        self.customer_list.remove(self.customer_list[customer_to_remove])
