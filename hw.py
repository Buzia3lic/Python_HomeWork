print('II  |  I')
print('=========')
print('III | IV')
quat = int(input('Введите номер четверти: '))
if quat < 1 or quat > 4: print('Такой четверти нет!')
elif quat == 1: print('X > 0, Y > 0')
elif quat == 2: print('X < 0, Y > 0')
elif quat == 3: print('X < 0, Y < 0')
elif quat == 4: print('X > 0, Y < 0')


