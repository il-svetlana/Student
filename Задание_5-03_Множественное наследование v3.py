class Horse:
    sound = 'Frrr'

    def __init__(self, x_distance=0):
        self.x_distance = x_distance

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, y_distance=0):
        self.y_distance = y_distance

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def __init__(self, x_distance=0, y_distance=0):
        Horse.__init__(self, x_distance)
        Eagle.__init__(self, y_distance)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        position = (self.x_distance, self.y_distance)
        return position

    def voice(self):
        sound = Horse.sound + ' ' + Eagle.sound
        return sound

desert = Pegasus()
desert.move(10, 3)
print('Координаты пегаса: ', desert.get_pos())
print('Пегас издает звуки: ', desert.voice(),'\n')

desert2 = Pegasus()
desert2.move(5, 6)
print('Координаты пегаса: ', desert2.get_pos())
print('Пегас издает звуки: ', desert2.voice(),'\n')


