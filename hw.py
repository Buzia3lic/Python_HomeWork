
from inspect import isdatadescriptor
from operator import truediv
import random
import math
from tkinter import N
import collections
from turtle import clear


task = int(input('Введите номер задачи: '))
print('#################################################################################')

#Задача 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

if task == 1:
    print('Программа удаляет из текста все слова, содержащие "абв".')
    print('#################################################################################')
    
    data = [i for i in input('Введите слова через пробел: ').split()]
    res = list(filter(lambda x: not 'абв' in x , data))
    print('Результат без "абв": ', *res)

#######################################################

#Задача 2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

elif task == 2:
    print('Программа для игры с конфетами человек против человека.')
    print('#################################################################################')
    print('На столе 2021 конфета. Брать можно от 1 до 28 конфет. Побеждает тот, кто заберает последние конфеты!')
    table = 202
    checkBot = input('Играем с Ботом или без? Да/Нет: ')
    if checkBot.lower() == 'нет':
        turn1 = random.randrange(1, 3)
        if turn1 == 1:
            turn2 = 2
        else:
            turn2 = 1
        print(f'Начинает игрок номер "{turn1}"')
        while (table > 0):
            print(f'На столе "{table}" конфет! Сколько взять?')
            x1 = int(input(f'Конфеты берет игрок номер "{turn1}": '))
            while x1 > 28:
                x1 = int(input(f'Неправильно! Конфет не может быть больше 28!! Игрок номер "{turn1}" возьми правильное количество: '))
            while x1 > table:
                x1 = int(input(f'Неправильно! Конфет не может быть больше, чем на столе!! Игрок номер "{turn1}" возьми правильное количество: '))
            table -= x1
            if table == 0:
                print('#################################')
                print(f'## Победил игрок "{turn1}" !!!!!!!!! ##')
                print('#################################')
                continue
            print(f'На столе "{table}" конфет! Сколько взять?')
            x2 = int(input(f'Конфеты берет игрок номер "{turn2}": '))
            while x2 > 28:
                x2 = int(input(f'Неправильно! Конфет не может быть больше 28!! Игрок номер "{turn2}" возьми правильное количество: '))
            while x2 > table:
                x2 = int(input(f'Неправильно! Конфет не может быть больше, чем на столе!! Игрок номер "{turn2}" возьми правильное количество: '))
            table -= x2
            if table == 0:
                print('#################################')
                print(f'## Победил игрок "{turn2}" !!!!!!!!! ##')
                print('#################################')
                continue
    elif checkBot.lower() == 'да':
        print('Играем с Ботом!')
        turn1 = random.randrange(1, 3)
        if turn1 == 1:
            turn2 = 2
            print(f'Начинает игрок номер "{turn1}"')
        else:
            turn2 = 1
            print(f'Начинает "Бот"')
            x2 = random.randrange(1, 29)
            print(f'Бот берет конфеты: {x2}')
            table -= x2
        while (table > 0):
            print(f'На столе "{table}" конфет! Сколько взять?')
            x1 = int(input(f'Конфеты берет игрок номер "{turn1}": '))
            while x1 > 28:
                x1 = int(input(f'Неправильно! Конфет не может быть больше 28!! Игрок номер "{turn1}" возьми правильное количество: '))
            while x1 > table:
                x1 = int(input(f'Неправильно! Конфет не может быть больше, чем на столе!! Игрок номер "{turn1}" возьми правильное количество: '))
            table -= x1
            if table == 0:
                print('#################################')
                print(f'## Победил игрок "{turn1}" !!!!!!!!! ##')
                print('#################################')
                continue
            print(f'На столе "{table}" конфет! Сколько взять?')
            if table <= 28:
                x2 = table
            else:
                x2 = random.randrange(1, 29)
            print(f'Бот берет конфеты: {x2}')
            table -= x2
            if table == 0:
                print('#############################')
                print(f'## Победил "Бот" !!!!!!!!! ##')
                print('#############################')
                continue

# ########################################################3

# Задача 3
# Создайте программу для игры в ""Крестики-нолики"".

elif task == 3:
    print('Программа для игры в "Крестики-нолики".')
    print('#################################################################################')
    print('Поле для игры:')
    
    win1 = [1, 2, 3]
    win2 = [4, 5, 6]
    win3 = [7, 8, 9]
    win4 = [1, 4, 7]
    win5 = [2, 5, 8]
    win6 = [3, 6, 9]
    win7 = [1, 5, 9]
    win8 = [3, 5, 7]
    
    battlefiled = ' 1 2 3 \n 4 5 6 \n 7 8 9 '
    print(battlefiled)
    checker = True
    turn = 1
    listX = []
    listO = []
    while checker == True:
        if turn == 1:
            checker = False
            bf = list(battlefiled)

            x1 = input(f'Игрок 1 введите номер для X: ')

            listX.append(int(x1))
            
            for i in range(len(bf)):
                if bf[i] == x1:
                    bf[i] = 'X'
            
            for i in bf:
                if i.isdigit():
                    checker = True
            
            battlefiled = "".join(bf)
            print(battlefiled)

            if collections.Counter(listX) == collections.Counter(win1) or collections.Counter(listX) == collections.Counter(win2) or collections.Counter(listX) == collections.Counter(win3)or collections.Counter(listX) == collections.Counter(win4) or collections.Counter(listX) == collections.Counter(win5) or collections.Counter(listX) == collections.Counter(win6) or collections.Counter(listX) == collections.Counter(win7) or collections.Counter(listX) == collections.Counter(win8):
                print(f'Победитель Игрок номер "{turn}" !!')
                checker = False
                continue


            turn = 2
            
            continue

        if turn == 2:
            checker = False
            bf = list(battlefiled)

            x2 = input(f'Игрок 2 введите номер для O: ')

            listO.append(int(x2))
            
            for i in range(len(bf)):
                if bf[i] == x2:
                    bf[i] = 'O'
            
            for i in bf:
                if i.isdigit():
                    checker = True
            
            battlefiled = "".join(bf)
            print(battlefiled)

            if collections.Counter(listO) == collections.Counter(win1) or collections.Counter(listO) == collections.Counter(win2) or collections.Counter(listO) == collections.Counter(win3)or collections.Counter(listO) == collections.Counter(win4) or collections.Counter(listO) == collections.Counter(win5) or collections.Counter(listO) == collections.Counter(win6) or collections.Counter(listO) == collections.Counter(win7) or collections.Counter(listO) == collections.Counter(win8):
                print(f'Победитель Игрок номер "{turn}" !!')
                checker = False
                continue

            turn = 1    
    

# ########################################################3

#Задача 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

elif task == 4:
    print('RLE алгоритм: модуль сжатия и восстановления данных')
    print('#################################################################################')
    data = input('Введите текст: ')
    res = []
    counter = 1
    sbl = ''
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            counter += 1
        else:
            res.append((counter, data[i - 1]))
            counter = 1
    res.append((counter, data[i]))
    
    for i in res:
        for j in i:
            sbl += str(j)
    print('После сжатия: ', sbl)

    sbl = ''

    for i in res:
        sbl += i[0] * i[1]
            
    print('После восстановления: ', sbl)


    
    

########################################################3

else:
    print('Такой задачи нет!')

