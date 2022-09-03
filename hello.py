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
