class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message

class Car:

    def __init__(self, model, vin, numbers):

        self.model = model # str
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if vin_number in range(1000000, 10000000):
                return True
            else:
                raise IncorrectVinNumber('ERROR. Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('ERROR. Некорректный тип vin')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('ERROR. Неверная длина номера')
        else:
            raise IncorrectCarNumbers('ERROR. Некорректный тип данных для номеров.')

try:
    car1 = Car('Lada', 9999999, 'ERC201')
except IncorrectVinNumber as err1:
    print('Сообщение об ошибке. ', err1.message)
except IncorrectCarNumbers as err2:
    print('Сообщение об ошибке. ', err2.message)