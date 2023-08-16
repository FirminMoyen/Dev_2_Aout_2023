import os
import time
from book import Book
from customer import Customer
from rented_book import Rented_book

# done


def cls():
    os.system("cls" if os.name == "nt" else "clear")

# done


def add_customer_menu(data):
    cls()
    first_name = input('What is the first name of this new customer ?')
    cls()
    last_name = input('What is the last name of this new customer ?')
    cls()
    while True:
        try:
            zip_code = int(
                input('What is the zip code of this new customer ?'))
            cls()
            break
        except ValueError:
            print('zip code shoul be a number')

    data.add_customer(first_name, last_name, zip_code)
    print('New customer created !')
    time.sleep(2)
    show_customer_menu(data)


def rm_customer_menu(data):
    cls()
    print('Witch customer do you want to remove ?')
    print('')
    data.print_customer_full_name_list()
    print('')
    full_name = input('Full name of the customer :')

    data.remove_customer(full_name)

    cls()
    print("Customer removed !")
    time.sleep(2)
    show_customer_menu(data)

# done


def rm_book_menu(data):
    cls()
    print('Witch book do you want to remove ?')
    print('')
    data.print_book_list()
    print('')
    title = input('Title :')

    data.remove_book(title)

    cls()
    print("Book removed !")
    time.sleep(2)
    show_book_menu(data)


# done
def add_book_menu(data):
    cls()
    title = input('What is the title of the book ?')
    cls()
    autor = input('Who is the autor of this book ?')
    cls()
    stock = int(input('How many books to add to stock ?'))
    cls()
    data.add_book(title, autor, stock)
    print('Book added sucessfuly !')
    time.sleep(2)
    cls()
    show_book_menu(data)

# done


def return_menu(data):
    cls()
    print('Witch book is beeing returned ?')
    print('')
    data.print_rented_book_title()
    print('')
    title = input('Title :')

    cls()
    print('Who is returning that book ?')
    print('')
    data.print_rented_book_customer_name(title)
    print('')
    name = input('Full name : ')

    index = data.get_rent_order_by_title_and_customer_name(title, name)

    data.return_book(data.rented_list[index])

    cls()
    print('Book returned')
    time.sleep(2)
    main_menu(data)


# done
def rented_list_menu(data):
    cls()
    print('Here are all the books currently rentd :')
    print('')
    data.print_rented_book()
    print('')
    print('(0) Go back')

    userinput = int(input(''))

    match userinput:
        case 0:
            main_menu(data)
        case _:
            print('Invalid Input, please try again')
            time.sleep(2)
            rented_list_menu(data)

# done


def rent_menu(data):
    cls()
    print('what book do you want to rent ?')
    print('')
    data.print_book_title_list()
    print('')
    book_title = input('Title :')

    cls()
    print('Who is renting that book ?')
    print('')
    data.print_customer_full_name_list()
    print('')
    customer_full_name = input('Full name of the customer :')

    data.rent_book(book_title, customer_full_name)

    cls()
    print('Book rented !')
    time.sleep(2)
    main_menu(data)

# done


def show_book_menu(data):
    cls()
    print('Here are all the books we have !')
    print('')
    data.print_book_list()
    print('')
    print('(1) add a book to the list')
    print('(2) remove a book from the list')
    print('')
    print('(0) Go back')

    userinput = int(input(''))

    match userinput:
        case 1:
            add_book_menu(data)
        case 2:
            rm_book_menu(data)
        case 0:
            main_menu(data)
        case _:
            print('Invalid Input, please try again')
            time.sleep(2)
            show_book_menu(data)

# done


def show_customer_menu(data):
    cls()
    print('Here are all our customers :')
    print('')
    data.print_customer_list()
    print('')
    print('(1) add a customer')
    print('(2) remove a customer')
    print('')
    print('(0) Go back')

    userinput = int(input(''))

    match userinput:
        case 1:
            add_customer_menu(data)
        case 2:
            rm_customer_menu(data)
        case 0:
            main_menu(data)
        case _:
            print('Invalid Input, please try again')
            time.sleep(2)
            show_customer_menu(data)

# done


def main_menu(data):
    cls()
    print('Hello, what do you want to do ?')
    print('')
    print('(1) see the book list')
    print('(2) see the customers list')
    print('(3) see the books currently rented')
    print('(4) rent a book')
    print('(5) return a book')
    print('')
    print('(0) Quit')

    userinput = int(input(''))

    match userinput:
        case 1:
            show_book_menu(data)
        case 2:
            show_customer_menu(data)
        case 3:
            rented_list_menu(data)
        case 4:
            rent_menu(data)
        case 5:
            return_menu(data)
        case 0:
            pass
        case _:
            print('Invalid Input, please try again')
            time.sleep(2)
            main_menu(data)
