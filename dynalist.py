import json

FILE_NAME = 'data.json'
CD = 'cd'
APPEND = 'app'
COMMANDS = frozenset([
    CD,
    APPEND,
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
    for value in data:
        if value.get("name") == node_name:
            return value
    return None


if __name__ == '__main__':
    with open(FILE_NAME, "r") as f:
        d = json.load(f)
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
            print_data(find_node(d, arg))
        elif command == APPEND:
            append_data(arg, d)
            save_file(d)
            print_data(d)
