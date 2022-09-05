# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
""" def the_sum_numbers(n):
    number = n.replace(',', '.').split('.')
    sum = 0
    for i in number:
        for j in i:
            sum += int(j)
    print(sum)


the_sum_numbers(input('Введите вещественное число: ')) """

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


""" def factorial(N):
    x = None
    match N:
        case 0 | 1:
            result.append(N)
            tup.append(f'{N}')
            return 1
        case _:
            string = '1'
            x = N * factorial(N - 1)
            for i in range(N - 1):
                string += f' * {i + 2}'
            result.append(x)
            tup.append(string)
            return x


n = int(input('Введите число: '))
result = list()
tup = list()
f = factorial(n)
tup = tuple(tup)
print(f'Факториал числа {n} равен {f} => {result} {tup}') """

# 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.


""" def subtract_elements(k):
    new_list = list()
    y = 0
    for i in range(1, k + 1):
        x = round((1 + 1 / i) ** i, 2)
        new_list.append(x)
        y += x
    print(
        f'Список элементов последовательности {new_list}, cумма элементов списка {round(y, 2)}')


subtract_elements(int(input('Введите число: '))) """

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.


""" def work_elements(N, index):
    new_list = list()
    work = 1
    for i in range(-N, N, 2):
        new_list.append(i)
    index = index.split()
    for i in index:
        work *= new_list[int(i) - 1]
    print(new_list)
    print(f'Произведение элементов на позициях {index} => {work}')


work_elements(int(input('Введите число: ')), input(
    'Введите позиции элементов массива: ')) """

# 5. Реализуйте алгоритм перемешивания списка.

""" from random import randint
def mixing_list(list):
    print(list)
    for i in range(len(list)):
        k = randint(0, len(list))
        list[i], list[k] = list[k], list[i]
    print(list)


mixing_list(input('Введите числа через пробел: ').split()) """
