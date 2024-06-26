# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0

First = input('Введите первое число: ')
Second = input('Введите второе число: ')
Third = input('Введите третье число: ')

# проверка на наличие пробелов

Control_String = First + Second + Third

if Control_String.count(' ') != 0:
    print('Введённые значения содержат пробелы. Программа завершена.')
else:

# сравнение чисел и вывод результата

    if int(First) == int(Second) == int (Third):
        print('Кол-во равных чисел: ', 3)
    elif int(First) == int(Second) or int(Second) == int(Third) or int(First) == int(Third):
        print('Кол-во равных чисел: ', 2)
    else:
        print('Кол-во равных чисел: ', 0)