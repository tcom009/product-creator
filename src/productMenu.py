from bullet import Input, Numbers  # and etc...
from src.fileWriter import submit_data
# Create a Bullet or Check object
shipping_costs = {
    "local": 0,
    "provinces": 0
}

new_product = {
    "shipping_costs": shipping_costs
}


def product_menu():
    new_product["name"] = Input('Product name: ').launch()
    new_product["price"] = Numbers('Product unit price: ').launch()
    new_product["description"] = Input('Product decription: ').launch()
    shipping_costs["local"] = Numbers('Local shipping cost: ').launch()
    shipping_costs["provinces"] = Numbers('Provinces shipping cost: ').launch()

    submit_data(new_product)
