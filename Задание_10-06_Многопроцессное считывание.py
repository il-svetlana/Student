import time
import multiprocessing

def read_info(name):
    all_data = []
    try:
        with open(name, 'r', encoding='utf-8') as file_:
            file_.seek(0)
            line = file_.readline()
            while line:
                all_data.append(line.strip())
                line = file_.readline()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{name}' не найден.")

filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вывод

# print('Запущен линейный вызов функций. Ждите.')
# timed_start = time.time()
# all_result = list(map(read_info, filenames))
# timed_end = time.time()
# print(f'Время выполнения при линейном вызове: {timed_end - timed_start}')

# Мультипроцессный вывод

if __name__ == '__main__':
    print('Запущен мультипроцессный вызов функций. Ждите.')
    timed_start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(read_info, filenames)
    timed_end = time.time()
    print(f'Время выполнения при мультипроцессном вызове: {timed_end - timed_start}')

