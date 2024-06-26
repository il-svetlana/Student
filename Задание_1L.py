# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

# выполняется сортировка списка учеников

Students_List = sorted(set(students))
print('Сортированный список учеников: ', Students_List)

# создание листа среднего балла

MidGrades_List = [0, 0, 0, 0, 0]

MidGrades_List[0] = sum(grades[0])/len(grades[0])
MidGrades_List[1] = sum(grades[1])/len(grades[1])
MidGrades_List[2] = sum(grades[2])/len(grades[2])
MidGrades_List[3] = sum(grades[3])/len(grades[3])
MidGrades_List[4] = sum(grades[4])/len(grades[4])

print('Проверка ср. балла: ', MidGrades_List)

# создание словаря

Attestat_List = {}

Attestat_List[Students_List[0]] = MidGrades_List[0]
Attestat_List[Students_List[1]] = MidGrades_List[1]
Attestat_List[Students_List[2]] = MidGrades_List[2]
Attestat_List[Students_List[3]] = MidGrades_List[3]
Attestat_List[Students_List[4]] = MidGrades_List[4]

print('Табель успеваемости: : ', Attestat_List)
