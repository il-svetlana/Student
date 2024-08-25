class WordsFinder:

    def __init__(self, *new_name_files):
        # объект должен принимать неограниченное кол-во названий файлов
        # и записывать их в атрибут file_names в списке списка/кортежа
        self.file_names = []

        for names in new_name_files:
            if isinstance(names, str):
                if '.' not in names:
                    print('Ошибка инициализации объекта: '
                          'формат файла не указан: ')
                    self.file_names.append(None)
                else:
                    self.file_names.append(names)
            else:
                print('Ошибка инициализации объекта: '
                      'данные не являются типом str.')
                self.file_names.append(None)
    def get_all_words(self):
    # возвращает словарь {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'],...}
    # 'file1.txt', 'file2.txt', ...' - названия файлов.
    # ['word1', 'word2'], ['word3', 'word4'], ... - слова, содержащиеся в этом файле.
    # строки переводить в lower, пунктуацию убрать (дефис в слове - не убирать, тире  - убирать)

        new_dict = {}
        for elem in self.file_names:
            punctuation = ('.', ',', ':', ';', '?', '!', '- ', '"',  '(', ')')

            with open(elem, mode='r', encoding='utf-8') as temp_file:
                temp_file.seek(0)
                all_text = temp_file.read().lower().split('\n')

            for i in range(len(all_text)):
                for mark in punctuation:
                    all_text[i] = all_text[i].replace(mark, '')

            new_dict[elem] = all_text
        return new_dict

    def find(self, word):
        # Возвращает словарь,
        # где ключ - название файла,
        # значение - позиция первого такого слова в списке слов этого файла.
        dict_pos = {}
        count = 0
        flag = False

        for elem_key, elem_value in self.get_all_words().items():
            if word.lower() in elem_value:
                for elem in elem_value:
                    if word.lower() == elem:
                        dict_pos[elem_key] = count
                        return dict_pos
                    count += 1

        if not flag:
            print('Слово не найдено.')
            return None

    def count(self, word):
        # Возвращает словарь,
        # где ключ - название файла,
        # значение - количество слова word в списке слов этого файла.
        flag = False
        dict_pos = {}

        for elem_key, elem_value in self.get_all_words().items():
            if word.lower() in elem_value:
                dict_pos[elem_key] = 0
                print(f'Найдено в value : {elem_value}')
                for elem in elem_value:
                    if word.lower() == elem:
                        flag = True
                        dict_pos[elem_key] += 1

        if not flag:
            print('Слово не найдено.')
            return None
        else:
            return dict_pos


test1 = WordsFinder('items.txt', 'names.txt', 'special text.txt')
print('1 - Тест для инициализации: ', test1.file_names, '\n')
print('2 - Тест для get_all_words: ')
print('')
for elem in test1.get_all_words().items():
    print(elem)
print('')
print('3 - Тест для find: ')
word1 = 'кот'
print(f'Первая найденная позиция заданного слова '
      f'(отсчёт с нуля): "{word1}": ', test1.find(word1))
print('')
print('4 - Тест для count: ')
print('Кол-во найденных позиций заданного слова: ', test1.count(word1))