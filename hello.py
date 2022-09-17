""" def testing_numbers(num1, num2):
    if num1 ** 2 == num2 or num1 == num2 ** 2:
        return 'Является'
    else:
        return 'Не является'


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print(
    f'Даны 2 числа {num1} и {num2}, является ли одно число квадратом другого?')
print(testing_numbers(num1, num2)) """


""" def maximum_number():
    numbers = list()
    i = 1
    while True:
        try:
            numbers.append(int(input(f'Введите {i} число: ')))
            i += 1
        except ValueError:
            break

    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number


print(f'Максимальное число {maximum_number()}') """


""" def the_range_of_numbers(N):
    N = abs(N)
    n = -N
    numbers = list()
    for i in range(n, N + 1):
        numbers.append(i)
    print(f'Диапазон чисел равен = {numbers}')


N = int(input('Введите число: '))
the_range_of_numbers(N) """


""" def the_first_digit_after_decimal(n):
    try:
        print(n.replace(',', '.').split('.')[1][0])
    except IndexError:
        print('Нет')


the_first_digit_after_decimal(input('Введите дробное число: ')) """


""" def the_multiplicity_of_the_number(n):
    if ((not n % 5 and not n % 10) or not n % 15) and (n % 30):
        print('Кратно')
    else:
        print('Не кратно')


the_multiplicity_of_the_number(
    int(input('Введите число кратное 5 и 10 или 15, но не кратное 30: '))) """

# 1. Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.


""" def subsequence(N):
    i = 0
    result = 1
    while (i < N):
        print(result, end=" ")
        result *= -3
        i += 1


subsequence(int(input('Введите число: '))) """

# 2. Для натурального n создать последовательности 3n + 1.


""" def the_sequence_of_numbers(n):
    i = 1
    while i <= n:
        result = 3 * i + 1
        print(f'{i}: {result}')
        i += 1


the_sequence_of_numbers(int(input('Введите число: '))) """

# 3. Напишите программу, в которой пользователь будет задавать две
# строки, а программа - определять количество вхождений одной строки в другой.


""" def entering_the_lines(str1, str2):
    if len(str2) > len(str1):
        print(str2.count(str1))
    else:
        print(str1.count(str2))


entering_the_lines(input('Введите первую строку: '),
                   input('Введите вторую строку: ')) """


""" def entering_the_lines(str1, str2):
    count = 0
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    for i in range(len(str2)):
        if str1 == str2[i:i + len(str1)]:
            count += 1
    print(f'{count} раз')


entering_the_lines(input('Введите первую строку: '),
                   input('Введите вторую строку: ')) """


""" def entering_the_lines(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    n = 1
    for i in range(0, len(str1)):
        for j in range(0, len(str2), n):
            if str1[0:i + 1] == str2[j:i + j + 1]:
                continue
            else:
                n += 1
                break
        else:
            return str1[0:i + 1]
    else:
        return '""'


divider = entering_the_lines(
    input('Введите первую строку: '), input('Введите вторую строку: '))
print(
    f'Наименьший общий делитель => {divider}') """


#  Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']

""" def existence_number(list, num):
    for i in list:
        for j in range(0, len(i)):
            if i[j: j + len(num)] == num:
                print(f'Число {num} содержится в строке {i}')


existence_number(['65h34q', 'sdg634d', '147jnbv'], input('Введите число: ')) """


# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
""" def position_second_entry(list, frase):
    count = 0
    for i in range(len(list)):
        if list[i] == frase:
            count += 1
        if count == 2:
            return i
    else:
        return -1


print(position_second_entry(
    ["йцу", "фыв", "йцу", "ячс", "цук", "йцукен", "йцу"], 'йцу')) """

# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.


""" from time import time
def random_number():
    now = str(time()).replace('.', '')
    count = 2
    dia = 10 ** int(now[-2])
    while dia // 10:
        dia //= 10
        count += 1
    print(now[-1:-count:-1])


random_number() """


""" from functools import wraps
def funk(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print("start")
        f(*args, **kwargs)
        print("end")
    return inner


@funk
def say(name, surname, age):
    print('Hello', name, surname, age)


say('V', 'sdf', 'asfasa')
print(say.__name__) """
