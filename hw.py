import math
import random

# 1 .Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. 
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. 
# Ввод чисел продолжается до ввода пустой строки.
# Входные данные
# 36 12 144 18
# Выходные данные
# 6

# numbers = [int(i) for i in input('Введите числоа через пробел: ').split()]
# print(numbers)
# temp = math.gcd(numbers[0], numbers[1])
# for i in range(2, len(numbers)):
#     temp = math.gcd(temp, numbers[i])
# print(temp)


##################################

# 2. Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
# Буква "О" – соответствует выпадению Орла
# буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные Выходные данные
# ОРРОРОРООРРРО 3
# ООООООРРРОРОРРРРРРР 7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР 31

# coinvar = input('Введите комбинации Орлов и Решек: ')
# print(coinvar)
# di = {'О': 0, 'Р': 0}
# counter = 1

# for i in range(1, len(coinvar)):
#     if coinvar[i] == coinvar[i - 1]:
#         counter += 1
#     else:
#         for k, v in di.items():
#             if counter > v:
#                 di[coinvar[i - 1]] = counter
#         counter = 1

# for k, v in di.items():
#     if counter > v:
#         di[coinvar[i]] = counter

# print(di.get("Р"))

##########################################

# 3. print('Программа выводит список неповторяющихся элементов исходной последовательности.')

def NewList(num):
    
    newlist = []
    for el in range(num):
        newlist.append(random.randrange(10))
    return newlist

num = int(input('Введите число элементов: '))

newList = NewList(num)

voc = {}

print(newList)

for el in newList:
    voc[el] = voc.get(el, 0) + 1
newList.clear()

# for key, val in voc.items():
#     if val == 1: 
#         newList.append(key)
# print(newList)

print(list(filter(