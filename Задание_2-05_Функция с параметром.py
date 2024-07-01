# Напишите функцию get_matrix с тремя параметрами n, m и value,
# которая будет создавать вложенный список размерами n строк и m столбцов,
# заполненную значениями value и возвращать эту матрицу в качестве результата работы.
#

m, n, value = 2, 4, 1
def det_matrix(n, m, value):

    columns = []
    matrix = []

    for i in range(m):
        columns.append(value)

    for i in range(n):
        matrix.append(columns)

    return matrix

result = det_matrix(n, m, value)
print(result)