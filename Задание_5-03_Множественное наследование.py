class Horse:
    x_distance = 0
    sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx
class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy
class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        return [Horse.sound, ' ', Eagle.sound]

desert = Pegasus()
desert.move(18, 3)
print('Координаты пегаса: ', desert.get_pos())
print('Пегас издает звуки: ', *desert.voice())
