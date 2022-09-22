# 1. Вычислить число c заданной точностью *d*
""" def calculation_number_pi(d):
    pi = 0
    i = 0
    while i < d:
        pi += (1 / 16**i) * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) -
                             (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
        i += 1
    print(float(str(pi)[:2 + d]))


d = input(
    'Задайте точность "d" числа Пи, к примеру при d = 0.001, Пи = 3.141 _:').split('.')[1]
calculation_number_pi(len(d)) """

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
""" def list_simple_factors(n):
    new_list = []
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            new_list.append(i)
        else:
            i += 1
    print(new_list)


list_simple_factors(int(input('Введите натуральное число: '))) """

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
""" def unimaginable_elements():
    list1 = [1, 1, 2, 3, 4, 5, 5, 3]
    list2 = []
    for i in list1:
        count = 0
        for j in list1:
            if j == i:
                count += 1
        if count == 1:
            list2.append(i)
    print(list2)


unimaginable_elements() """

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
""" from random import randint as r
def formation_polynomial(k):
    polycan = ''
    while k > 0:
        rand = r(0, 100)
        sign = '+' if r(0, 1) else '-'
        k = str(k)
        if len(k) == 2:
            if rand != 0 and k != 1 and rand != 1:
                polycan += f'{rand}X{seeps_dictionary[k[0]]}{seeps_dictionary[k[1]]} {sign} '
            elif rand != 0 and k != 1 and rand == 1:
                polycan += f'X{seeps_dictionary[k[0]]}{seeps_dictionary[k[1]]} {sign} '
            elif k == 1 and rand != 0 and rand != 1:
                polycan += f'{rand}X {sign} '
            elif k == 1 and rand != 0 and rand == 1:
                polycan += f'X {sign} '
            else:
                k = int(k)
                k -= 2
                continue
        else:
            if rand != 0 and k != 1 and rand != 1:
                polycan += f'{rand}X{seeps_dictionary[k[0]]} {sign} '
            elif rand != 0 and k != 1 and rand == 1:
                polycan += f'X{seeps_dictionary[k[0]]} {sign} '
            elif k == 1 and rand != 0 and rand != 1:
                polycan += f'{rand}X {sign} '
            elif k == 1 and rand != 0 and rand == 1:
                polycan += f'X {sign} '
            else:
                k = int(k)
                k -= 2
                continue
        k = int(k)
        k -= 1
    else:
        rand = r(0, 100)
        if rand == 0:
            polycan = polycan[:-2]
            polycan += f'= 0'
        else:
            polycan += f'{rand} = 0'

    return polycan


seeps_dictionary = {'0': '⁰', '1': '¹', '2': '²', '3': '³',
                    '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}

with open('formation_polynomial.txt', 'w', encoding='utf-8') as f:
    f.write(formation_polynomial(int(input('Введите натуральную степень k: ')))) """

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
""" from re import findall, split, match, search, sub
with open('polynomial_1.txt', 'r') as f:
    str1 = f.readline()
with open('polynomial_2.txt', 'r') as f:
    str2 = f.readline()
print(str1)
print(str2)


def amount_polynomials(str1, str2):
    new_list = []
    s1 = str1.split('=')
    s2 = str2.split('=')
    s1_1 = ''.join(findall(r'\S', s1[0]))
    s1_2 = ''.join(findall(r'\S', s1[1]))
    s2_1 = ''.join(findall(r'\S', s2[0]))
    s2_2 = ''.join(findall(r'\S', s2[1]))
    signs1 = findall(r'[+-]', s1_1)
    signs2 = findall(r'[+-]', s2_1)
    s1_1 = split(r'[+-]', s1_1)
    s2_1 = split(r'[+-]', s2_1)
    print(signs1)
    print(signs2)
    result = None
    for i in range(len(s1_1)):
        for j in range(len(s2_1)):
            try:
                if search(r'\*\*(\d+)', s1_1[i]).group(1) == search(r'\*\*(\d+)', s2_1[j]).group(1):
                    result = int(search(
                        r'(\d+)\*', s1_1[i]).group(1)) + int(search(r'(\d+)\*', s2_1[j]).group(1))
                    new_list.append(sub(r'(\d+)\*', str(result), s1_1[i]))
                else:
                    if int(search(r'\*\*(\d+)', s1_1[i]).group(1)) > int(search(r'\*\*(\d+)', s2_1[j]).group(1)):
                        if s1_1[i] not in new_list:
                            new_list.append(s1_1[i])
                    else:
                        if s2_1[j] not in new_list:
                            new_list.append(s2_1[j])
            except AttributeError:
                j += 1
            except IndexError:
                j += 1
    for i in range(len(s1_1)):
        for j in range(len(s2_1)):
            try:
                if search(r'\b^\d+$\b', s1_1[i]) and search(r'\b^\d+$\b', s2_1[j]):
                    result = int(search(
                        r'\b^\d+$\b', s1_1[i]).group(0)) + int(search(r'\b^\d+$\b', s2_1[j]).group(0))
                    new_list.append(str(result))
                if search(r'\w+\Sx$\b', s1_1[i]) and search(r'\w+\Sx$\b', s2_1[j]):
                    result = int(search(
                        r'(\d+)\*', s1_1[i]).group(1)) + int(search(r'(\d+)\*', s2_1[j]).group(1))
                    new_list.append(sub(r'(\d+)\*', str(result), s1_1[i]))
            except AttributeError:
                j += 1
    print(new_list)


amount_polynomials(str1, str2) """
