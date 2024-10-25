from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        warriors = 100
        day = 0
        while warriors > 0:
            day += 1
            warriors -= self.power
            print(f'{self.name} сражается {day} дней, осталось победить {warriors} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

threads = []

threads.append(Knight('Sir Lancelot', 10, ))
threads.append(Knight('Sir Galahad', 20, ))

for thread in threads:
    thread.start()
    time.sleep(1)

for thread in threads:
    thread.join()

print('Все битвы закончились!')
