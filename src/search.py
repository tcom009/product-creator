import numpy as np
import pandas as pd
from bullet import Input
from src.fileWriter import read_file
import re
from bullet import Bullet


def searchData(name):

    file = read_file()
    file = pd.json_normalize(file)
    data_frame = pd.DataFrame(file)
    search_results = data_frame[data_frame.name.str.contains(
        name, flags=re.IGNORECASE)].values
    # fill option list

    def getId(product_name, product_list):
        id = ""
        for product in product_list:
            if product[0] == product_name:
                id = product[3]
        return id

    def generate_options(result_values):
        options = []
        for result in result_values:
            options.append(result[0])
        return options

    options = generate_options(search_results)

    def getValues(result):
        if result in options:

            return result

    menu = Bullet(choices=options)
    # result from selection
    bullet_result = menu.launch()

    if bullet_result == getValues(bullet_result):
        edit(getId(bullet_result, search_results))


def showData(product_name):
    searchData(product_name)


def searchMenu():
    name = Input("Product name: ").launch()
    showData(name)


def edit(id):
    print(f"You are editing {id}")
