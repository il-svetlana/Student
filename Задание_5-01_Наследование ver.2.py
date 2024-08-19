class Animal:
    fed = False
    alive = True

    def __init__ (self, name):
        self.name = name

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
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

tiger = Predator('Тигр')
cow = Mammal('Корова')
peony = Flower('Пион')
apple = Fruit('Яблоко')

tiger.eat(peony)
cow.eat(apple)
cow.eat(peony)
tiger.eat(apple)


