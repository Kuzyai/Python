def get_last_name(value):
    return input(value)


def get_first_name(value):
    return input(value)


def get_phone_number(value):
    return input(value)


def get_description(value):
    return input(value)


def get_search(value):
    return input(value)


def encoding():
    while True:
        name = input('Выберете формат json или csv: ')
        if name == 'json':
            return name
        elif name == 'csv':
            return name
        else:
            print('Неверный формат!')


def choice():
    return input('''Выберите цифру:
	1. Внести контакт
	2. Найти контакт
	3. Удалить контакт
	4. Вывести все контакты
	0. Завершить работу программы
	Ввод: ''')
