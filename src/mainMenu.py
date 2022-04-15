from bullet import Bullet, Check, YesNo, Input  # and etc...
# Create a Bullet or Check objectç
from src.productMenu import product_menu, printItems
main_menu_choices = ["Create product",
                     "Edit Product", "Remove Product", "Exit"]
main_menu = Bullet(prompt="Choose from the items below: ",
                   choices=main_menu_choices)
result = main_menu.launch()


def main_menu():
    if result == main_menu_choices[0]:
        product_menu()
        printItems()
    elif result == main_menu_choices[1]:
        print(result)
    elif result == main_menu_choices[2]:
        print(result)

    elif result == main_menu_choices[3]:
        quit()
