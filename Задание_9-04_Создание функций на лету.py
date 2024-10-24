# Lambda-функция:
# Необходимо составить lambda-функцию для следующего выражения - list(map(lambda?, first, second)).
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.

first = 'Мама мыла раму'
second = 'Рамена мало было'
third = list(map(lambda x, y: x == y, first, second))
print(third)

# ------------------------------
# Замыкание:

def get_advanced_writer(file_name):
    # Принимает название файла для записи
    # Логика заключается в добавлении в файл file_name всех данных из data_set в том же виде.
    # Функция get_advanced_writer возвращает функцию write_everything.
    def write_everything(*data_set):
      # data_set - параметр, принимающий неограниченное количество данных любого типа.
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

writed = get_advanced_writer('example_9-04.txt')
writed('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# ------------------------------
# Метод call
# Создайте класс MysticBall, объекты которого обладают атрибутом words, хранящий коллекцию строк.
# В этом классе также определите метод call который будет случайным образом выбирать слово из words
# и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции
# можете использовать функцию choice из модуля random.

from random import choice

class MysticBall:

  def __init__(self, *words):
    self.words = list(words)
  def call(self):
    return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball.call())
print(first_ball.call())
print(first_ball.call())