import json

def writeFile(data):
    json_data = json.dumps(data, indent=4)
    with open("products.json", "r") as openfile:
        prev_data = json.load(openfile)
        prev_data = json.dumps(prev_data, indent=4)
        new_data = [prev_data].append(json_data)
    with open("products.json", "w") as outfile:
        outfile.write(json.dumps(new_data))
