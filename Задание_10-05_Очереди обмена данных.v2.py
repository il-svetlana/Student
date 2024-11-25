import random
import time
from threading import Thread
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name} начал(а) есть.")
        time.sleep(random.randint(5, 15))
        print(f"{self.name} закончил(а) есть.")

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                print(f"{guest.name} сел(-а) за стол N {free_table.number}.")
                guest.start()
                # time.sleep(random.randint(1, 4))
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди.")
                # time.sleep(random.randint(1, 4))

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(а) и ушёл(а). "
                          f"Стол N {table.number} свободен.")
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        print(f"{next_guest.name} вышел(ла) из очереди и сел(а) за стол N {table.number}.")
                        table.guest.start()


guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey',
                'Darya', 'Arman', 'Victoria', 'Nikita',
                'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]
tables = [Table(number) for number in range(1, 6)]
cafe = Cafe(*tables)

cafe.guest_arrival(*guests)
cafe.discuss_guests()


