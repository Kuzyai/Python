from get_value import get_last_name, get_first_name, get_phone_number, get_description, get_search
from logger import introduction_logger, search_logger, dellete_logger, view_logger
from json import dump, loads
import re
lines = None
index = None


def give_output(code):
    last_name = get_last_name('Введите фамилию: ')
    first_name = get_first_name('Введите имя: ')
    phone_number = get_phone_number('Введите номер телефона: ')
    description = get_description('Введите описание: ')
    contact = {'last_name': last_name, 'first_name': first_name,
               'phone_number': phone_number, 'description': description}
    if code == 'csv':
        with open('DZ_7\\output.csv', 'a', encoding='utf-8') as output:
            output.write(
                f'{last_name};{first_name};{phone_number};{description}\n')
            introduction_logger(
                (last_name, first_name, phone_number, description))
    elif code == 'json':
        with open('DZ_7\\output.json', 'a', encoding='utf-8') as output:
            dump(contact, output, ensure_ascii=False, indent=4)
            output.write('\n')
            introduction_logger(
                (last_name, first_name, phone_number, description))


def give_input(code):
    if code == 'csv':
        with open('DZ_7\\output.csv', encoding='utf-8') as input:
            lines = input.read().split('\n')
            [print(line) for line in lines]
            view_logger(lines)
    elif code == 'json':
        with open('DZ_7\\output.json', encoding='utf-8') as input:
            sub = re.sub(r'\s+', ' ', re.sub(r'\n', '', re.sub(
                r'\n\t', '', re.sub(r'}\n{', '}|{', input.read()))))
            lines = sub.split('|')
            view_logger(lines)
            for line in lines:
                line = loads(line)
                [print(f'{key}: {value}') for key, value in line.items()]
                print()


def search(code, text, id=0):
    global lines, index
    if code == 'csv':
        with open('DZ_7\output.csv', encoding='utf-8') as input:
            lines = input.read().split('\n')
            value = get_search(text)
            for i in range(len(lines)):
                if value in lines[i]:
                    index = i
                    if id == 1:
                        dellete_logger(lines[index])
                    elif id == 0:
                        search_logger(lines[index])
                    print(lines[i])
            else:
                print('Данный контакт не найден')
    elif code == 'json':
        with open('DZ_7\\output.json', encoding='utf-8') as input:
            sub = re.sub(r'\s+', ' ', re.sub(r'\n', '', re.sub(
                r'\n\t', '', re.sub(r'}\n{', '}|{', input.read()))))
            lines = sub.split('|')
            value = get_search(text)
            for i in range(len(lines)):
                if value in lines[i]:
                    index = i
                    if id == 1:
                        dellete_logger(lines[index])
                    elif id == 0:
                        search_logger(lines[index])
                    string = loads(lines[i])
                    [print(f'{key}: {value}') for key, value in string.items()]
            else:
                print('Данный контакт не найден')


def dell(code, text):
    if code == 'csv':
        search(code, text, id=1)
        try:
            del lines[index]
        except TypeError:
            print('Непозможно удалить несуществующий контакт')
        with open('DZ_7\\output.csv', 'w', encoding='utf-8') as output:
            output.write('\n'.join(lines))
    elif code == 'json':
        search(code, text, id=1)
        try:
            del lines[index]
            with open('DZ_7\\output.json', 'w', encoding='utf-8') as output:
                for line in lines:
                    line = loads(line)
                    dump(line, output, ensure_ascii=False, indent=4)
                    output.write('\n')
        except TypeError:
            print('Непозможно удалить несуществующий контакт')
