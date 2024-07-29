class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.args = args
        cls.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(cls, key, value)
        cls.houses_history.append(cls.name)
        return object.__new__(cls)

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __del__(self):
        print(f'{self.name} удалён, но останется в истории')
        return None

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

center1_kw = {'name': 'ЖК Эльбрус', 'num_of_floors': 3}
center2_kw = {'name': 'ТЦ ДАРС', 'num_of_floors': 5}

trade_center_1 = House(**center1_kw)
print('Объект 1: ', trade_center_1)
print('houses_history:', House.houses_history)

trade_center_2 = House(**center2_kw)
print('Объект 2: ', trade_center_2)
print('houses_history:', House.houses_history)

del trade_center_1
print('houses_history:', House.houses_history)