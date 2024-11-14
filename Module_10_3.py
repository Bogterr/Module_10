import random
import time
import threading


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        count_ammount = 100
        while count_ammount > 0:

            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()

            deposit_amount = random.randint(50, 500)
            self.balance = self.balance + deposit_amount
            print(f'Пополнение: {deposit_amount}. Баланс: {self.balance}')

            count_ammount -= 1
            time.sleep(0.001)


    def take(self):
        count_ammount = 100
        while count_ammount > 0:

            take_amount = random.randint(50, 500)
            print(f'Запрос на {take_amount}')

            if take_amount <= self.balance:
                self.balance = self.balance - take_amount
                print(f'Снятие: {take_amount}. Баланс: {self.balance}')

            elif take_amount > self.balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()

            count_ammount -= 1
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print()
print(f'Итоговый баланс: {bk.balance}')
