import json
from request_classes import HeadHunter, SuperJob
from vacancy_classes import Vacancy, HHVacancy, SJVacancy
from operator import itemgetter


def main(user_input):
    """
    Очищает json-файл(если его нет, то создаёт).
    Запрашивает поисковый запрос пользователя.
    Создаёт экземпляры классов HH и SuperJob.
    Создаёт экземпляры классов HHVacancy и SJVacancy.
    Записывает данные в json-файл.
    """
    open("data.json", "w").close()
    user_query = input('Введите запрос для поиска: ')
    if user_input == '1':
        hh = HeadHunter(user_query)
        data = {'HH': hh.get_request()}
        hh = HHVacancy(data)
        json_dump = {'HH': hh.get_data()}
    elif user_input == '2':
        sj = SuperJob(user_query)
        data = {'SJ': sj.get_request()}
        sj = SJVacancy(data)
        json_dump = {'SJ': sj.get_data()}
    else:
        hh = HeadHunter(user_query)
        sj = SuperJob(user_query)
        data = {'HH': hh.get_request(), 'SJ': sj.get_request()}
        hh = HHVacancy(data)
        sj = SJVacancy(data)
        json_dump = {'HH': hh.get_data(), 'SJ': sj.get_data()}
    with open('data.json', 'w+', encoding='utf-8') as file:
        json.dump(json_dump, file, indent=4, ensure_ascii=False)


class Sort:
    """
    При необходимости сортирует по зарплате и выводит
    список с N-количеством топ вакансий.
    """
    def __init__(self, quantity_vacansies):
        self.quantity_vacansies = int(quantity_vacansies)
        self.top_salary_list = []

    def top_hh(self):
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in range(len(data['HH'])):
                if data['HH'][str(i + 1)]['salary'] == 'Не указана' or data['HH'][str(i + 1)]['salary'] is None:
                    continue
                else:
                    self.top_salary_list.append(data['HH'][str(i + 1)])
        sort_list = sorted(self.top_salary_list, key=itemgetter('salary'), reverse=True)[:self.quantity_vacansies]
        return sort_list

    def top_sj(self):
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for i in range(len(data['SJ'])):
                self.top_salary_list.append(data['SJ'][str(i + 1)])
        sort_list = sorted(self.top_salary_list, key=itemgetter('salary'), reverse=True)[:self.quantity_vacansies]
        return sort_list


class PrintVacancy:
    """
    Выводит строковое значение топ вакансий
    """
    def __init__(self, user_quantity):
        self.s = Sort(user_quantity)

    def top_hh(self):
        for i in self.s.top_hh():
            v = Vacancy(i)
            print(v.__ge__(i['salary']))
            print(v)

    def top_sj(self):
        for i in self.s.top_sj():
            v = Vacancy(i)
            print(v.__ge__(i['salary']))
            print(v)
