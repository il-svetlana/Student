def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()
print_params(2)
print_params(b='другая строка')
print_params(25, 'fly', False)
print_params(a='внезапно', b=True, c=5)

values_list = ['Нулевой', True, 1]
values_dict = {'a': 15, 'b': False, 'c': 'string'}

print_params(*values_list)
print_params(**values_dict)

