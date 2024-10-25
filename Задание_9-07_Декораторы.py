def is_prime(func):
    # Функция декоратор, которая распечатывает "Простое", если результат 1ой функции будет простым числом
    # и "Составное" в противном случае.
    def wrapper(a, b, c):
        tmp_num = func(a, b, c)
        if tmp_num > 1:
            for i in range(2, tmp_num):
                if not tmp_num % i:
                    print("Составное")
                    break
            print("Простое")
        else:
            print("Простое")
        return tmp_num
    return wrapper

@is_prime
def sum_three(a, b, c):
    # Функция, которая складывает 3 числа
    result = a + b + c
    return result

result1 = sum_three(2, 3, 6)
print(result1)

