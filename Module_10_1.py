# Задача "Потоковая запись в файлы"
import threading
import time
from threading import current_thread
from time import sleep


prog_start_time = time.time()   # Контроль запуска программы (время)


''' Main часть кода '''
def operation(wc, fn):
    w_count = int(wc)   # переменная числу
    f_name = str(fn)    # str переменная (файлу в данном случае)

    # создаем и пишем файл
    with open(f_name, mode='w', encoding='utf-8') as write_in_file:
        start_time = time.time()                                            # Время, контроль для потока
        # print(f'{f_name}, поток:{threading.current_thread()}')
        for word in range(w_count):                                         # прогон по заданному числу
            write_in_file.write(str(f'Какое-то слово № {word+1}'))          # вписываем в файл
            write_in_file.write('\n')                                       # новая строка
            time.sleep(0.1)                                                 # ожидание
        end_time = time.time()      # Время, конец потока
        # print(current_thread())
        print(f'Завершилась запись в файл {f_name}. Время работы потока {round(end_time-start_time, 4)} \n')


''' Определяем что передано: список или как условлено? '''
def write_words(word_count, file_name=None):

    # print(word_count)
    # print()

    ''' Если список '''
    if type(word_count) is list:
        print("Сценарий: list")

        true_list = word_count
        list_count = 0
        for pos in range(0, len(true_list) - 1, 2):
            list_count += 1
            print(list_count, true_list[pos], true_list[pos+1])
            w_count = true_list[pos]
            f_name = true_list[pos + 1]

            operation(w_count, f_name)

        ''' ВНИМАНИЕ: доделай себе, НЕ ИСКЛЮЧАЕТ все варианты!
                       но для данной ситуации подойдет'''
    else:
        print("Сценарий: operation(word_count, file_name)")
        operation(word_count, file_name)



list_1 = [
    10, 'example1.txt',
    30, 'example2.txt',
    200, 'example3.txt',
    100, 'example4.txt'
    ]

list_2 = [
    10, 'example5.txt',
    30, 'example6.txt',
    200, 'example7.txt',
    100, 'example8.txt',
    ]

list_3 = [
    15, 'test_1.txt',
    50, 'test_2.txt',
    33, 'test_3.txt',
    92, 'test_4.txt',
    10, 'test_5.txt'
]


# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# interceptor(test_list)

# write_words(list_1)
# write_words(list_3)


# write_words(10, 'example5.txt')
# write_words(10, 'example6.txt')
# write_words(10, 'example7.txt')
# write_words(10, 'example8.txt')



thread_1 = threading.Thread(target=write_words, args=(list_2[0], list_2[1]))
thread_2 = threading.Thread(target=write_words, args=(list_2[2], list_2[3]))
thread_3 = threading.Thread(target=write_words, args=(list_2[4], list_2[5]))
thread_4 = threading.Thread(target=write_words, args=(list_2[6], list_2[7]))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()


# print(f'МАРКИРОВАННЫЙ ПОТОК:{current_thread()}')
# print(f'МАРКИРОВАННЫЙ ПОТОК:{current_thread().is_alive()}')
# print(f'Жив_1 = {thread_1.is_alive()}')
# print(f'Жив_2 = {thread_2.is_alive()}')
# print(f'Жив_3 = {thread_3.is_alive()}')
# print(f'Жив_4 = {thread_4.is_alive()}')


#########################################
# Тормозит основной поток (код ниже блока) до завершения раскоментированного потока
#########################################
# current_thread().join() # Вызывает RuntimeError: cannot join current thread
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

prog_end_time = time.time()
print("Работа основной программы окончена")
print("Общее время работы основной программы: ", prog_end_time - prog_start_time)
print()

print("ВНИМАНИЕ: Запущен дополнительный блок программы")

args_5 = (list_3[0], list_3[1])
args_6 = (list_3[2], list_3[3])
args_7 = (list_3[4], list_3[5])
args_8 = (list_3[6], list_3[7])

thread_5 = threading.Thread(target=write_words, args=args_5)
thread_6 = threading.Thread(target=write_words, args=args_6)
thread_7 = threading.Thread(target=write_words, args=args_7)
thread_8 = threading.Thread(target=write_words, args=args_8)

thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()


thread_5.join()
thread_6.join()
thread_7.join()
thread_8.join()

prog_end_time = time.time()
print("Работа программы полностью завершена")
print("Общее время работы всей программы: ", prog_end_time - prog_start_time)







##########################################
# for i in range(3):
#     print(f'{i+1}: ждем 2 секунд')
#
#     print(f'МАРКИРОВАННЫЙ ПОТОК:{current_thread().is_alive()}')
#     print(f'Жив_1 = {thread_1.is_alive()}')
#     print(f'Жив_2 = {thread_2.is_alive()}')
#     print(f'Жив_3 = {thread_3.is_alive()}')
#     print(f'Жив_4 = {thread_4.is_alive()}')
#     sleep(2)
#
# print(f'Жив_1 = {thread_1.is_alive()}')
# print(f'Жив_2 = {thread_2.is_alive()}')
# print(f'Жив_3 = {thread_3.is_alive()}')
# print(f'Жив_4 = {thread_4.is_alive()}')


# print(thread_2.is_alive())
# print(thread_3.is_alive())
# print(thread_4.is_alive())
