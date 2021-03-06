import json
import sys


def load_data(filepath):
    with open(filepath) as file:
        json_string = file.read()
        return json.loads(json_string)


def pretty_print_decoded_json(python_object):
    print(
        json.dumps(python_object, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        data_from_file = load_data(path)
        pretty_print_decoded_json(data_from_file)
    except IndexError:
        print('Требуется путь к файлу как аргумент')
    except FileNotFoundError:
        print('Файл не найден')
    except json.decoder.JSONDecodeError:
        print('Файл содержит данные не в формате json')
