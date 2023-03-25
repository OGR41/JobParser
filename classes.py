from client_api import HH_API_KEY, SUPERJOB_API_KEY
import requests
from abc import ABC, abstractmethod
from pprint import pprint


class Engine(ABC):
    def __init__(self, search_query):
        self.search_query = search_query
        self.hh_headers = {"User-Agent": HH_API_KEY}
        self.sj_headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        self.pages_number = 50
        self.page = 0
        self.vacancies = []

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    def __init__(self, search_query):
        super().__init__(search_query)

    def get_request(self):
        while self.page < self.pages_number:
            params = {"text": self.search_query, "page": self.page}
            hh_openings = requests.get(f'https://api.HH.ru/vacancies/',
                                       headers=self.hh_headers,
                                       params=params).json()

            self.page += 1

            page_vacancies = hh_openings["items"]
            for vacancy in page_vacancies:
                self.vacancies.append(vacancy)
        return self.vacancies


class SuperJob(Engine):
    def __init__(self, search_query):
        super().__init__(search_query)

    def get_request(self):
        while self.page < self.pages_number:
            params = {"keyword": self.search_query, "page": self.page}
            js_openings = requests.get(f'https://api.superjob.ru/2.0/vacancies/',
                                       headers=self.sj_headers,
                                       params=params).json()

            self.page += 1
            page_vacancies = js_openings["objects"]
            for vacancy in page_vacancies:
                self.vacancies.append(vacancy)

        return self.vacancies
