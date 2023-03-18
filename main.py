from classes import HH, Superjob
from pprint import pprint


def hh_request():
    h = HH(input('Введите поисковой запрос: '))
    name = h.get_request()['items'][1]['name']
    url = h.get_request()['items'][1]['alternate_url']
    responsibility = h.get_request()['items'][1]['snippet']['responsibility']
    salary = [h.get_request()['items'][1]['salary']['from'], h.get_request()['items'][1]['salary']['to']]
    data = {f"Вакансия": name, "Ссылка": url, "Описание": responsibility, "Зарплата": {'от': salary[0], 'до': salary[1]}}
    return data
    # print(h.get_request()['items'][1]['name'])
    # print(h.get_request()['items'][1]['alternate_url'])
    # print(h.get_request()['items'][1]['snippet']['responsibility'])
    # print(h.get_request()['items'][1]['salary']['from'])
    # print(h.get_request()['items'][1]['salary']['to'])


# s = Superjob(input('Введите поисковой запрос: '))
# pprint(s.get_request()['objects'][0])
# print(s.get_request()['objects'][0]['profession'])
# print(s.get_request()['objects'][0]['link'])
# print(s.get_request()['objects'][0]['candidat'])
# print(s.get_request()['objects'][0]['payment_from'])
# print(s.get_request()['objects'][0]['payment_to'])

# pprint(hh_request())