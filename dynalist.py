import json

class Node :
    name = ""
    children = []
    parent = None

    def __init__(self, name) :
        self.name = name

def print_data(data, depth=0):
    if isinstance(data, list):
        for value in data:
            print_data(value, depth)
        return

    print ('\t' * depth) + data.get("name")
    print_data(data.get("children"), depth+1)


if __name__ == '__main__':
    with open("data.json", "r") as f:
        d = json.load(f)
    print_data(d)
