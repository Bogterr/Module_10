import threading
import time


# class MyThread(threading.Thread):
#     def __init__(self, name, counter, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.counter = counter
#         self.delay = delay
#
#     def timer(self, name, counter, delay):
#         while counter:
#             time.sleep(delay)
#             print(f'{name} {time.ctime(time.time())}')
#             counter -= 1
#
#     def run(self):
#         print(f'Поток {self.name} запущен')
#         self.timer(name=self.name, counter=self.counter, delay=self.delay)
#         print(f'Поток {self.name} завершен')
#
#
#
#
#
# thread1 = MyThread('thread1', 5, 1)
# thread2 = MyThread('thread2', 3, 0.5)
#
# thread1.start()
# thread2.start()

###########################################################
# За честь и отвагу!

class Knight(threading.Thread):
    def __init__(self, name, power, delay=1):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.delay = delay

    def fight(self, delay):
        count_enemies = 100
        days = 0
        while count_enemies > 0:
            print(f'{self.name} сражается {days}..., осталось {count_enemies} воинов.')
            count_enemies = count_enemies - self.power
            time.sleep(delay)
            days += 1

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight(self.delay)

    def victory(self):
        print(f'Все битвы закончились!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения

first_knight.victory()