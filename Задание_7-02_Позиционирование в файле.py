def custom_write(file_name, strings):
    str_dict = {}
    num_str = 1
    file = open(file_name, mode='w', encoding='utf-8')
    for i in strings:
        str_dict[(num_str, file.tell())] = i
        file.write(i + '\n')
        num_str += 1
    file.close()
    return str_dict

test_str1 = ['Анекдот.','1941: ','"Guten tag"', '"o kurwa"']
result = custom_write('quest_7-2.txt', test_str1)
for elem in result.items():
    print(elem)