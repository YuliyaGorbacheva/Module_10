from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemys = 100
        days = 0
        while enemys:
            enemys -= self.power
            days += 1
            sleep(1)
            print(f'{self.name} сражается {days} дней, осталось {enemys} воинов')
        print(f'{self.name} одержал победу спустя {days} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
