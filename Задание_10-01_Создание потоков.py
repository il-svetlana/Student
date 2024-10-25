# После создания файла вызовите 4 раза функцию write_words.
# После вызовов функций создайте 4 потока для вызова этой функции.
# Запустите эти потоки.
# Измерьте время, затраченное на выполнение функций и потоков.

import time
from threading import Thread

def write_words(word_count, file_name):
    # word_count - количество записываемых слов.
    # file_name - название файла, куда будут записываться слова.
    # Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
    # в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
    work_file = open(file_name, 'w')

    for i in range(1, word_count + 1):
        work_file.write(f'Какое-то слово № {i}\n')
        time.sleep(0.1)

    work_file.close()
    print(f'Завершилась запись в файл {file_name}.')

# Запуск 4 функций

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f'Работа функций: {end_time - start_time:.4f} сек.\n')

# Запуск 4 потоков

start_time = time.time()

threads = []
threads.append(Thread(target=write_words, args=(10, 'example5.txt', )))
threads.append(Thread(target=write_words, args=(30, 'example6.txt', )))
threads.append(Thread(target=write_words, args=(200, 'example7.txt', )))
threads.append(Thread(target=write_words, args=(100, 'example8.txt', )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f'Работа потоков: {end_time - start_time:.4f} сек.')


