# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) -
# должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) -
# должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__ (self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors
    def __len__(self):
        return self.num_of_floors
    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.num_of_floors}'
    def go_to(self, new_floor):
        if new_floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print('Этаж № ', i)

trade_center = House('ЖК Эльбрус', 5)
trade_center.go_to(3)
print('Вызов __len__: ', len(trade_center))
print('Вызов __str__: ', str(trade_center))