import json
from operator import itemgetter
import requests

from main import HHVacancy, SJVacancy
from pprint import pprint


def json_writer():
    """
    Записывает полученные данные в json-файл
    """

    # предлагаем ввести запрос для поиска вакансий
    user_input = input('Введите поисковой запрос: ')

    # создаем экземпляры классов HHVacancy и SJVacancy
    hh = HHVacancy(user_input)
    sj = SJVacancy(user_input)

    # записываем в json-файл полученные данные
    with open('data.json', 'w', encoding='utf-8') as file:
        data = {'HH': hh.hh_request(), 'SJ': sj.sj_request()}
        json.dump(data, file, indent=4, ensure_ascii=False)


json_writer()
