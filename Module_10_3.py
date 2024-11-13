import random
import threading
import time



# counter = 0
# lock = threading.Lock()
# # print(lock.locked())
#
# def increment(name):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter += 1
#         print(name, counter, """lock.locked()""")
#     lock.release()
#
# def decrement(name):
#     global counter
#     try:
#         lock.acquire()
#         for i in range(1000):
#             counter -= 1
#             print(name, counter, """lock.locked()""")
#     except Exception:
#         pass
#     finally:
#         lock.release()
#
# thread_1 = threading.Thread(target=increment, args=('Thread-1',))
# thread_2 = threading.Thread(target=decrement, args=('Thread-2',))
# thread_3 = threading.Thread(target=increment, args=('Thread-3',))
# thread_4 = threading.Thread(target=decrement, args=('Thread-4',))
#
# thread_1.start()
# thread_3.start()
# thread_2.start()
# thread_4.start()
######################################################
# Задача "Банковские операции"          ##############
######################################################


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.blocked = False
        self.count_amount = 100
        self.count_take = 100
        self.take_chance = 3


    def deposit(self):
        #print(f'Стартовая блокировка пополнение: {self.lock.locked()} ############################')
        while self.count_amount > 0:
            if self.blocked == True:
                break
            else:
                if self.balance >= 500 and self.lock.locked():
                    print('#'* 50)
                    print(f'Пополнение перед разблокировкой: {self.lock.locked()}')
                    self.lock.release()
                    print(f"Пополнение разблокировано: {self.lock.locked()}")
                    print('#'* 50)
                else:
                    pass
                deposit_amount = random.randint(50, 500)
                self.balance += deposit_amount
                print(f'Пополнение: {deposit_amount}. Баланс: {self.balance}')
                self.count_amount -= 1
                print(f'Осталось поолнений: {self.count_amount}')
                time.sleep(0.01)
                # print()
                # print(f'Статус блокировки на пополнение: {self.lock.locked()}')
                # print()

    def take(self):
        while self.count_take > 0:
            if self.take_chance <= 0:
                break
            else:
                take_amount = random.randint(50, 500)
                print(f'Запрос на: {take_amount}')
                if take_amount > self.balance and self.count_amount == 0:
                    print(f'Снятие суммы: {take_amount} не представляется возможным,\n'
                          f'количество пополнений: {self.count_amount}\n')
                    self.take_chance -= 1
                    print(f"Повторных попыток на снятие: {self.take_chance}")
                elif take_amount > self.balance and self.count_amount > 0:
                    print(f'Запрос отклонён, недостаточно средств')
                    print('#'* 50)
                    # print(f'Снятие перед блокировкой: {self.lock.locked()}')
                    self.lock.acquire()
                else:
                    self.balance -= take_amount
                    self.count_take -= 1
                    print(f'Снятие: {take_amount}. Баланс: {self.balance}')
                    print(f'Осталось снятий: {self.count_take}')
                    # if self.lock.locked() == True:
                    #     print(self.lock.locked())
                    #     self.lock.release()
                    #     print('Мы видим, что Вы пытаетесь снять средства, но счёт уже заблокирован.')
                    #     print("Специально для Вас, счёт временно разблокирован")
                    #     print('Пополнение возможно: ', th1.is_alive())
                    #     print('Снятие возможно: ', th2.is_alive())
                    #     # self.blocked = True
                    #     # break
                    # else:
                    #     self.lock.acquire()
                    #     print(f'Снятие заблокировано: {self.lock.locked()}')
                    #     print('#'* 50)
                time.sleep(0.01)

    def total_balance(self):
        print(f'Итоговый баланс: {self.balance}')

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print()
print('#'*50)
print(f'#####          Итоговый баланс: {bk.balance}         #####')
print('#'*50)