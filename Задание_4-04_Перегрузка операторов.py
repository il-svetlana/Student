# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) -
# должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
# должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам.
# Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) -
# увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) -
# работают так же как и __add__ (возвращают результат его вызова).
#
class House:
    def __init__ (self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors
    def __len__(self):
        return self.num_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.num_of_floors == other.num_of_floors
        else:
            return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors < other.num_of_floors
        elif isinstance(other, int):
            return self.num_of_floors < other
        else:
            return False
    def __le__(self, other):
        if isinstance(other, House):
            return self.num_of_floors <= other.num_of_floors
        elif isinstance(other, int):
            return self.num_of_floors <= other
        else:
            return False
    def __gt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors > other.num_of_floors
        elif isinstance(other, int):
            return self.num_of_floors > other
        else:
            return False
    def __ge__(self, other):
        if isinstance(other, House):
            return self.num_of_floors >= other.num_of_floors
        elif isinstance(other, int):
            return self.num_of_floors >= other
        else:
            return False
    def __ne__(self, other):
        if isinstance(other, House):
            return self.num_of_floors != other.num_of_floors
        elif isinstance(other, int):
            return self.num_of_floors != other
        else:
            return False
    def __add__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self.num_of_floors
        else:
            print(f'Некорректное значение value = "{value}"')
            return 'ERROR VALUE'
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
    def go_to(self, new_floor):
        if new_floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print('Этаж № ', i)

trade_center_1 = House('ЖК Эльбрус', 3)
trade_center_2 = House('ТЦ ДАРС', 3)

print('Объект 1: ', trade_center_1)
print('Объект 2: ', trade_center_2)
print(f'Кол-во этажей {trade_center_1.name} и {trade_center_2.name} одинаково: ',
      trade_center_1 == trade_center_2, '\n') # __eq__

new_floor_1 = 2
print(f'Объекту {trade_center_1.name} Наф-Наф достроил {new_floor_1} этажа, итого: ',
      trade_center_1 + new_floor_1) # __add__
new_floor_2 = 3
print(f'Объекту {trade_center_2.name} Нуф-Нуф достроил {new_floor_2} этажа, итого: ',
      new_floor_2 + trade_center_2, '\n') # __radd__

print(f'Кол-во этажей {trade_center_1.name} < {trade_center_2.name}: ',
      trade_center_1 < trade_center_2) # __lt__

print(f'Кол-во этажей  {trade_center_1.name} <= {trade_center_2.name}: ',
      trade_center_1 <= trade_center_2) # __le__

print(f'Кол-во этажей  {trade_center_1.name} != {trade_center_2.name}: ',
      trade_center_1 != trade_center_2) # __ne__

print(f'Кол-во этажей  {trade_center_1.name} >= {trade_center_2.name}: ',
      trade_center_1 >= trade_center_2) # __ge__

print(f'Кол-во этажей  {trade_center_1.name} > {trade_center_2.name}: ',
      trade_center_1 > trade_center_2) # __gt__
