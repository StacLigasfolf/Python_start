a = [[31, 22], [37, 43], [51, 86]]
b = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
q = [[3, 5, 8, 3], [8, 3, 7, 1]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        c = []
        for i in range(len(self.matrix)):
            c.append([])
            for j in range(len(self.matrix[0])):
                c[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
matrix_3 = Matrix(q)
print(f"Вывод матрицы :\n{matrix_1}")
print(f"{matrix_2}")
print(f"{matrix_3}")

