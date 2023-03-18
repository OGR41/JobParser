from abc import ABC, abstractmethod
from client_api import HH_API_KEY, SUPERJOB_API_KEY
import requests


class Engine(ABC):
    def __init__(self, search_query):
        self.search_query = search_query

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
            """ Возвращает экземпляр класса Connector """
            pass

    def __repr__(self):
        pass


class HH(Engine):
    def __init__(self, search_query):
        super().__init__(search_query)

    def get_request(self):
        headers = {"User-Agent": HH_API_KEY}
        params = {"text": f"{self.search_query}"}
        vacancy_list = requests.get(f'https://api.hh.ru/vacancies/',
                                    headers=headers,
                                    params=params)
        return vacancy_list.json()


class Superjob(Engine):
    def __init__(self, search_query):
        super().__init__(search_query)

    def get_request(self):
        headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        params = {"keyword": f"{self.search_query}"}
        vacancy_list = requests.get(f'https://api.superjob.ru/2.0/vacancies/',
                                    headers=headers,
                                    params=params)
        return vacancy_list.json()
