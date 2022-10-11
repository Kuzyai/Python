from datetime import datetime as dt


def introduction_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('DZ_7\\log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{time};Добавление контакта;{data}\n')


def search_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('DZ_7\\log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{time};Выполнен поиск контакта;{data}\n')


def dellete_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('DZ_7\\log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{time};Удаление контакта;{data}\n')


def view_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('DZ_7\\log.csv', 'a', encoding='utf-8') as file:
        file.write(f'{time};Просмотр всех контактов;{data}\n')
