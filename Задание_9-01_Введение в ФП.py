def get_correct_list(new_list):

    def correct_list(new_list):
        if len(new_list) == 0:
            raise ValueError

        for i in new_list:
            if isinstance(i, int) or isinstance(i, float):
                continue
            else:
                print('!!! Некорректный элемент: ', i)
                raise TypeError

    try:
        correct_list(new_list)
        return True
    except TypeError:
        print(f'Ошибка. Типы данных в списке {new_list} некорректны.')
        return False
    except ValueError:
        print(f'Ошибка. Передан пустой список {new_list}.')
        return False
def min_elem(new_list):
    if get_correct_list(new_list):
        print(f'Минимальный элемент списка {new_list}: ', min(new_list))
        return min(new_list)
    else:
        print('С ошибками не работаем.')
        return None
def max_elem(new_list):
    if get_correct_list(new_list):
        print(f'Максимальный элемент списка {new_list}: ', max(new_list))
        return max(new_list)
    else:
        print('С ошибками не работаем.')
        return None
def sum_elem(new_list):
    if get_correct_list(new_list):
        print(f'Сумма элементов списка {new_list}: ', sum(new_list))
        return sum(new_list)
    else:
        print('С ошибками не работаем.')
        return None
def len_list(new_list):
    if get_correct_list(new_list):
        print(f'Длина списка {new_list}: ', len(new_list))
        return len(new_list)
    else:
        print('С ошибками не работаем.')
        return None
def sorted_list(new_list):
    if get_correct_list(new_list):
        print(f'Сортировка списка {new_list}:\n', sorted(new_list))
        return sorted(new_list)
    else:
        print('С ошибками не работаем.')
        return None
def apply_all_func(new_list, *functions):
    # Эта функция должна:
    # Вызвать каждую функцию к переданному списку
    # Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
    print('')
    dict_apply = {}

    for func in functions:
        dict_apply[func.__name__] = func(new_list)

    return dict_apply

test_list0 = [10, 5, 0, 5]
test_list1 = [10.4, 5, 0, -5.1]
test_list2 = [2, [11, 5], 9, 'all', 1]
test_list3 = []
test_list4 = [{'r': 1}, 'incorrect', (), 0, False]

apply_all_func(test_list0, min_elem, max_elem, sum_elem, len_list, sorted_list)
apply_all_func(test_list1, min_elem, max_elem, sum_elem, len_list, sorted_list)
apply_all_func(test_list2, min_elem, max_elem, sum_elem, len_list, sorted_list)
apply_all_func(test_list3, min_elem, max_elem, sum_elem, len_list, sorted_list)
apply_all_func(test_list4, min_elem, max_elem, sum_elem, len_list, sorted_list)