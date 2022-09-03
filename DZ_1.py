import math
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
""" def day_of_the_week(n):
    if n == 6 or n == 7:
        print('Да')
    elif n >= 1 and n <= 5:
        print('Нет')
    else:
        print('Введено неверное число')


day_of_the_week(int(input('Введите число обозначающее день недели: '))) """

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
""" def the_truth_of_the_statement(X, Y, Z):
    if not (X == 1 or X == 0) and not (Y == 1 or Y == 0) and not (Z == 1 or Z == 0):
        return 'Введены неверные предикаты'
    if not (X or Y or Z) == (not X) and (not Y) and (not Z):
        return f'Истина X = {X}, Y = {Y}, Z = {Z}'
    else:
        return f'Ложь X = {X}, Y = {Y}, Z = {Z}'


x = int(input('Введите число либо 0 либо 1: '))
y = int(input('Введите число либо 0 либо 1: '))
z = int(input('Введите число либо 0 либо 1: '))

print(the_truth_of_the_statement(x, y, z)) """

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
""" def number_of_a_quarter(x, y):
    if x > 0 and y > 0:
        return '1 четверть'
    elif x < 0 and y > 0:
        return '2 четверть'
    elif x < 0 and y < 0:
        return '3 четверть'
    elif x > 0 and y < 0:
        return '4 четверть'
    else:
        return 'x или y = 0'


x = float(input('Введите число x не равное 0: '))
y = float(input('Введите число y не равное 0: '))
print(number_of_a_quarter(x, y)) """

# 4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
""" def the_coordinate_range(n):
    if n == 1:
        return 'x > 0 и y > 0'
    elif n == 2:
        return 'x < 0 и y > 0'
    elif n == 3:
        return 'x < 0 и y < 0'
    elif n == 4:
        return 'x > 0 и y < 0'
    else:
        return 'Не верный номер четверти'


n = int(input('Введите номер четверти от 1 до 4: '))
print(the_coordinate_range(n)) """

# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
""" def point_a():
    A = list()
    for i in range(2):
        A.append(int(input(f'Введите {i + 1} координату точки A: ')))
    return A


def point_b():
    B = list()
    for i in range(2):
        B.append(int(input(f'Введите {i + 1} координату точки B: ')))
    return B


def the_distance_between_the_points(point_a, point_b):
    max_x = point_a[0]
    min_x = point_b[0]
    max_y = point_a[1]
    min_y = point_b[1]
    if point_a[0] < point_b[0]:
        max_x = point_b[0]
        min_x = point_a[0]
    if point_a[1] < point_b[1]:
        max_y = point_b[1]
        min_y = point_a[1]
    new_x = max_x - min_x
    new_y = max_y - min_y
    return round((math.sqrt(new_x ** 2 + new_y ** 2)), 2)


print(the_distance_between_the_points(point_a(), point_b())) """
