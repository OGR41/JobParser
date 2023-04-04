from pprint import pprint
from request_classes import main


class Vacancy:

    def __init__(self, vacansies):
        self.name = vacansies['name']
        self.url = vacansies['url']
        self.city = vacansies['city']
        self.salary = vacansies['salary']

    def __str__(self):
        return f'Вакансия - {self.name}, заработная плата - {self.salary} \n;'


class HHVacancy(Vacancy):
    def __init__(self, vacansies):
        super().__init__(vacansies)

    def get_data(self):
        pass

    def __repr__(self):
        return f"HH: {self.name}, зарплата: {self.salary} руб/мес \n;"

    def __str__(self):
        return f'HH: {self.name}, зарплата: {self.salary} руб/мес \n;'


class SJVacancy(Vacancy):
    def __init__(self, vacansies):
        super().__init__(vacansies)

    def get_data(self):
        vacansies = []
        data_list = data['SJ']
        for i in range(len(data_list)):
            name = data_list[i]['profession']
            city = data_list[i]['town']['title']
            url = data_list[i]['link']
            salary_from = data_list[i]['payment_from']
            salary_to = data_list[i]['payment_to']
            vacansies.append({'name': name, 'city': city, 'url': url, 'salary': [salary_from, salary_to]})
        return vacansies

    def __repr__(self):
        return f"SJ: {self.name}, зарплата: {self.salary} руб/мес \n;"

    def __str__(self):
        return f'SJ: {self.name}, зарплата: {self.salary} руб/мес \n;'


data = main()
# pprint(data)
s = SJVacancy
data1 = s.get_data(data)
pprint(data1)
# v = Vacancy(data1)
# print(v)
