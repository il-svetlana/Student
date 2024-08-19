class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        flag = False
        if isinstance(sides, list):
            for val_sides in sides:
                if not isinstance(val_sides, int):
                    flag = True
                    break
                elif val_sides <= 0:
                    flag = True
                    break
        else:
            flag = True

        if isinstance(color, list):
            for val_color in color:
                if not isinstance(val_color, int):
                    flag = True
                    break
                elif val_color < 0:
                    flag = True
                    break
        else:
            flag = True

        if not isinstance(filled, bool):
            flag = True

        if not flag:
            self.__sides = sides
            self.__color = color
            self.filled = filled
        else:
            print('Объект не был инициализирован.')
            self.__sides = None
            self.__color = None
            self.filled = None

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        flag_type = False

        for val_color in r, g, b:
            if not isinstance(val_color, int):
                flag_type = True
                break
            elif val_color < 0:
                flag_type = True
                break

        if flag_type:
            print('Некорректное значение color')
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            print('Цвет был изменен.')
            self.__color = [r, g, b]
            return self.__color
        else:
            print('Цвет не был изменен')
            return self.__color

    def __is_valid_sides(self, list_values):
        i = 0
        flag_type = False
        flag_upper_zero = True
        quant = 0

        for values in list_values:
            i += 1
            if not isinstance(values, int):
                flag_type = True
                break

        if flag_type:
            print('Некорректное значение sides')
            return None
        else:
            for values in list_values:
                quant += 1
                if values <= 0:
                    flag_upper_zero = False

            if flag_upper_zero and quant == len(self.__sides):
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            print('Параметры сторон фигуры были изменены.')
            self.__sides = [*new_sides]
        else:
            print('Значение сторон не изменилось.')

        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def print_psbl_Fugire(self, new_color, new_sides):
        print(f'Значение сторон: ', self.get_sides())
        print(f'Текущий цвет : ', self.get_color())
        self.set_color(*new_color)
        print(f'Текущий цвет: ', self.get_color())
        self.set_sides(*new_sides)
        print(f'Параметры сторон: ', self.get_sides())
        print(f'Периметр: ', len(self))

class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled=False):
        if not Circle.sides_count == len(sides):
            sides = [1]
            print('Ошибка значений sides для объекта Circle. '
                  'Установлены значения по умолчанию.\n')
        super().__init__(sides, color, filled=False)
        self.__radius = round(sum(self.get_sides()) / (2 * 3.14159), 2)
        self.__square = round(3.14159 * (len(self.get_sides()) ** 2), 2)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return self.__square

    def print_psbl_Circle(self, new_color, new_sides):
        print(f'Значение сторон: ', self.get_sides())
        print(f'Текущий цвет : ', self.get_color())
        self.set_color(*new_color)
        print(f'Текущий цвет: ', self.get_color())
        self.set_sides(*new_sides)
        print(f'Значение сторон: ', self.get_sides())
        print(f'Длина окружности: ', len(self))
        print(f'Радиус: ', self.get_radius())
        print(f'Площадь: ', self.get_square())

class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled=False):
        if not Triangle.sides_count == len(sides):
            print('Ошибка значений sides для объекта Triangle. '
                  'Установлены значения по умолчанию.\n')
            sides = [1, 1, 1]

        super().__init__(sides, color, filled=False)
        p = 0.5 * sum(self.get_sides())
        self.__square = round((p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5, 2)

    def get_square(self):
        return self.__square

    def print_psbl_Triangle(self,  new_color, new_sides):
        print(f'Значение сторон: ', self.get_sides())
        print(f'Текущий цвет : ', self.get_color())
        self.set_color(*new_color)
        print(f'Текущий цвет: ', self.get_color())
        self.set_sides(*new_sides)
        print(f'Значение сторон: ', self.get_sides())
        print(f'Периметр: ', len(self))
        print(f'Площадь: ', self.get_square())

class Cube(Figure):
    sides_count = 12
    # Переопределить __sides сделав список из 12 одинаковых сторон (передаётся 1 сторона)

    def __init__(self, sides, color, filled=False):

        if len(sides) != 1:
            print('Ошибка значений sides для объекта Cube. '
                  'Установлены значения по умолчанию.\n')
            sides = [1] * Cube.sides_count

        super().__init__(sides, color, filled=False)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = [*new_sides] * Cube.sides_count
        super().set_sides(*new_sides)

    def get_volume(self):
        return (sum(self.get_sides())/Cube.sides_count) ** 3

    def print_psbl_Cube(self,  new_color, new_sides):
        print(f'Значение сторон: ', self.get_sides())
        print(f'Текущий цвет : ', self.get_color())
        self.set_color(*new_color)
        print(f'Текущий цвет: ', self.get_color())
        self.set_sides(*new_sides)
        print(f'Значение сторон: ', self.get_sides())
        print(f'Периметр: ', len(self))
        print(f'Объем: ', self.get_volume())

# Данные для класса Figure
sides_figure1 = [40, 10, 5, 5, 10]
sides_figure2 = [30, 10, 20, 5, 10]
color1 = [255, 0, 0]
color2 = [0, 0, 255]
color3 = [50, 255, 100]
test_figure1 = Figure(sides_figure1, color1, True)
# Данные для класса Circle
sides_circle1 = [50]
sides_circle2 = [60]
test_circle = Circle(sides_circle1, color3)
# Данные для класса Triangle
sides_triangle1 = [10, 10, 4]
sides_triangle2 = [5, 10, 15]
test_triangle = Triangle(sides_triangle1, color2, True)
# Данные для класса Cube
sides_cube1 = [10, 10, 4, 20]
sides_cube2 = [15]
test_cube = Cube(sides_cube1, color1, True)

# Чтение и изменение данных объекта класса Figure
print('Доступные атрибуты и методы для test_figure1')
test_figure1.print_psbl_Fugire(color2, sides_figure2)

# # Чтение и изменение данных объекта класса Circle
print('\nДоступные атрибуты и методы для test_circle')
test_circle.print_psbl_Circle(color1, sides_circle2)
#
# # Чтение и изменение данных объекта класса Triangle
print('\nДоступные атрибуты и методы для test_triangle')
test_triangle.print_psbl_Triangle(color3, sides_triangle2)

# Чтение и изменение данных объекта класса Cube
print('\nДоступные атрибуты и методы для test_cube')
test_cube.print_psbl_Cube(color3, sides_cube2)
