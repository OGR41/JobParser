from abc import ABC, abstractmethod
from client_api import HH_API_KEY, SUPERJOB_API_KEY
import requests


class Vacancy:
    def __init__(self, search_query, title=None, url=None, description=None, salary=None):
        self.search_query = search_query
        self.title = title  # s.get_request()['objects'][0]['profession']
        self.url = url  # s.get_request()['objects'][0]['link']
        self.description = description  # s.get_request()['objects'][0]['candidat']
        self.salary = salary  # s.get_request()['objects'][0]['payment_from'], s.get_request()['objects'][0]['payment_to']

    def __repr__(self):
        return f"{self.title}, {self.url}, {self.description}, {self.salary}"


class HH(Vacancy):
    def __init__(self, search_query):
        super().__init__(search_query)

    def get_request(self):
        headers = {"User-Agent": HH_API_KEY}
        params = {"text": f"{self.search_query}"}
        vacancy_list = requests.get(f'https://api.hh.ru/vacancies/',
                                    headers=headers,
                                    params=params)
        return vacancy_list.json()


class Superjob(Vacancy):
    def __init__(self, search_query):
        super().__init__(search_query)

    def get_request(self):
        headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        params = {"keyword": f"{self.search_query}"}
        vacancy_list = requests.get(f'https://api.superjob.ru/2.0/vacancies/',
                                    headers=headers,
                                    params=params)
        return vacancy_list.json()
