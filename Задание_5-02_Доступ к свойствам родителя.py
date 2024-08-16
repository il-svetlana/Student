class Vehicle:
    __COLOR_VARIANTS = ['white', 'blue', 'red']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return 'Модель: ' + self.__model

    def get_horsepower(self):
        return 'Мощность: ' + str(self.__engine_power)
    def get_color(self):
        return 'Цвет: ' + self.__color

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец: ', self.owner)

    def set_color(self, new_color):
        flag = False
        for find_color in self.__COLOR_VARIANTS:
            if new_color.lower() == find_color.lower():
                flag = True
        if flag:
            self.__color = new_color
            print(f'Цвет изменен на {new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# исходные данные
lada  = Sedan('Michael', 'Granta', 500, 'black')

# проверка стандартных методов
print(lada.get_model())
print(lada.get_horsepower())
print(lada.get_color())
print('')

# методы изменения атрибутов
lada.set_color('red')
lada.set_color('pink')
print('')

# проверка метода вызова общей информации
lada.print_info()





