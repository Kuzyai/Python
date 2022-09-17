# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


""" def summer_elements():
    new_list = [2, 3, 5, 9, 3]
    sum = 0
    for i in range(1, len(new_list), 2):
        sum += new_list[i]
    return sum


print(summer_elements()) """

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.


""" def work_pairs_numbers():
    list1 = [2, 3, 4, 5, 6]
    list2 = []
    i, j = 0, len(list1) - 1
    count = len(list1) // 2
    if len(list1) % 2:
        count += 1
    while i < count:
        list2.append(list1[i] * list1[j])
        i += 1
        j -= 1
    print(list2)


work_pairs_numbers() """

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.


""" def difference_fractional_part():
    list1 = [1.1, 1.2, 3.1, 10.01]
    list2 = []
    for i in list1:
        list2.append(float('0.' + str(i).split('.')[1]))
    max_i, min_i = 0, 1
    for i in range(len(list2)):
        if list2[i] > list2[0]:
            max_i = list2[i]
        if list2[i] < list2[0]:
            min_i = list2[i]
    return round(max_i - min_i, 4)


print(difference_fractional_part()) """


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
""" def transformation_numbers(num):
    result = ''
    while num // 2 != 0:
        result += str(num % 2)
        num //= 2
    else:
        result += '1'
    return int(result[::-1])


print(transformation_numbers(int(input('Введите число: ')))) """

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


""" def fibonachi(n):
    n = abs(n)
    k = -n
    new_list = []
    fib0 = 0
    fib1 = fib2 = fib_1 = 1
    fib_2 = -1
    new_list.append(fib_1)
    new_list.append(fib_2)
    for _ in range(k, -2):
        fib_2, fib_1 = fib_1, fib_2 - fib_1
        new_list.append(-fib_1)
    new_list.reverse()
    new_list.append(fib0)
    new_list.append(fib1)
    new_list.append(fib2)
    for _ in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        new_list.append(fib2)
    print(new_list)


fibonachi(int(input('Введите число: '))) """
