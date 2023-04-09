from client_api import HH_API_KEY, SUPERJOB_API_KEY

from abc import ABC, abstractmethod

import requests


class Engine(ABC):
    """
    Абстрактный класс
    """
    def __init__(self, search_query):
        """
        page = начальная страница
        pages_number = количество страниц для поиска
        search_query = поисковый запрос пользователя
        """
        self.page = 0
        self.pages_number = 10
        self.search_query = search_query

    @abstractmethod
    def get_request(self):
        pass


class HeadHunter(Engine):
    """
    Запрашивает данные на HH
    """
    def __init__(self, search_query):
        super().__init__(search_query)
        self.hh_headers = {"User-Agent": HH_API_KEY}
        self.params = {'text': self.search_query,
                       'per_page': 100,
                       'page': self.page}

    def get_request(self):
        """
        Создаёт список для полученных данных.
        Запускает итерацию по страницам.
        :return: Список с полученными с HH данными
        """
        vacancies_list = []
        while self.page < self.pages_number:
            response = requests.get('https://api.HH.ru/vacancies/',
                                    headers=self.hh_headers,
                                    params=self.params).json()
            self.page += 1
            vacancies = response['items']
            for vacancy in vacancies:
                vacancies_list.append(vacancy)
        return vacancies_list


class SuperJob(Engine):
    """
    Запрашивает данные на SuperJob
    """
    def __init__(self, search_query):
        super().__init__(search_query)
        self.sj_headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        self.params = {'keywords': search_query,
                       'count': 100,
                       'page': self.page}

    def get_request(self):
        """
        Создаёт список для полученных данных.
        Запускает итерацию по страницам.
        :return: Список с полученными с SuperJob данными
        """
        vacancies_list = []
        while self.page < self.pages_number:
            response = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                    headers=self.sj_headers,
                                    params=self.params).json()
            self.page += 1
            vacancies = response['objects']
            for vacancy in vacancies:
                vacancies_list.append(vacancy)
        return vacancies_list
