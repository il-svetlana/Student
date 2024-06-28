# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Составьте второй список primes, содержащий только простые числа из первого.
# А также третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes в консоль.

list_based = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in list_based:
    if i == 1:
        continue
    else:
        flag_not_primes = False
        for j in range(2, i):
            if flag_not_primes:
                break
            elif i % j == 0:
                not_primes.append(i)
                flag_not_primes = True
        if not flag_not_primes:
            primes.append(i)

print('Базовый список чисел: ', list_based)
print('Список простых чисел: ', primes)
print('Список не простых чисел: ', not_primes)