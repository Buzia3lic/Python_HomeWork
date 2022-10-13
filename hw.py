
import random
import math

def NewList(num):
    
    newlist = []
    for el in range(num):
        newlist.append(random.randrange(10))
    return newlist

task = int(input('Введите номер задачи: '))
print('#################################################################################')

#Задача 1
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

if task == 1:
    print('Программа вычисляет число c заданной точностью d')
    print('#################################################################################')
    d = float(input('Задайте точность $d (например 0.001): '))
    count = 0
    while d != 1:
        d *= 10
        count += 1
    p = round(math.pi, count)

    print(p)


#######################################################

#Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример:
# N = 20 => [2, 2, 5]

elif task == 2:
    print('Программа составляет список простых множителей числа N.')
    print('#################################################################################')
    num = int(input('Напишите число: '))
    res = []
    d = 2
    while d**2 <= num:
        if num % d == 0:
            res.append(d)
            num = num // d
        else:
            d += 1
    res.append(num)

    print(res)


# ########################################################3

# Задача 3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

elif task == 3:
    print('Программа выводит список неповторяющихся элементов исходной последовательности.')
    print('#################################################################################')
    num = int(input('Введите число элементов: '))
    newList = NewList(num)
    voc = {}
    print(newList)
    for el in newList:
        voc[el] = voc.get(el, 0) + 1
    newList.clear()
    for key, val in voc.items():
        if val == 1: 
            newList.append(key)
    print(newList)

# ########################################################3

#Задача 4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена.
# Записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

elif task == 4:
    print('Программа записывает в файл многочлен степени k.')
    print('#################################################################################')
    k = int(input('Введите степень для многочелена: '))
    numbers = NewList(k + 1)
    print('Список коэффициентов: ', numbers)
    equ = []
    for el in numbers:
        if k == 0:
            if el != 0:
                equ.append(str(el))
                continue
        if el == 0:
            k -= 1  
            continue
        else:
            equ.append('x' + str(k) + '*' + str(el))
            k -= 1
            continue
        
     
    print('Это уравнение запишем в файл: ')
    print(*equ, sep=' + ')

    with open('file_out.txt', 'w') as f:
        print(*equ, sep=' + ', file = f)
    

########################################################3

#Задача 5
#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Пример:
# файл1: 2x^2 + 7x + 5
# файл2: 4x^2 + 3x + 9
# результат: 6x^2 + 10x + 14

elif task == 5:
    print('Программа создает файл, содержащий сумму многочленов.')
    print('#################################################################################')
    with open('file_input_1.txt', 'r') as f1:
        data1 = f1.readline()
    print(data1)
    list1 = data1.split('+')
    for k in range(len(list1)):
        num = ''
        for i in list1[k]:
            j = 0
            if i[j] == 'x':
                break
            if i[j].isdigit():
                num += i[j]
                j += 1
        list1[k] = num
        k += 1
    list1 = list1[:: -1]
    


    with open('file_input_2.txt', 'r') as f2:
        data2 = f2.readline()
    print(data2)
    list2 = data2.split('+')   
    for k in range(len(list2)):
        num = ''
        for i in list2[k]:
            j = 0
            if i[j] == 'x':
                break
            if i[j].isdigit():
                num += i[j]
                j += 1
        list2[k] = num
        k += 1
    list2 = list2[:: -1]
    

    listres = []

    for i in range(len(list1)):
        listres.append(int(list1[i]) + int(list2[i]))
    for i in range(int(len(list1)), int(len(list2))):
        listres.append(int(list2[i]))
    listres = listres[:: -1]
    
    k = len(listres) - 1
    equ = []
    for el in listres:
        if k == 0:
            if el != 0:
                equ.append(str(el))
                continue
        if el == 0:
            k -= 1  
            continue
        else:
            equ.append('x' + str(k) + '*' + str(el))
            k -= 1
            continue
        
     
    print('Это уравнение запишем в файл: ')
    print(*equ, sep=' + ')

    with open('file_out.txt', 'w') as f:
        print(*equ, sep=' + ', file = f)
########################3

else:
    print('Такой задачи нет!')

