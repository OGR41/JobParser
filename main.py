from classes import SuperJob, HH
from pprint import pprint


class Vacancy:
    # __slots__ = ...

    def __init__(self, user_input):
        self.user_input = user_input
        self.vacancy_list = []

    def __str__(self):
        pass


class CountMixin:
    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass


class HHVacancy(Vacancy):
    def __init__(self, user_input):
        super().__init__(user_input)
        
    def hh_request(self):
        hh = HH(self.user_input)
        hh_list = hh.get_request()
        for i in range(len(hh_list)):
            name = hh_list[i]['name']
            url = hh_list[i]['alternate_url']
            responsibility = hh_list[i]['snippet']['responsibility']
            if hh_list[i]['salary'] is None:
                salary = None
            else:
                salary = hh_list[i]['salary']
            data = {i + 1: {"Вакансия": name, "Ссылка": url, "Описание": responsibility, "Зарплата": salary}}
            self.vacancy_list.append(data)
        return self.vacancy_list


class SJVacancy(Vacancy):
    def __init__(self, user_input):
        super().__init__(user_input)

    def sj_request(self):
        sj = SuperJob(self.user_input)
        sj_list = sj.get_request()
        for i in range(len(sj_list)):
            name = sj_list[i]['profession']
            url = sj_list[i]['link']
            responsibility = sj_list[i]['candidat']
            salary_from = sj_list[i]['payment_from']
            salary_to = sj_list[i]['payment_to']
            data = {i + 1001: {"Вакансия": name, "Ссылка": url, "Описание": responsibility,
                               "Зарплата": f'от {salary_from} до {salary_to}'}}
            self.vacancy_list.append(data)

        return self.vacancy_list
