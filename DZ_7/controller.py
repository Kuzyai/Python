from get_value import get_last_name, get_first_name, get_phone_number, get_description, get_sep

last_name = get_last_name('Введите фамилию: ')
first_name = get_first_name('Введите имя: ')
phone_number = get_phone_number('Введите номер телефона: ')
description = get_description('Введите описание: ')
sep = get_sep('Введите сепаратор: ')


def give_output(last_name, first_name, phone_number, description, sep):
    with open('DZ_7\\output.csv', 'a', encoding='utf-8') as output:
        output.write(
            f'{last_name}{sep}{first_name}{sep}{phone_number}{sep}{description}\n')
