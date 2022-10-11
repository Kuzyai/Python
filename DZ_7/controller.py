from get_value import choice, encoding
from functions import give_output, search, dell, give_input


def launch():
    while True:
        name = choice()
        match name:
            case '1':
                give_output(encoding())
            case '2':
                search(encoding(), 'Введите контакт для поиска: ')
            case '3':
                dell(encoding(), 'Введите контакт для удаления: ')
            case '4':
                give_input(encoding())
            case '0':
                break
            case _:
                print('Вы ввели неверную команду, повторите ввод!')
