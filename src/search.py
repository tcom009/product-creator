
import numpy as np
import pandas as pd
from bullet import Input
from src.fileWriter import read_file


def searchData(name):
    file = read_file()
    file = pd.json_normalize(file)
    data_frame = pd.DataFrame(file)
    print(data_frame[data_frame["name"] == name])


def showData(product_name):
    print(searchData(product_name))


def searchMenu():
    name = Input("Product name: ").launch()
    showData(name)
