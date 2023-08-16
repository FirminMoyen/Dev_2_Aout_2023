from book import Book
from customer import Customer
from rented_book import Rented_book


class Data():
    def __init__(self):
        self.book_list = [Book('Da Vinci Code', 'Dan Brown', 12),
                          Book('La Bible', 'Jesus', 15),
                          Book('Eragon', 'Paolini', 100)]
        self.customer_list = [Customer('Firmin', 'Moyen', 6761),
                              Customer('Jack', 'Adit', 1348),
                              Customer('Jhon', 'Watson', 1234)]
        self.rented_list = [
            Rented_book(
                self.customer_list[0], self.book_list[0]),
            Rented_book(
                self.customer_list[1], self.book_list[1]),
            Rented_book(
                self.customer_list[2], self.book_list[2])
        ]

    ### Book list related methods ###

    def print_book_list(self):
        for book in self.book_list:
            print(book.info)

    def add_book(self, title, autor, stock):
        if any(book.title == title for book in self.book_list):
            raise ValueError(
                f"A book with the title '{title}' already exists.")
        new_book = Book(title, autor, stock)
        self.book_list.append(new_book)

    def get_book_by_title(self, title):
        for book in self.book_list:
            if book.title == title:
                return book
        return None

    def remove_book(self, title):
        book = self.get_book_by_title(title)
        if not book:
            raise ValueError(f"No book with the title '{title}' found.")
        self.book_list.remove(book)

    ### customer list related methods ###

    def print_customer_list(self):
        for customer in self.customer_list:
            print(customer.info)

    def add_customer(self, first_name, last_name, zip_code):
        if any(c.full_name == f"{first_name} {last_name}" for c in self.customer_list):
            raise ValueError(
                f"A customer with the name '{first_name} {last_name}' already exists.")
        new_customer = Customer(first_name, last_name, zip_code)
        self.customer_list.append(new_customer)

    def get_customer_by_full_name(self, full_name):
        for customer in self.customer_list:
            if customer.full_name == full_name:
                return customer
        return None

    def remove_customer(self, full_name):
        customer = self.get_customer_by_full_name(full_name)
        if not customer:
            raise ValueError(f"No customer with the name '{full_name}' found.")
        self.customer_list.remove(customer)

    ### renting and returning books related methods ###

    def rent_book(self, book_title, customer_full_name):
        book = self.get_book_by_title(book_title)
        if not book:
            raise ValueError(f"No book with the title '{book_title}' found.")
        if book.stock <= 0:
            raise ValueError(f"'{book_title}' is not available anymore.")

        customer = self.get_customer_by_full_name(customer_full_name)
        if not customer:
            raise ValueError(
                f"No customer with the name '{customer_full_name}' found.")

        new_rent_order = Rented_book(customer, book)
        self.rented_list.append(new_rent_order)
        book.stock -= 1

    def return_book(self, rent_order):
        if rent_order not in self.rented_list:
            raise ValueError("This rent order does not exist.")
        self.rented_list.remove(rent_order)
        rent_order.book.stock += 1
