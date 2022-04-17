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
    casevalues = data_frame[data_frame.name.str.contains(
        name, flags=re.IGNORECASE)].values
    options = []
    for result in casevalues:
        options.append(result[0])
    menu = Bullet(choices=options)
    result = menu.launch()

    # print(type(casevalues))
    # print(casevalues)


def showData(product_name):
    searchData(product_name)


def searchMenu():
    name = Input("Product name: ").launch()
    showData(name)
