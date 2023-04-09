from pprint import pprint
from utils import main, Sort, PrintVacancy

user_input = input('Выберете с какого сайта хотите получить вакансии\n'
                   '1 - hh.ru\n'
                   '2 - superjob.ru\n'
                   'Если хотите запросить с обоих сайтов, то просто нажмите Enter\n'
                   'Для выхода из программы введите "exit": ')
if user_input.lower() == 'exit':
    exit()
else:
    main(user_input)

user_input_sort = input('Хотите отсортировать и вывести топ вакансий по зарплате? (y/n): ')
if user_input_sort.lower() == 'n':
    print('Работа с программой завершена. Всего доброго!')
    exit()
elif user_input_sort.lower() == 'y':
    quantity_vacansies = input('Какое количество топ вакансий вывести? ')
    s = Sort(quantity_vacansies)
    if user_input == '1':
        pprint(s.top_hh())
    elif user_input == '2':
        pprint(s.top_sj())
    else:
        pprint(s.top_hh())
        pprint(s.top_sj())


# PrintVacancy()
