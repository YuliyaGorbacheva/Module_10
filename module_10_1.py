# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков

import threading
import time
from datetime import datetime


def write_words(word_count, file_name):
    word_count = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        while word_count < 10:
            time.sleep(0.1)
            word_count += 1
            file.write(f'Какое-то слово №{word_count}\n')

    print(f'Завершилась запись в файл {file.name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.now()
res_time = time_stop - time_start
print(f'Работа функции {res_time}')

thread1 = threading.Thread(write_words(10, 'example5.txt'))
thread2 = threading.Thread(write_words(30, 'example6.txt'))
thread3 = threading.Thread(write_words(200, 'example7.txt'))
thread4 = threading.Thread(write_words(100, 'example8.txt'))

time2_start = datetime.now()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time2_stop = datetime.now()
res2_time = time2_stop - time2_start
print(f'Работа потоков {res2_time}')
