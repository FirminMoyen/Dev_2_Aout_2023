from data import Data
from book import Book
from customer import Customer


if __name__ == "__main__":

    data = Data()

    print('printing book liste : ')
    print("")
    data.print_book_list()
    print("")

    print('adding a book : ')
    print("")
    data.add_book('da vinci code', 'dan brown', 20)
    data.print_book_list()
    print("")

    print('removing a book')
    print("")
    data.remove_book('coucou')
    data.print_book_list()
    print('')

    print('printing customer liste : ')
    print("")
    data.print_customer_list()
    print("")

    print('adding a customer : ')
    print("")
    data.add_customer('jean', 'dupount', 4321)
    data.print_customer_list()
    print('')

    print('removing customer : ')
    print("")
    data.remove_customer('Jhon Watson')
    data.print_customer_list()
    print('')

    print('adding first rent order')
    print('')
    data.rent_book('Eragon', 'Thelma Brasseur')
    data.print_rented_book()
    print('')
    print('renting a second book')
    print('')
    data.rent_book('da vinci code', 'Firmin Moyen')
    data.print_rented_book()
    print('')
    data.print_book_list()

    print('returning a book : ')
    print('')
    data.return_book(data.rented_list[0])
    print('')
    data.print_rented_book()
