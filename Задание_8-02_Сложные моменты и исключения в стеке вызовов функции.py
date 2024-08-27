def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            if isinstance(i, bool):
                incorrect_data += 1
            else:
                result += i
        except TypeError as exc:
            print(f'В numbers записан некорректный тип данных : {exc}')
            incorrect_data += 1
    tuple_sum = (result, incorrect_data)
    return tuple_sum

def calculate_average(numbers):
    try:
        temp_dict = personal_sum(numbers)
        average = round(temp_dict[0] / (len(numbers) - temp_dict[1]), 2)
    except ZeroDivisionError as exc:
        print('Пресечена попытка деления на ноль. Обнуление значений.')
        average = 0
    return average

str1 = [10, 20, 30, 10]
str2 = [10, '20, 30, 10', 0, -5, True, 6]
str3 = [8, [20, 30], -4]
str4 = []

print(personal_sum(str1))
print('Среднее арифметическое str1: ', calculate_average(str1), '\n')
print(personal_sum(str2))
print('Среднее арифметическое str1: ', calculate_average(str2), '\n')
print(personal_sum(str3))
print('Среднее арифметическое str1: ', calculate_average(str3), '\n')
print(personal_sum(str4))
print('Среднее арифметическое str1: ', calculate_average(str4), '\n')


