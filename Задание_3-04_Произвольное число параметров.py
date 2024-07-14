# Напишите функцию single_root_words, которая принимает
# одно обязательное слово в параметр root_word, а далее
# неограниченную последовательность в параметр *other_words.

# Функция должна составить новый список same_words
# только из тех слов списка other_words,
# которые содержат root_word или наоборот
# root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    print('Список same_words: ', same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')