import unittest
import sys
from io import StringIO
from data import Data
from rented_book import Rented_book
from book import Book


class TestData(unittest.TestCase):

    def setUp(self):
        """ This method is called before each test. It sets up the initial state for testing. """
        self.data = Data()

    ### Book list related tests ###

    def test_add_book(self):
        # Test adding a book
        self.data.add_book('New Book', 'New Author', 10)
        book = self.data.get_book_by_title('New Book')
        self.assertIsNotNone(book)
        self.assertEqual(book.title, 'New Book')
        self.assertEqual(book.autor, 'New Author')
        self.assertEqual(book.stock, 10)

        with self.assertRaises(ValueError):
            self.data.add_book('New Book', 'Another Author', 5)

    def test_remove_book(self):

        self.data.add_book('To be removed', 'Author', 5)
        self.data.remove_book('To be removed')
        book = self.data.get_book_by_title('To be removed')
        self.assertIsNone(book)

        with self.assertRaises(ValueError):
            self.data.remove_book('Non-existing Book')

    ### customer list related tests ###

    def test_add_customer(self):

        self.data.add_customer('New', 'Customer', 1234)
        customer = self.data.get_customer_by_full_name('New Customer')
        self.assertIsNotNone(customer)
        self.assertEqual(customer.first_name, 'New')
        self.assertEqual(customer.last_name, 'Customer')
        self.assertEqual(customer.zip_code, 1234)

        with self.assertRaises(ValueError):
            self.data.add_customer('New', 'Customer', 5678)

    def test_remove_customer(self):

        self.data.add_customer('To be removed', 'Customer', 1234)
        self.data.remove_customer('To be removed Customer')
        customer = self.data.get_customer_by_full_name(
            'To be removed Customer')
        self.assertIsNone(customer)

        with self.assertRaises(ValueError):
            self.data.remove_customer('Non-existing Customer')

    ### renting and returning books related tests ###

    def test_rent_book(self):

        self.data.rent_book('Da Vinci Code', 'Firmin Moyen')
        book = self.data.get_book_by_title('Da Vinci Code')
        self.assertEqual(book.stock, 11)

        with self.assertRaises(ValueError):
            self.data.rent_book('Non-existing Book', 'Firmin Moyen')

        with self.assertRaises(ValueError):
            self.data.rent_book('Da Vinci Code', 'Non-existing Customer')

    def test_return_book(self):

        rented_book = self.data.rented_list[0]
        self.data.return_book(rented_book)
        book = self.data.get_book_by_title(rented_book.book.title)
        self.assertEqual(book.stock, rented_book.book.stock)

        with self.assertRaises(ValueError):
            fake_rent_order = Rented_book(
                self.data.customer_list[0], self.data.book_list[0])
            self.data.return_book(fake_rent_order)


if __name__ == "__main__":
    unittest.main()
