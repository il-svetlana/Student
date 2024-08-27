import os
import time

file1 = 'items.txt'
file2 = 'names.txt'
file3 = 'special text.txt'
directory = os.getcwd()

# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
for root, dirs, files in os.walk(directory):
    # print(f"Корневой каталог: {root}")

    for file in files:

        if file in [file1, file2, file3]:
            # Примените os.path.join для формирования полного пути к файлам.
            file_path = os.path.join(root, file)

            # Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
            last_modified_time = os.path.getmtime(file_path)
            formatted_time = time.ctime(last_modified_time)

            # Используйте os.path.getsize для получения размера файла.
            file_size = os.path.getsize(file_path)

            # Используйте os.path.dirname для получения родительской директории файла.
            parent_directory = os.path.dirname(file_path)

            print(f'Файл: {file}')
            print(f'- Полный путь: {file_path}')
            print(f'- Время последнего изменения: {formatted_time}')
            print(f'- Размер: {file_size} байт')
            print(f'- Родительская директория: {parent_directory}')