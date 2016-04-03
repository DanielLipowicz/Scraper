import json


def read_json_file(file):
    with open(file, encoding='utf-8') as data_file:
        data_file_readed = data_file.read()
        data = json.loads(data_file_readed)
    return data
