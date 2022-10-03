count = 1
for i in range (0, 2):
    for j in range (0, 2):
        for k in range (0, 2):
            print(f'Комбинация {count}:')
            count += 1
            print (i, j, k) 
            cond1 = not (i or j or k)
            cond2 = (not i) or (not j) or (not k)
            print ('Результат для [not (i or j or k)]: ', cond1)
            print ('Результат для [(not i) or (not j) or (not k)]: ',cond2)
            print ('Сравнение этих двух утверждений: ', cond1 == cond2)
            print ()
            

