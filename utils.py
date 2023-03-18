import json

from main import hh_request


def json_writer():
    with open('data.json', 'w') as file:
        json.dump(hh_request(), file, ensure_ascii=False)


json_writer()