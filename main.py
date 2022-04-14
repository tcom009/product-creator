from random import choices
from bullet import Bullet, Check, YesNo, Input  # and etc...
# Create a Bullet or Check object
choices = ["Create product", "Exit"]
cli = Bullet(prompt="Choose from the items below: ",
             choices=choices)
result = cli.launch()
if str(result) == choices[0]:
    product_name = input('Product name: ')
    print(product_name)
elif result == choices[1]:
    quit()
