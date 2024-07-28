# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor),
# где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1,
# то вывести строку "Такого этажа не существует".

class House:
    def __init__ (self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors
    def go_to(self, new_floor):
        if new_floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print('Этаж № ', i)

trade_center = House('ЖК Эльбрус', 5)
trade_center.go_to(3)

