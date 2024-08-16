class Animal:
    fed = False
    alive = True

    def __init__ (self, name):
        self.name = name
        self.fed = Animal.fed
        self.alive = Animal.alive

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел(а) {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал(а) есть {food.name}')
            self.alive = False
class Plant:
    edible = False

    def __init__ (self, name):
        self.name = name
        self.edible = Plant.edible
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    def __init__ (self, name):
        self.name = name
class Fruit(Plant):
    def __init__ (self, name, edible = True):
        self.name = name
        self.edible = edible

# условие, в котором Animal едят только Fruit - хоть Predator, хоть Mammal - без ножа режет.
# но ТЗ есть ТЗ

tiger = Predator('Тигр')
cow = Mammal('Корова')
peony = Flower('Пион')
apple = Fruit('Яблоко')

tiger.eat(peony)
cow.eat(apple)
