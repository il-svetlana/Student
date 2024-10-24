# Напишите функцию-генератор all_variants(text), которая принимает строку text и
# возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.

# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc

def all_variants(text):
    if not type(text) == str:
        raise TypeError('Значение должно являться строкой.')
    elif not text:
        raise ValueError('Значение не должно быть пустым.')
    else:
        print('Проверки пройдены.')
        for i in range(len(text) + 1):
            for j in range(i):
                if j < len(text):
                    yield text[j:i]

a = all_variants("abc")
for i in a:
    print(i)