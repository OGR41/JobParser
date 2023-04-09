
class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, sort_data):
        self.name = sort_data['name']
        self.area = sort_data['city']
        self.url = sort_data['url']
        self.salary = sort_data['salary']

    def __str__(self):
        return f'Вакансия - {self.name}, заработная плата - {self.salary} \n;'

    def __ge__(self, other):
        return self.salary >= other


class HHVacancy:

    def __init__(self, data):
        self.data = data['HH']

    def get_data(self):
        """
        Создаёт словарь, записывает в него необходимые данные
        (название вакансии, город, ссылка и зарплата)
        :return: словарь с данными
        """
        json_data = {}
        for i in range(len(self.data)):
            name = self.data[i]['name']
            city = self.data[i]['area']['name']
            url = self.data[i]['alternate_url']
            if self.data[i]['salary'] is not None:
                salary = self.data[i]['salary']['from']
            else:
                salary = 'Не указана'

            json_data[i+1] = {'name': name, 'city': city, 'url': url, 'salary': salary}
        return json_data


class SJVacancy:
    def __init__(self, data):
        self.data = data['SJ']

    def get_data(self):
        """
        Создаёт словарь, записывает в него необходимые данные
        (название вакансии, город, ссылка и зарплата)
        :return: словарь с данными
        """
        json_data = {}
        for i in range(len(self.data)):
            name = self.data[i]['profession']
            city = self.data[i]['town']['title']
            url = self.data[i]['link']
            salary = self.data[i]['payment_from']
            json_data[i+1] = {'name': name, 'city': city, 'url': url, 'salary': salary}
        return json_data
