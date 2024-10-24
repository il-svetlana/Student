# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.

# Создайте класс Iterator, который обладает следующими свойствами:
# Атрибуты объекта:
# start - целое число с которого начинается итерация.
# stop - целое число на котором заканчивается итерация.
# step - шаг с которой совершается итерация.
# pointer - указывает на текущее число в итерации (изначально start)

# Пункты задачи:

# Создайте несколько объектов класса Iterator и совершите итерации с ними при помощи цикла for.
# Особое внимание уделите методу __next__ и условиям в нём.

class StepValueError(ValueError):
    pass
class Iterator:

    def __init__(self, start, stop, step=1):
    # принимает значения старта и конца итерации, а также шага.
    # В этом методе в первую очередь проверяется step на равенство 0.
    # Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')

        if step == 0:
            raise StepValueError('Значение step не должно быть 0')
        else:
            self.start = start
            self.stop = stop
            self.step = step
            self.pointer = start

    def __iter__(self):
    # сбрасывает значение pointer на start и возвращает сам объект итератора.
        self.pointer = self.start
        return self

    def __next__(self):
    # метод увеличивающий атрибут pointer на step.
    # В зависимости от знака атрибута step итерация завершится
    # либо когда pointer станет больше stop, либо меньше stop

        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration('Итерация завершена')
        elif self.step < 0 and self.pointer < self.stop:
            raise StopIteration('Итерация завершена')

        start_pointer = self.pointer
        self.pointer += self.step

        return start_pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()