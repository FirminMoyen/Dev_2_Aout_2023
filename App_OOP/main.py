from data import Data
from book import Book
from customer import Customer


if __name__ == "__main__":

    data = Data()

    data.add_book('jsp', 'rolala', 12)

    print(data.book_list[2].info)

    print(data.get_book_index_by_title('Eragon'))

    data.print_book_list()

    print("")

    data.remove_book('Eragon')

    print("")

    data.print_book_list()
