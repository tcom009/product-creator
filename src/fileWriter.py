import json
from uuid import uuid4
from os.path import exists


def write_file(data):

    with open("products.json", "w") as json_file:
        json_file.write(json.dumps(data))


def read_file():
    """
    returns data parsed into a python list
    if the file doesn't exists create a new one as empty array
    todo: Add a variable to get the file name
    """
    file_exists = exists("products.json")

    if file_exists:
        with open("products.json", "r") as json_file:
            prev_data = json.load(json_file)
    else:
        write_file([])
        prev_data = []
    return prev_data


def submit_data(new_data):
    prev_data = read_file()
    id = str(uuid4())
    new_data["id"] = id
    prev_data.append(new_data)
    write_file(prev_data)
