import json
from pprint import pprint
from request_classes import main


class Vacancy:

    def __init__(self, data):
        pass

    def json_w(self):
        with open('data.json', 'w+', encoding='utf-8') as file:
            data = {'name': self.name, 'url': self.url, 'city': self.city, 'salary': self.salary}
            json.dump(data, file, ascii=4)

    def __str__(self):
        return f'Вакансия - {self.name}, заработная плата - {self.salary} \n;'


class HHVacancy(Vacancy):
    def __init__(self, data):
        super().__init__(data)

    def get_data(self):
        pass

    def __repr__(self):
        return f"HH: {self.name}, зарплата: {self.salary} руб/мес \n;"

    def __str__(self):
        return f'HH: {self.name}, зарплата: {self.salary} руб/мес \n;'


class SJVacancy(Vacancy):
    def __init__(self, data):
        super().__init__(data)
        self.sort_list = []


    def get_data(self):
        vacansies_list = []
        data_list = data['SJ']
        for i in range(len(data_list)):
            name = data_list[i]['profession']
            city = data_list[i]['town']['title']
            url = data_list[i]['link']
            salary_from = data_list[i]['payment_from']
            salary_to = data_list[i]['payment_to']
            vacansies_list.append({'name': name, 'city': city, 'url': url, 'salary': [salary_from, salary_to]})
        return vacansies_list

    def __ge__(self, other):
        return self >= other

    def __repr__(self):
        return f"SJ: {self.name}, зарплата: {self.salary} руб/мес \n;"

    def __str__(self):
        return f'SJ: {self.name}, зарплата: {self.salary} руб/мес \n;'


def start():
    data = main()
    s = SJVacancy(data)
    data1 = s.get_data()
    # v = Vacancy(data1)
    # v.json_w()


start()
