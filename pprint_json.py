import json
import sys


def load_data(filepath):
    json_string = open(filepath, 'r').read()
    return(json.loads(json_string))


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    path = sys.argv[1]
    data = load_data(path)
    pretty_print_json(data)
