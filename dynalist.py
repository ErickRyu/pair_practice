import json

FILE_NAME = 'data.json'
CD = 'cd'
APPEND = 'app'
LS = 'ls'
COMMANDS = frozenset([
    CD,
    APPEND,
    LS,
])

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


def append_data(name, siblings):
    a = {"name" : name, "children" : []}
    siblings.append(a)


def save_file(data):
    json_str = json.dumps(data, indent=4, sort_keys=True)
    with open(FILE_NAME, 'w') as f:
        f.write(json_str)


def find_node(data, node_name):
    if not node_name:
        return data

    if not isinstance(data, dict):
        raise TypeError

    if 'children' not in data:
        raise ValueError

    for value in data.get('children', []):
        if value.get("name") == node_name:
            return value
    return None


if __name__ == '__main__':
    with open(FILE_NAME, "r") as f:
        d = json.load(f)

    current_node = d
    while True:
        input_comamnd = raw_input()
        args = input_comamnd.split()
        command = args[0]
        if command not in COMMANDS:
            print('Not found command')
            continue
        try:
            arg = args[1]
        except IndexError:
            arg = None

        if command == CD:
            current_node = find_node(current_node, arg)
        elif command == APPEND:
            append_data(arg, current_node)
            save_file(current_node)
            print_data(current_node)
        elif command == LS:
            print_data(find_node(current_node, arg))
