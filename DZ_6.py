# 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
""" def subtract_elements(k):
    y = 0
    new_list = [round((1 + 1 / i) ** i, 2) for i in range(1, k + 1)]
    [y := y + i for i in new_list]
    print(
        f'Список элементов последовательности {new_list}, cумма элементов списка {round(y, 2)}')


subtract_elements(int(input('Введите число: '))) """

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
""" def work_elements(N, index):
    work = 1
    new_list = [i for i in range(-N, N, 2)]
    [work := work * new_list[int(i) - 1] for i in index.split()]
    print(
        new_list, f'Произведение элементов на позициях {index} => {work}', sep='\n')


work_elements(int(input('Введите число: ')), input(
    'Введите позиции элементов массива: ')) """

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
""" def summer_elements():
    my_list = [2, 3, 5, 9, 3]
    sum_i = 0
    [sum_i := sum_i + my_list[i] for i in range(1, len(my_list), 2)]
    return sum_i


print(summer_elements()) """


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
""" def difference_fractional_part():
    list1 = [1.1, 1.2, 3.1, 10.01]
    # list2 = []
    list2 = list(map(float, ['0.' + str(i).split('.')[1] for i in list1]))
    max_i, min_i = 0, 1
    [max_i := list2[i] for i in range(len(list2)) if list2[i] > list2[0]]
    [min_i := list2[i] for i in range(len(list2)) if list2[i] < list2[0]]
    return round(max_i - min_i, 4)


print(difference_fractional_part()) """


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
""" def unimaginable_elements():
    list1 = [1, 1, 2, 3, 4, 5, 5, 3]
    list2 = list(filter(lambda x: list1.count(x) == 1, list1))
    print(list2)


unimaginable_elements() """
