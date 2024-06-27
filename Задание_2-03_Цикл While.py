# Нужно выписывать из данного списка только положительные числа,
# пока не встретите отрицательное или не закончится список.

based_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num_based = 0

while num_based < len(based_list):
    if based_list[num_based] < 0:
        print('Найдено отрицательное число, просмотр закончен.')
        break
    elif based_list[num_based] > 0:
        print('Найдено положительное число: ', based_list[num_based])
    num_based += 1




