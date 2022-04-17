import numpy as np
import pandas as pd
from bullet import Input
from src.fileWriter import read_file
import re
from bullet import Bullet

options = []


def getValues(result):
    for option in options:
        if option == result:
            return option


def searchData(name):
    file = read_file()
    file = pd.json_normalize(file)
    data_frame = pd.DataFrame(file)
    casevalues = data_frame[data_frame.name.str.contains(
        name, flags=re.IGNORECASE)].values
    for case in casevalues:
        options.append(case[0])
    menu = Bullet(choices=options)
    bullet_result = menu.launch()
    id = ""
    for case in casevalues:
        if case[0] == bullet_result:
            id = case[3]
    if bullet_result == getValues(bullet_result):
        edit(id)



def showData(product_name):
    searchData(product_name)


def searchMenu():
    name = Input("Product name: ").launch()
    showData(name)


def edit(id):
    print(f"You are editing {id}")
