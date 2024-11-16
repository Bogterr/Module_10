# Задача "Потоки гостей в кафе"

from queue import Queue
import time
import threading
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sec_ = random.randint(3, 10)
        time.sleep(sec_)


class Cafe:
    spis_thr = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        spis_guests = list(guests)
        spis_tables = self.tables
        len_spis_guests = len(spis_guests)
        # print(f'Спислк гостей (количество): {len_spis_guests}')
        min_guests_tables = min(len_spis_guests, len(spis_tables))
        # print(f'Количество столов в кафе: {min_guests_tables}')

        for table in range(min_guests_tables):
            spis_tables[table].guest = guests[table]
            thr = guests[table]
            thr.start()
            Cafe.spis_thr.append(thr)
            print(f'{spis_guests[table].name} сел за стол {spis_tables[table].number}')
        if len_spis_guests > min_guests_tables:
            for count in range(min_guests_tables, len_spis_guests):
                self.queue.put(guests[count])
                print(f'{spis_guests[count].name} в очереди')

##################################################################################
        # for guest in guests:
        #     for table in self.tables:
        #         if table.guest is None:
        #             guest.start()
        #             print(f'{guest.name} сел за стол номер {table.number}')
        #             table.guest = guest
        #             break
        #     else:
        #         print(f'{guest.name} ожидает в очереди')
        #         self.queue.put(guest)
###################################################################################

    def discuss_guests(self):

        while not self.queue.empty() or Cafe.table_is_busy(self):
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive(): # Если поток окончился, и стол занят
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None                                      # Освободи стол
                if not self.queue.empty() and table.guest is None:          # Если очередь не пуста и стол пуст
                    table.guest = self.queue.get()                          # Посадить за стол из очереди
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thr = table.guest
                    thr.start()
                    Cafe.spis_thr.append(thr)

###############################################################################
            # if len(Cafe.spis_thr) != 0:
            #     print(f'Количество потоков: {len(Cafe.spis_thr)}')
            #     for thr in Cafe.spis_thr:
            #         thr.is_alive()
            #         print(f'Поток жив: {thr.is_alive()}') True - да / False - нет
            #         if thr.is_alive():
            #             print(f'{thr.name} за столом №{}')
###############################################################################

    def table_is_busy(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
cafe.discuss_guests()


# print('1: ', len(tables))
# print('2: ',len(guests))
# print('3: ', guests)
# print('4: ', len(cafe.tables))



####################################################





















