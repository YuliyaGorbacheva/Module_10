from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            put_money = randint(50, 500)
            if self.balance <= 500 and self.lock.locked():
                self.balance += put_money
                print(f'Пополнение: {put_money}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            take_money = randint(50, 500)
            print(f'Запрос на {take_money}')
            with self.lock:
                if take_money <= self.balance:
                    self.balance -= take_money
                    print(f'Снятие: {take_money}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонен, недостаточно средств')

            sleep(0.001)



bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
