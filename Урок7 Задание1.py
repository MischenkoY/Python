class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        tab = '\t'
        ns = '\n'
        my_matrix = ns.join([tab.join([str(j) for j in i]) for i in self.matrix])
        return f'{my_matrix}'

    def __add__(self, other):
        try:
            sum_matrix = self.matrix
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    sum_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(sum_matrix)
        except IndexError:
            return f'Ошибка! Неверный размер матриц'


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
m_2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])
print(m_1)
print(m_2)
print(m_1+m_2)
m_3 = Matrix([[1, 2], [4, 5], [7, 8], [10, 11]])
print(m_3)
print(m_1+m_3)