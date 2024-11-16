# Задача "Многопроцессное считывание"

import multiprocessing
import threading
import time
from threading import current_thread


def read_info(name):
    all_data = []

    start_time = time.time()
    with open(name) as f:
        for line in f:
            r_line = f.readline()
            all_data.append(r_line)
    end_time = time.time()
    print(f'Поток {current_thread().name} закончил работу с файлом {name}. Время {end_time - start_time}')
    # print(f'Процесс {current_process.__name__} окончил работу с файлом {name}, времени задействовано: {end_time - start_time}')



filenames = [f'./file {number}.txt' for number in range(1, 5)]
# print(filenames)

######################################################################################

# ЛИНЕЙНЫЙ
# start = time.time()
# for filename in filenames:
#     read_info(filename)
# end = time.time()
# print()
# print(f'Линейный процесс затратил времени всего: {end - start}')

######################################################################################

# МУЛЬТИПРОЦЕССОРНЫЙ
if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = time.time()
    print()
    print(f'Мультипроцессорный процесс затратил времени всего: {end - start}')

######################################################################################

# МУЛЬТИПОТОЧНЫЙ
# all_threads = [len(filenames)]
# start = time.time()
# for thread in range(all_threads[0]):
#     thread = threading.Thread(target=read_info, args=(filenames[thread],))
#     thread.start()
#     thread.join()
# end = time.time()
# print(f'Мультипоточный процесс затратил времени всего: {end - start}')
######################################################################################