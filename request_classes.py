from client_api import HH_API_KEY, SUPERJOB_API_KEY
from abc import ABC, abstractmethod
import requests


class Engine(ABC):

    def __init__(self, search_query):
        self.page = 0
        self.pages_number = 10
        self.search_query = search_query

    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, search_query):
        super().__init__(search_query)
        self.hh_headers = {"User-Agent": HH_API_KEY}
        self.params = {'text': self.search_query,
                       'per_page': 100,
                       'page': self.page}

    def get_request(self):
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
    def __init__(self, search_query):
        super().__init__(search_query)
        self.sj_headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        self.params = {'keywords': search_query,
                       'count': 100,
                       'page': self.page}

    def get_request(self):
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


def main():
    if __name__ == '__main__':
        user_query = input('Введите запрос для поиска: ')
        h = HH(user_query)
        s = SuperJob(user_query)
        data = {'HH': h.get_request(), 'SJ': s.get_request()}
        return data['SJ']


main()
