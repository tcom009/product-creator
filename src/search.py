import numpy as np
import pandas as pd
from src.fileWriter import read_file
file = read_file()

data_frame = pd.DataFrame(file)


def showData():
    print(data_frame)
