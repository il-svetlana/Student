# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function,
# функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function():
    def inner_function():
        text = "Я в области видимости функции test_function"
        print(text)
    inner_function()

test_function()
# inner_function() - вызов вне функции test_function выдаст ошибку, т.к. является локальным именем