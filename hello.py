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

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


""" def min_max_number(value):
    list_num = value.split(' ')
    min_i, max_i = 0, 0
    for i in range(1, len(list_num)):
        if int(list_num[i]) > int(list_num[max_i]):
            max_i = i
        if int(list_num[i]) < int(list_num[min_i]):
            min_i = i
    return f'Большее число {list_num[max_i]}, меньшее число {list_num[min_i]}'


print(min_max_number(input('Введите числа через пробел: '))) """

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python


""" from re import findall, split, match
from math import sqrt
def root_square_equation(equation):
    s = equation.split('=')
    s1 = ''.join(findall(r'\S', str(s[0])))
    s2 = ''.join(findall(r'\S', str(s[1])))
    h = findall(r'[+-]', s1)
    m1 = match(r'[+-]', s1)
    s2 = int(s2)
    if m1:
        s1 = split(r'[+-]', s1[1:])
    else:
        s1 = split(r'[+-]', s1[:])
    A, B, c = s1
    a = int(match(r'\d*', A)[0])
    b = int(match(r'\d*', B)[0])
    c = int(c)
    if m1:
        if m1[0] == '-':
            a = -a
        else:
            a = a
    if h[-2] == '-':
        b = -b
    if h[-1] == '-':
        c = -c
    if s2 != 0:
        c -= s2
    if not a:
        print('Так как "A = 0" решаем его как линейное: ')
        return (-c) / b
    D = b ** 2 - 4 * a * c
    if D < 0:
        print(D)
        return 'Корней нет'
    if D == 0:
        print(D)
        return (-b) / (2 * a)
    print(D)
    return round((-b + sqrt(D)) / (2 * a), 2), round((-b - sqrt(D)) / (2 * a), 2)


print(root_square_equation(input(
    'Введите квадратное уравнение в формате "+-A * x ** 2 +- B * x +- C = number": '))) """


# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.
""" def smallest_common_multiple(num1, num2):
    max_n = num1 if num1 > num2 else num2
    for i in range(1, max_n + 1):
        for j in range(1, max_n + 1):
            if num1 * i == num2 * j:
                return f'{num2 * j}'


with open('smallest_common_multiple.txt', 'w', encoding='utf-8') as f:
    f.write(smallest_common_multiple(
        int(input('Введите первое число: ')), int(input('Введите второе число: ')))) """

""" with open('new.txt', 'r', encoding='utf-8') as f:
    print([x for x in map(lambda i: (
        i, i ** 2), filter(lambda x: not x % 2, map(int, f.readline().split(' '))))]) """

# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
""" with open('new1.txt', 'r') as f:
    new_list = list(map(int, f.readline().split()))

print([new_list[i] - 1 for i in filter(lambda i: new_list[i] -
      1 != new_list[i-1], range(1, len(new_list)))]) """

# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
""" with open('new2.txt', 'r') as f:
    new_list = list(map(int, f.readline().split()))
print(new_list)
new_list2 = [new_list[i]
             for i in range(1, len(new_list)) if new_list[i] > max(new_list[0:i])]
new_list2.insert(0, new_list[0])
print(new_list2) """

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
""" with open('new3.txt', 'r', encoding='utf-8') as f:
    print(' '.join(
        [x for x in filter(lambda x: x.find('абв') < 0, f.readline().split())])) """


""" def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


val = countdown(5)
next(val) """


""" class Robot:
    population = 0

    def __init__(self, name=None):
        self.name = name
        print(f'Инициализация {self.name}')
        Robot.population += 1

    def __del__(self):
        print(f'{self.name} уничтожается')
        Robot.population -= 1
        if not Robot.population:
            print(f'{self.name} был последним')
        else:
            print(f'Осталось {Robot.population} роботов')

    def say_hi(self):
        print('Приветствую, мои хозяева называют меня', self.name)

    @staticmethod
    def how_many():
        print(f'У нас осталось {Robot.population} роботов')


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2
Robot.how_many() """


""" from re import sub
def polimorfizm(str):
    str = sub(r'[,.!?\s]', '', str).lower()
    if str == str[::-1]:
        print("Полиморфизм")
    else:
        print("Не полиморфизм")


polimorfizm('А роза, упала на !лапу?. Азора.') """


# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции + , -, /, *. приоритет операций стандартный.
# - Добавьте возможность использования скобок, меняющих приоритет операций.
s = '((1+2)*3 + 2 *3)/ 5 '
# s = '1 + 2 * 3 + 4   / 2'
print(eval(s))
result = list(''.join(s.split()))


def parentheses():
    list_index_start = []
    list_index_end = []
    for i in range(len(result)):
        try:
            list_index_start.append(result.index('(', i))
        except ValueError:
            pass
    for i in range(len(result)):
        try:
            list_index_end.append(result.index(')', i))
        except ValueError:
            pass
    # print(list_index_start)
    # list_index_end = sorted(list(set(list_index_end)), reverse=True)
    # print(list_index_end)
    list_index = sorted(
        list(set.union(set(list_index_start), set(list_index_end))))
    return list_index


def calculation_expression(s, i=0, j=len(result)):
    def replacement():
        del result[i - 1:i + 2]
        result.insert(i - 1, n)
    while j - i > 1:
        while i < j:
            if result[i] == '*':
                n = str((float(result[i - 1]))
                        * (float(result[i + 1])))
                replacement()
            elif result[i] == '/':
                n = str((float(result[i - 1])) /
                        (float(result[i + 1])))
                replacement()
            i += 1
        i = 0
        while i < j:
            if result[i] == '+':
                n = str((float(result[i - 1])) +
                        (float(result[i + 1])))
                replacement()
                i -= 1
            elif result[i] == '-':
                n = str((float(result[i - 1])) -
                        (float(result[i + 1])))
                replacement()
                i -= 1
            i += 1
    index_list = parentheses()
    if len(index_list):
        countdown = len(index_list) // 2
        del result[index_list[countdown]]
        del result[index_list[countdown - 1]]
    s = ''.join(result)
    return s


index_list = parentheses()
countdown = len(index_list) // 2

s = calculation_expression(
    s, index_list[countdown - 1] + 1, index_list[countdown])
print(s)
s = calculation_expression(
    s, index_list[countdown - 1] + 1, index_list[countdown])
print(s)
s = calculation_expression(
    s, index_list[countdown - 1] + 1, index_list[countdown])
print(s)

# 2. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
