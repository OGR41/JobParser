import json
from operator import itemgetter
import requests

from main import HHVacancy, SJVacancy
from pprint import pprint


def json_writer():
    user_input = input('Введите поисковой запрос: ')
    hh = HHVacancy(user_input)
    sj = SJVacancy(user_input)

    with open('data.json', 'w', encoding='utf-8') as file:
        data = {'HH': hh.hh_request(), 'SJ': sj.sj_request()}
        json.dump(data, file, indent=4, ensure_ascii=False)


json_writer()
