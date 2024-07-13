# Функция count_calls - подсчитывающая вызовы остальных функций.

calls = 0

def count_calls():
    global calls
    calls += 1

# Функция string_info - принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.

def string_info():
    count_calls()
    string_user = input('Введите строку для создания кортежа: ')
    string_user_list = []
    string_user_list.append(len(string_user))
    string_user_list.append(string_user.upper())
    string_user_list.append(string_user.lower())
    string_user_tuple = tuple(string_user_list)
    print(string_user_tuple)

# Функция is_contains принимает два аргумента: строку и список,
# возвращает True, если строка находится в этом списке,
# возвращает False - если отсутствует. Регистром строки при проверке пренебречь.

def is_contains():
    count_calls()
    flag = False
    string_user = input('Введите строку для поиска в списке: ')
    string_list = ['Апельсин', 'Яблоко', 'Гранат',
                   'Банан', 'Ананас', 'Вишня']
    for i in string_list:
        if i.lower() == string_user.lower():
            flag = True
            break
    if flag:
        print(f'Строка "{string_user}" присутствует в списке')
    else:
        print(f'Строки "{string_user}" нет в списке')

string_info()
is_contains()

print('Количество вызовов функций в программе: ', calls)
