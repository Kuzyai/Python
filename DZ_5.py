# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
""" text = 'Я абв люблю иабв Питон абви Джавабв'
new_text = ' '.join([i for i in text.split() if 'абв' not in i])
print(new_text) """
# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

""" from random import choice


def game_sweets(sweets, m):
    print(
        f'Первому игроку надо забрать {sweets % (m + 1)} чтобы забрать все конфеты у аппонента.')
    player_list = ['bot', input('Введите ваше имя: ')]
    gamer = choice(player_list)
    while sweets:
        if gamer == 'bot':
            print(f'Ходит игрок {gamer}')
            move = sweets % (m + 1)
        else:
            print(f'Ходит игрок {gamer}')
            while True:
                move = int(input(f'Введите количество конфет, максимум {m}: '))
                if move <= m:
                    break
        sweets -= move
        print(f'Осталось {sweets} конфет')
        if not sweets:
            print(f'Игрок {gamer} победил')
        gamer = player_list[0] if gamer == player_list[1] else player_list[1]


game_sweets(int(input('Введите общее количество конфет: ')), int(
    input('Введите максимаьное количество конфет за 1 ход: '))) """

# 3. Создайте программу для игры в ""Крестики-нолики"".
""" from collections import Counter
import numpy
n = 3
A = [['*' for _ in range(n)] for _ in range(n)]
# B = [[input(f'Введите {j + 1} элемент {i + 1} строки: ')
#       for j in range(n)] for i in range(n)]
# C = [[input(f'Введите {j + 1} элемент {i + 1} строки: ')
#       for j in range(n)] for i in range(n)]
a1 = [['X', 'X', 'X'], ['0', '0', '0'], ['0', '0', '0']]
a2 = [['0', '0', '0'], ['X', 'X', 'X'], ['0', '0', '0']]
a3 = [['0', '0', '0'], ['0', '0', '0'], ['X', 'X', 'X']]
b1 = [['X', '0', '0'], ['X', '0', '0'], ['X', '0', '0']]
b2 = [['0', 'X', '0'], ['0', 'X', '0'], ['0', 'X', '0']]
b3 = [['0', '0', 'X'], ['0', '0', 'X'], ['0', '0', 'X']]
c1 = [['X', '0', '0'], ['0', 'X', '0'], ['0', '0', 'X']]
c2 = [['0', '0', 'X'], ['0', 'X', '0'], ['X', '0', '0']]
winner_list = [a1, a2, a3, b1, b2, b3, c1, c2]
print()
print('\n'.join([' '.join(row) for row in A]))


def crosses_noliki():
    player1 = 'lu'
    player2 = 'pe'
    player = player1
    while True:
        i = int(input(r'Введите строку: '))
        j = int(input(r'Введите столбец: '))
        mean = input('Введите X или 0: ')
        A[i][j] = mean
        print('\n'.join([' '.join(row) for row in A]))
        # print(b2)
        for win in winner_list:
            if Counter(win[i]) == Counter(A[i]) or (win[i][j] == A[i][j] and win[i][j] == A[i][j] and Counter(win[2]) == Counter(A[2])):
                return f'{player} выйграл!'
        player = player1 if player == player2 else player2


print(crosses_noliki()) """
#  or Counter(win[j]) == Counter(A[j]
# Counter(numpy.array(win[j]).transpose()) == Counter(numpy.array(A[j]).transpose())


""" from tkinter import Tk, Label, Button
import random, time
def stop_game():
    global game_left
    for item in game_left:
        buttons[item].config(bg='white', state='disabled')


def win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) or (game[6] == n and game[7] == n and game[8] == n)\
            or (game[0] == n and game[3] == n and game[6] == n) or (game[1] == n and game[4] == n and game[7] == n) or (game[2] == n and game[5] == n and game[8] == n)\
            or (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True


def push(b):
    global game
    global game_left
    global turn
    game[b] = 'X'
    buttons[b].config(text='X', bg='white', state='disabled')
    game_left.remove(b)
    if b == 4 and turn == 0:
        t = random.choice(game_left)
    elif b != 4 and turn == 0:
        t = 4
    if turn > 0:
        t = 8 - b
    if t not in game_left:
        try:
            t = random.choice(game_left)
        except IndexError:
            label['text'] = 'Игра окончена!'
            stop_game()
    game[t] = '0'
    time.sleep(0.5)
    buttons[t].config(text='0', bg='white', state='disabled')
    if win('X'):
        label['text'] = 'Вы победили!'
        stop_game()
    elif win('0'):
        label['text'] = 'Вы проиграли!'
        stop_game()
    else:
        if len(game_left) > 1:
            game_left.remove(t)
        else:
            label['text'] = 'Игра окончена!'
            stop_game()
        turn += 1


game = [None] * 9
game_left = list(range(9))
turn = 0
root = Tk()
label = Label(text='Крестики-нолики',
              font=('Arial', 18, 'bold'))
buttons = [Button(width=5, height=2, font=(
    'Arial', 20, 'bold'), bg='DeepSkyBlue', command=lambda x=i: push(x)) for i in range(9)]
label.grid(row=0, column=0, columnspan=3)
row, col = 1, 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0
root.mainloop() """

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
""" from re import findall
def encode(s):
    encoding = ''
    i = 0
    while i < len(s) - 1:
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i += 1
    return encoding


def decode(s):
    int_list = findall(r'\d+', s)
    char_list = findall(r'[a-zA-Zа-яА-ЯёЁ]', s)
    return ''.join([char_list[i] * int(int_list[i]) for i in range(len(char_list))])


with open('unexplored.txt', encoding='utf-8') as f:
    s = f.readline()
with open('encoded.txt', 'w', encoding='utf-8') as f:
    f.write(encode(s))
with open('encoded.txt', encoding='utf-8') as f:
    s = f.readline()
with open('decoded.txt', 'w', encoding='utf-8') as f:
    f.write(decode(s)) """
