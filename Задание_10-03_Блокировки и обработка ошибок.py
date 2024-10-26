# Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
# После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".
#
# По итогу вы получите скрипт разблокирующий поток до баланса равному 500 и больше или
# блокирующий, когда происходит попытка снятия при недостаточном балансе.

from threading import Thread, Lock
import random
import time
class Bank:

    def __init__(self, balance):
        if type(balance) == int:
            self.balance = balance
            self.lock = Lock()
            print(f'Объект инициализирован. Баланс {self.balance}')
        else:
            print('[!] Ошибка инициализации объекта')
            self.balance = None
            self.lock = Lock()
    def deposit(self):
        for _ in range(10):
            try:
                self.lock.acquire()

                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()

                deposition = random.randrange(50, 500)
                self.balance += deposition
                print(f'Пополнение: {deposition}. Баланс: {self.balance}.')
            except:
                print('[!] При пополнении баланса произошла ошибка.')
            finally:
                if self.lock.locked():
                    self.lock.release()
                time.sleep(0.003)

    def take(self):
        for _ in range(10):
            try:
                self.lock.acquire()
                take_sum = random.randrange(50, 500)
                print(f'Запрос на снятие: {take_sum}.')
                if self.balance >= take_sum:
                    self.balance -= take_sum
                    print(f'Снятие {take_sum}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён - недостаточно средств.')
            except:
                print('[!] При запросе на снятие произошла ошибка.')
            finally:
                if self.lock.locked():
                    self.lock.release()
                time.sleep(0.003)


VTB = Bank(300)

thr_1 = Thread(target=VTB.deposit)
thr_2 = Thread(target=VTB.take)

thr_1.start()
thr_2.start()

thr_1.join()
thr_2.join()

print(f'Итоговый баланс: {VTB.balance}')