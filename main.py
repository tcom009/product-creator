import functools
from operator import add
from simple_term_menu import TerminalMenu
from functools import reduce
from src.functions import get_labels

# main_menu = [
#     {"label": "> Añadir nuevo producto", "value": "CREATE_PRODUCT"},
#     {"label": "> Salir", "value": "EXIT"}
# ]


# menu_labels = (reduce(lambda accumulator, value: accumulator +
#                       [value["label"]], main_menu, []))

# the letter in the square brackets too can use to index the options
menu_labels = ['Añadir nuevo producto', 'Salir']


def add_product_name():

    product_name = input('Nombre')
    print(product_name)
    show_menu()


def show_menu():
    choice = menu_labels[TerminalMenu(
        menu_labels, title="Product creator", accept_keys=("y")).show()]

    if choice == 'Añadir nuevo producto':
        add_product_name()
    elif choice == menu_labels[1]:
        quit()


if __name__ == '__main__':
    show_menu()
