from get_value import get_last_name, get_first_name, get_phone_number, get_description, get_sep
from get_value import get_search

lines = None
string = None


def give_output():
    last_name = get_last_name('Введите фамилию: ')
    first_name = get_first_name('Введите имя: ')
    phone_number = get_phone_number('Введите номер телефона: ')
    description = get_description('Введите описание: ')
    sep = get_sep('Введите сепаратор: ')
    with open('DZ_7\\output.csv', 'a', encoding='utf-8') as output:
        output.write(
            f'{last_name}{sep}{first_name}{sep}{phone_number}{sep}{description}\n')


def search(value, line):
    global string
    if value in line:
        string = line
        print(string)


def get_input():
    global lines
    with open('DZ_7\output.csv', encoding='utf-8') as input:
        lines = input.read().split('\n')
        value = get_search('Введите слово для поиска: ')
        for line in lines:
            search(value, line)


def dell():
    get_input()
    lines.remove(string)
    with open('DZ_7\\output.csv', 'w', encoding='utf-8') as output:
        output.write('\n'.join(lines))
