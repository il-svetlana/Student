first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (
    abs(len(x) - len(y))
    for x, y
    in zip(first, second)
    if len(x) != len(y))

print('first_result : ', list(first_result))

second_result = (
    abs(len(first[i]) - len(second[i]))
    for i in range(len(first))
    if len(first[i]) != len(second[i]))

print('second_result : ', list(second_result))