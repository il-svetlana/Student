from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        flag = False

        if isinstance(name, str) and isinstance(category, str):
            if name != '' and category != '':
                self.name = name
                self.category = category
            else:
                flag = True
        else:
            flag = True

        if isinstance(weight, float):
            self.weight = weight
        else:
            flag = True

        if flag:
            print('Объект класса Pruduct не был инициализирован.')
            self.name = None
            self.category = None
            self.weight = None

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
            file = open(self.__file_name, encoding='utf-8')
            file.seek(0)
            products = file.read().replace('\n', ', ')
            file.close()
            return products

    def add(self, *products):
        new_list = []

        for new_product in products:
            if new_product.name not in self.get_products():
                new_list.append(new_product)

        file = open(self.__file_name, mode='a', encoding='utf-8')
        for new_product in products:
            if new_product in new_list:
                file.write('\n' + new_product.name)
            else:
                print(f'Продукт {new_product.name} уже есть в магазине')
        file.close()

product1 = Product('Картофель', 5.2, 'Овощи')
product2 = Product('Кофе', 0.250, 'Бакалея')
product3 = Product('Апельсин', 1.5, 'Фрукты')
magnit = Shop()
print('Начальный набор продуктов: ', magnit.get_products())
magnit.add(product1, product2, product3)
print(f'Набор продуктов после закупки: ', magnit.get_products())
